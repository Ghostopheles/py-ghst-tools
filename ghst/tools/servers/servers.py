import httpx

from typing import Optional
from dataclasses import dataclass
from rich.table import Table

from ghst.tools.shared import console

GRAPHQL_URL = "https://worldofwarcraft.blizzard.com/graphql/"

headers = httpx.Headers({"Content-Type": "application/json"})
client = httpx.Client(headers=headers)


@dataclass
class RealmStatus:
    Name: str
    Slug: str
    Online: bool
    Lock: Optional[bool]


def __get_all_realm_statuses():
    data = {
        "operationName": "GetRealmStatusData",
        "variables": {"input": {"compoundRegionGameVersionSlug": "us"}},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "b37e546366a58e211e922b8c96cd1ff74249f564a49029cc9737fef3300ff175",
            }
        },
    }
    res = client.post(GRAPHQL_URL, json=data)
    res.raise_for_status()
    return res.json()


def __get_status_for_all_realms() -> list[RealmStatus]:
    realm_statuses = __get_all_realm_statuses()
    realms = []
    for realm in realm_statuses["data"]["Realms"]:
        realms.append(
            RealmStatus(
                realm["name"], realm["slug"], realm["online"], realm["realmLockStatus"]
            )
        )
    return realms


def __get_realm_status(realmSlug: str) -> Optional[RealmStatus]:
    realm_statuses = __get_all_realm_statuses()
    for realm in realm_statuses["data"]["Realms"]:
        if realm["slug"] == realmSlug:
            return RealmStatus(
                realm["name"], realm["slug"], realm["online"], realm["realmLockStatus"]
            )
    return None


def __get_status_text(status: bool):
    if status:
        return "[bold green]Online[/bold green]"
    else:
        return "[bold red]Offline[/bold red]"


def cmd_get_all_realm_statuses():
    realm_statuses = __get_status_for_all_realms()
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Name", min_width=12)
    table.add_column("Status", min_width=8)
    for realm in realm_statuses:
        name = f"[white]{realm.Name}[/white]"
        status_text = __get_status_text(realm.Online)
        table.add_row(name, status_text)

    console.print(table)


def cmd_get_realm_status(realmSlug: str):
    if realmSlug == "moonguard":
        realmSlug = "moon-guard"
    realm_status = __get_realm_status(realmSlug)
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Name", min_width=12)
    table.add_column("Status", min_width=8)
    if realm_status is not None:
        name = f"[white]{realm_status.Name}[/white]"
        status_text = __get_status_text(realm_status.Online)
        table.add_row(name, status_text)
        console.print(table)
