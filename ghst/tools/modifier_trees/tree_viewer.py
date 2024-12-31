import re
import csv
import httpx

from pathlib import Path
from rich.tree import Tree
from typing import Optional
from dataclasses import dataclass

from ghst.tools.modifier_trees.constants import (
    MODIFIER_TREE_TYPE_INFO,
    MODIFIER_TREE_OPERATOR_INFO,
    MODIFIER_TREE_OPERATOR_COLORS,
)
from ghst.tools.shared import console

DEBUG_TREE_ID = 226509

http = httpx.Client(http2=True)


def get_modifier_type_info(type: int):
    info = MODIFIER_TREE_TYPE_INFO[type]
    return info


def get_operator_color(operator: int):
    return MODIFIER_TREE_OPERATOR_COLORS[operator]


def get_operator_str(operator: int, color: bool = False):
    text = MODIFIER_TREE_OPERATOR_INFO[operator]
    if color:
        color = get_operator_color(operator)
        text = wrap_text_in_color(text, color)
    return text


def wrap_text_in_color(text: str, color: str):
    return f"[{color}]{text}[/{color}]"


def replace_token(string: str, sub: str) -> str:
    return re.sub(r"\{.*?\}", sub, string)


@dataclass
class ModifierTree:
    ID: int
    Parent: int
    Operator: int
    Amount: int
    Type: int
    Asset: int
    SecondaryAsset: int
    TertiaryAsset: int

    @staticmethod
    def from_line(line: dict[str, int]):
        line = {key: int(value) for key, value in line.items()}
        return ModifierTree(**line)

    def to_str(self) -> str:
        operator_text = get_operator_str(self.Operator, True)
        if self.Type != 0 and self.Asset != 0:
            type_info = get_modifier_type_info(self.Type)
            sub_text = f"[u deep_sky_blue1]{self.Asset}[/u deep_sky_blue1]"
            info_text = replace_token(type_info[1], sub_text)
        else:
            info_text = f"(Asset={self.Asset})" if self.Asset != 0 else ""
        text = f"[bold]ID={self.ID}[/bold] {operator_text}"
        if info_text != "":
            text += f" >> {info_text}"
        else:
            text += ":"

        return text


class TreeNode:
    value: Optional[ModifierTree] = None
    children: list
    parent = None

    def __init__(self, value: ModifierTree = None):
        self.value = value
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def fetch_modifier_tree_csv(db2csv_path: Optional[Path] = None) -> str:
    if db2csv_path is not None and db2csv_path.exists():
        console.print("Reading ModifierTree DB2 from file...")
        with open(db2csv_path, "r") as f:
            data = f.read()
    else:
        console.print("Fetching ModifierTree DB2 as csv...")
        res = http.get("https://wago.tools/db2/ModifierTree/csv")
        res.raise_for_status()
        data = res.text

    console.print("Done!")

    return data


def build_tree_db(db2_text: str) -> dict[int, TreeNode]:
    console.print("Building tree...")
    nodes = {}
    reader = csv.DictReader(db2_text.splitlines())
    for line in reader:
        tree = ModifierTree.from_line(line)
        node = nodes.setdefault(tree.ID, TreeNode(tree))
        node.value = tree
        if tree.Parent != 0:
            parent = nodes.setdefault(tree.Parent, TreeNode())
            parent.add_child(node)
        if tree.Type == 73:
            if tree.Asset != 0:
                target = nodes.setdefault(tree.Asset, TreeNode())
                node.add_child(target)
            if tree.SecondaryAsset != 0:
                target = nodes.setdefault(tree.SecondaryAsset, TreeNode())
                node.add_child(target)
            if tree.TertiaryAsset != 0:
                target = nodes.setdefault(tree.TertiaryAsset, TreeNode())
                node.add_child(target)

    console.print("Done building tree!")
    return nodes


def convert_to_rich_tree(node: TreeNode) -> Tree:
    if node.value is None:
        console.print(f"Node has no value")
        return None

    tree = Tree(node.value.to_str())
    for child in node.children:
        child: TreeNode
        child_tree = convert_to_rich_tree(child)
        if child_tree is not None:
            tree.add(child_tree)
    return tree


def get_root_node(node) -> TreeNode:
    current_node = node
    while current_node.parent is not None:
        current_node = current_node.parent

    return current_node


def cmd_dump_tree(tree_id: int, db2csv_path: Optional[Path] = None):
    data = fetch_modifier_tree_csv(db2csv_path)
    tree_db = build_tree_db(data)

    if tree_id not in tree_db:
        console.print("Target tree ID not found")
        exit(1)

    target_node = tree_db[tree_id]
    root_node = get_root_node(target_node)
    if root_node != target_node:
        console.print(f"Root ModifierTree ID: {root_node.value.ID}")

    console.print(f"ModifierTree {target_node.value.ID}:\n")

    rich_tree = convert_to_rich_tree(target_node)
    console.print(rich_tree)
