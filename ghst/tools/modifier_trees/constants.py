MODIFIER_TREE_OPERATOR_COLORS = {
    0: "red",
    2: "green",
    3: "red",
    4: "bright_green",
    8: "bright_red",
}

# everything below this is just taken from wow.tools.local (https://github.com/Marlamin/wow.tools.local/blob/main/wwwroot/js/enums.js)

MODIFIER_TREE_OPERATOR_INFO = {
    0: "Unknown operator",  # ???
    2: "True",  # this node must evaluate to true
    3: "False",  # this node must evaluate to false
    4: "All true",  # all child nodes must evaluate to true
    8: "Any true",  # at least one child node must evaluate to true
}

MODIFIER_TREE_TYPE_INFO = {
    0: ["NONE", "No modifier"],
    1: ["SOURCE_DRUNK_VALUE", "Player inebriation level is {#Drunkenness} or more"],
    2: ["SOURCE_PLAYER_CONDITION", 'Player meets condition "{PlayerCondition}"'],
    3: ["ITEM_LEVEL", "Minimum item level is {#Item Level}"],
    4: ["TARGET_CREATURE_ENTRY", 'Target is NPC "{Creature}"'],
    5: ["TARGET_MUST_BE_PLAYER", "Target is player"],
    6: ["TARGET_MUST_BE_DEAD", "Target is dead"],
    7: ["TARGET_MUST_BE_ENEMY", "Target is opposite faction"],
    8: ["SOURCE_HAS_AURA", 'Player has aura "{Spell}"'],
    9: ["SOURCE_HAS_AURA_TYPE", 'Player has aura effect "{SpellAuraNames.EnumID}"'],
    10: ["TARGET_HAS_AURA", 'Target has aura "{Spell}"'],
    11: ["TARGET_HAS_AURA_TYPE", 'Target has aura effect "{SpellAuraNames.EnumID}"'],
    12: ["SOURCE_AURA_STATE", 'Target has aura state "{$Aura State}"'],
    13: ["TARGET_AURA_STATE", 'Player has aura state "{$Aura State}"'],
    14: ["ITEM_QUALITY_MIN", "Item quality is at least {$Item Quality}"],
    15: ["ITEM_QUALITY_EQUALS", "Item quality is exactly {$Item Quality}"],
    16: ["SOURCE_IS_ALIVE", "Player is alive"],
    17: ["SOURCE_AREA_OR_ZONE", 'Player is in area "{AreaTable}"'],
    18: ["TARGET_AREA_OR_ZONE", 'Target is in area "{AreaTable}"'],
    19: ["ITEM_IS_ITEMID", 'Item is "{Item}"'],
    20: ["MAP_DIFFICULTY_OLD", 'Legacy dungeon difficulty is "{$Dungeon Difficulty}"'],
    21: [
        "TARGET_CREATURE_YIELDS_XP",
        "Exceeds the target's level by {#Level Delta} levels",
    ],
    22: [
        "SOURCE_LEVEL_ABOVE_TARGET",
        "Target exceeds your level by {#Level Delta} levels",
    ],
    23: ["SOURCE_LEVEL_EQUAL_TARGET", "You and the target are equal level"],
    24: ["ARENA_TYPE", "Player is in an arena with team size {#Team Size}"],
    25: ["SOURCE_RACE", 'Player race is "{ChrRaces}"'],
    26: ["SOURCE_CLASS", 'Player class is "{ChrClasses}"'],
    27: ["TARGET_RACE", 'Target race is "{ChrRaces}"'],
    28: ["TARGET_CLASS", 'Target class is "{ChrClasses}"'],
    29: ["MAX_GROUP_MEMBERS", "Less than {#Tappers} tappers"],
    30: ["TARGET_CREATURE_TYPE", 'Creature is type "{CreatureType}"'],
    31: ["TARGET_CREATURE_FAMILY", 'Creature is family "{CreatureFamily}"'],
    32: ["SOURCE_MAP", 'Player is on map "{Map}"'],
    33: ["CLIENT_VERSION", 'Milestone is at or before "{WowStaticSchemas}"'],
    34: [
        "BATTLE_PET_TEAM_LEVEL",
        "All three winning battle pets are at or above level {#Battle Pet Level}",
    ],
    35: ["NOT_IN_GROUP", "Player is not in a party"],
    36: ["IN_GROUP", "Player is in a party"],
    37: ["MIN_PERSONAL_RATING", "Has a Personal Rating of at least {#Personal Rating}"],
    38: ["TITLE_BIT_INDEX", 'Has title "{CharTitles.Mask_ID}"'],
    39: ["SOURCE_LEVEL", "Player is exactly level {#Level}"],
    40: ["TARGET_LEVEL", "Target is exactly level {#Level}"],
    41: ["SOURCE_ZONE", 'Player is in top-level area "{AreaTable}"'],
    42: ["TARGET_ZONE", 'Target is in top-level area "{AreaTable}"'],
    43: ["SOURCE_HEALTH_PCT_LOWER", "Player health below {#Percent}%"],
    44: ["SOURCE_HEALTH_PCT_GREATER", "Player health above {#Percent}%"],
    45: ["SOURCE_HEALTH_PCT_EQUAL", "Player health equals {#Percent}%"],
    46: ["TARGET_HEALTH_PCT_LOWER", "Target health below {#Percent}%"],
    47: ["TARGET_HEALTH_PCT_GREATER", "Target health above {#Percent}%"],
    48: ["TARGET_HEALTH_PCT_EQUAL", "Target health equals {#Percent}%"],
    49: ["SOURCE_HEALTH_LOWER", "Player health below {#Hit Points} HP"],
    50: ["SOURCE_HEALTH_GREATER", "Player health above {#Hit Points} HP"],
    51: ["SOURCE_HEALTH_EQUAL", "Player health equals {#Hit Points} HP"],
    52: ["TARGET_HEALTH_LOWER", "Target health below {#Hit Points} HP"],
    53: ["TARGET_HEALTH_GREATER", "Target health above {#Hit Points} HP"],
    54: ["TARGET_HEALTH_EQUAL", "Target health equals {#Hit Points} HP"],
    55: [
        "TARGET_PLAYER_CONDITION",
        'Target is a player with condition "{PlayerCondition}"',
    ],
    56: [
        "MIN_ACHIEVEMENT_POINTS",
        "Player has over {#Achievement Pts} achievement points",
    ],
    57: ["IN_LFG_DUNGEON", "Player is in a LFG dungeon"],
    58: ["IN_LFG_RANDOM_DUNGEON", "Player is in a random LFG dungeon"],
    59: ["IN_LFG_FIRST_RANDOM_DUNGEON", "Player is in a first random LFG dungeon"],
    60: ["IN_RANKED_ARENA_MATCH", "Player is in a ranked arena match"],
    61: ["REQUIRES_GUILD_GROUP", "Player is in a guild party"],
    62: [
        "GUILD_REPUTATION",
        "Player has guild reputation of {#Guild Reputation} or more",
    ],
    63: ["RATED_BATTLEGROUND", "Player is in rated battleground"],
    64: [
        "RATED_BATTLEGROUND_RATING",
        "Player has a battleground rating of {#Battleground Rating} or more",
    ],
    65: ["PROJECT_RARITY", 'Research project rarity is "{$Project Rarity}"'],
    66: ["PROJECT_RACE", 'Research project is in branch "{ResearchBranch}"'],
    67: [
        "WORLD_STATE_EXPRESSION",
        'World state expression "{WorldStateExpression}" is true',
    ],
    68: ["MAP_DIFFICULTY", 'Dungeon difficulty is "{Difficulty}"'],
    69: ["SOURCE_LEVEL_GREATER", "Player level is {#Level} or more"],
    70: ["TARGET_LEVEL_GREATER", "Target level is {#Level} or more"],
    71: ["SOURCE_LEVEL_LOWER", "Player level is {#Level} or less"],
    72: ["TARGET_LEVEL_LOWER", "Target level is {#Level} or less"],
    73: ["MODIFIER_TREE", 'Modifier tree "{ModifierTree}" is also true'],
    74: ["SCENARIO_ID", 'Player is on scenario "{Scenario}"'],
    75: ["THE_TILLERS_REPUTATION", "Reputation with Tillers is above {#Reputation}"],
    76: [
        "PET_BATTLE_ACHIEVEMENT_POINTS",
        "Battle pet achievement points are at least {#Achievement Pts}",
    ],
    77: ["UNIQUE_PETS_KNOWN", "(Account) At least {#Pets Known} unique pets known"],
    78: ["BATTLE_PET_FAMILY", 'Battlepet is of type "{$Battle Pet Types}"'],
    79: [
        "BATTLE_PET_HEALTH_PCT",
        "(Account) Battlepet's health is below {#Health Percent} percent",
    ],
    80: ["GUILD_GROUP_MEMBERS", "Be in a group with at least {#Members} guild members"],
    81: ["BATTLE_PET_ENTRY", 'Battle pet opponent is "{Creature}"'],
    82: ["SCENARIO_STEP_INDEX", "Player is on scenario step number {#Step Number}"],
    83: [
        "CHALLENGE_MODE_MEDAL",
        'Challenge mode medal earned is "{#Challenge Mode Medal(OBSOLETE)}" (OBSOLETE)',
    ],
    84: ["IS_ON_QUEST", 'Player is currently on the quest "{QuestV2}"'],
    85: ["EXALTED_WITH_FACTION", 'Reach exalted with "{Faction}"'],
    86: ["HAS_ACHIEVEMENT", 'Earned achievement "{Achievement}" on this account'],
    87: [
        "HAS_ACHIEVEMENT_ON_CHARACTER",
        'Earned achievement "{Achievement}" on this player',
    ],
    88: [
        "CLOUD_SERPENT_REPUTATION",
        "Reputation with Order of the Cloud Serpent is above {#Reputation}",
    ],
    89: [
        "BATTLE_PET_BREED_QUALITY_ID",
        'Battle pet is of quality "{BattlePetBreedQuality}"',
    ],
    90: ["PET_BATTLE_IS_PVP", "Battle pet fight was PVP"],
    91: ["BATTLE_PET_SPECIES", 'Battle pet is species type "{BattlePetSpecies}"'],
    92: [
        "ACTIVE_EXPANSION",
        'Server expansion level is "{$Expansion Level}" or higher',
    ],
    93: ["HAS_BATTLE_PET_JOURNAL_LOCK", "Player has battle pet journal lock"],
    94: [
        "FRIENDSHIP_REP_REACTION",
        'Friendship rep reaction "{FriendshipRepReaction}" is met',
    ],
    95: ["FACTION_STANDING", 'Reputation with "{Faction}" is {#Reputation} or more'],
    96: [
        "ITEM_CLASS_AND_SUBCLASS",
        'Item is class "{ItemClass.ClassID}", subclass "{^ItemSubclass.SubclassID:ItemSubclass.ClassID = ?}"',
    ],
    97: ["SOURCE_SEX", 'Player\'s gender is "{$Gender}"'],
    98: ["SOURCE_NATIVE_SEX", 'Player\'s native gender is "{$Gender}"'],
    99: ["SKILL", 'Player skill "{SkillLine}" is level {#Skill Level} or higher'],
    100: [
        "LANGUAGE_SKILL",
        'Player language "{Languages}" is level {#Language Level} or higher',
    ],
    101: ["NORMAL_PHASE_SHIFT", "Player is in normal phase"],
    102: ["IN_PHASE", 'Player is in phase "{Phase}"'],
    103: ["NOT_IN_PHASE", 'Player is in phase group "{PhaseGroup}"'],
    104: ["HAS_SPELL", 'Player knows spell "{Spell}"'],
    105: ["ITEM_COUNT", 'Player is carrying item "{Item}", quantity {#Quantity}'],
    106: [
        "ACCOUNT_EXPANSION",
        'Player expansion level is "{$Expansion Level}" or higher',
    ],
    107: ["SOURCE_HAS_AURA_LABEL", "Player has aura with label {Label}"],
    108: ["WORLDSTATE_EQUALS", 'Player\'s realm state "{WorldState}" equals {#Value}'],
    109: ["TIME_IN_RANGE", 'Time is between "{/Begin Date}" and "{/End Date}"'],
    110: ["REWARDED_QUEST", 'Player has previously completed quest "{QuestV2}"'],
    111: ["COMPLETED_QUEST", 'Player is ready to turn in quest "{QuestV2}"'],
    112: [
        "COMPLETED_QUEST_OBJECTIVE",
        'Player has completed Quest Objective "{QuestObjective}"',
    ],
    113: ["EXPLORED_AREA", 'Player has explored area "{AreaTable}"'],
    114: [
        "ITEM_COUNT_INCLUDING_BANK",
        'Player or bank has item "{Item}", quantity {#Quantity}',
    ],
    115: ["WEATHER_IS_ID", 'Weather is "{Weather}"'],
    116: ["SOURCE_PVP_FACTION_INDEX", "Player faction is {$Player Faction}"],
    117: [
        "LFG_VALUE_EQUAL",
        'Looking-for-group status "{$LFG Status}" equals {#Value}',
    ],
    118: [
        "LFG_VALUE_GREATER",
        'Looking-for-group status "{$LFG Status}" is {#Value} or more',
    ],
    119: [
        "CURRENCY_AMOUNT",
        'Player has currency "{CurrencyTypes}" in amount {#Amount} or more',
    ],
    120: [
        "CREATURE_KILL_NUM_THREAT",
        'Player Killed creature with less than "{#Targets}" threat list targets',
    ],
    121: [
        "CURRENCY_TRACKED_AMOUNT",
        'Player has currency "{CurrencyTypes}" tracked (per season) in amount {#Amount} or more',
    ],
    122: ["MAP_INSTANCE_TYPE", 'Player is on a map of type "{@INSTANCE_TYPE}"'],
    123: ["MENTOR", "Player was in a Time Walker instance"],
    124: ["PVP_SEASON_ACTIVE", "PVP season is active"],
    125: ["PVP_SEASON_CURRENT", "Current PVP season is {#Season}"],
    126: [
        "GARRISON_LEVEL_ABOVE",
        'Garrison is tier {#Tier} or higher for garrison type "{GarrType}"',
    ],
    127: [
        "GARRISON_FOLLOWERS_ABOVE_LEVEL",
        'At least {#Followers} followers of at least level {#Level} for follower type "{GarrFollowerType}"',
    ],
    128: [
        "GARRISON_FOLLOWERS_ABOVE_QUALITY",
        'At least {#Followers} followers at least quality "{@GARR_FOLLOWER_QUALITY}" for follower type "{GarrFollowerType}"',
    ],
    129: [
        "GARRISON_FOLLOWER_ABOVE_LEVEL_WITH_ABILITY",
        'Follower of at least level {#Level} has ability {GarrAbility} for follower type "{GarrFollowerType}"',
    ],
    130: [
        "GARRISON_FOLLOWER_ABOVE_LEVEL_WITH_TRAIT",
        'Follower of at least level {#Level} has trait {GarrAbility} for follower type "{GarrFollowerType}"',
    ],
    131: [
        "GARRISON_FOLLOWER_WITH_ABILITY_IN_BUILDING",
        'Follower with ability "{GarrAbility}" is assigned to building type "{@GARRISON_BUILDING_TYPE}" for garrison type "{GarrType}"',
    ],
    132: [
        "GARRISON_FOLLOWER_WITH_TRAIT_IN_BUILDING",
        'Follower with trait "{GarrAbility}" is assigned to building type "{@GARRISON_BUILDING_TYPE}" for garrison type "{GarrType}"',
    ],
    133: [
        "GARRISON_FOLLOWER_ABOVE_LEVEL_IN_BUILDING",
        'Follower at least level {#Level} is assigned to building type "{@GARRISON_BUILDING_TYPE}" for garrison type "GarrType}"',
    ],
    134: [
        "GARRISON_BUILDING_ABOVE_LEVEL",
        'Building "{@GARRISON_BUILDING_TYPE}" is at least level {#Level} for garrison type "{GarrType}"',
    ],
    135: [
        "GARRISON_BLUEPRINT",
        'Has blueprint for garrison building "{GarrBuilding}" of type "{GarrType}"',
    ],
    136: [
        "GARRISON_SPECIALIZATION",
        'Has garrison building specialization "{GarrSpecialization}"',
    ],
    137: ["GARRISON_PLOTS_FULL", 'All garrison type "{GarrType}" plots are full'],
    138: ["OWN_GARRISON", "Player is in their own garrison"],
    139: [
        "GARRISON_SHIPMENT_PENDING",
        'Shipment of type "{CharShipmentContainer}" is pending',
    ],
    140: [
        "GARRISON_BUILDING_INACTIVE",
        'Garrison building "{GarrBuilding}" is under construction',
    ],
    141: [
        "GARRISON_MISSION_COMPLETED",
        'Garrison mission "{GarrMission}" has been completed',
    ],
    142: [
        "GARRISON_BUILDING_EQUAL_LEVEL",
        'Building {@GARRISON_BUILDING_TYPE} is exactly level {#Level} for garrison type "{GarrType}"',
    ],
    143: [
        "GARRISON_FOLLOWER_WITH_ABILITY",
        'This follower has ability "{GarrAbility}" for garrison type "{GarrType}"',
    ],
    144: [
        "GARRISON_FOLLOWER_WITH_TRAIT",
        'This follower has trait "{GarrAbility}" for garrison type "{GarrType}"',
    ],
    145: [
        "GARRISON_FOLLOWER_ABOVE_QUALITY_WOD",
        "This Garrison Follower is {@GARR_FOLLOWER_QUALITY} quality",
    ],
    146: ["GARRISON_FOLLOWER_EQUAL_LEVEL", "This Garrison Follower is level {#Level}"],
    147: ["GARRISON_RARE_MISSION", "This Garrison Mission is Rare"],
    148: ["GARRISON_ELITE_MISSION", "This Garrison Mission is Elite"],
    149: ["GARRISON_BUILDING_LEVEL", "This Garrison Building is level {#Level}"],
    150: [
        "GARRISON_BUILDING_READY",
        'Garrison plot instance "{GarrPlotInstance}" has building that is ready to activate',
    ],
    151: [
        "BATTLE_PET_SPECIES_IN_TEAM",
        'Battlepet: with at least {#Amount} "{BattlePetSpecies}"',
    ],
    152: [
        "BATTLE_PET_FAMILY_IN_TEAM",
        'Battlepet: with at least {#Amount} pets of type "{$Battle Pet Types}"',
    ],
    153: [
        "BATTLE_PET_LAST_ABILITY",
        'Battlepet: last ability was "{BattlePetAbility}"',
    ],
    154: [
        "BATTLE_PET_LAST_ABILITY_TYPE",
        'Battlepet: last ability was of type "{$Battle Pet Types}"',
    ],
    155: ["BATTLE_PET_NUM_ALIVE", "Battlepet: with at least {#Alive} alive"],
    156: [
        "GARRISION_SPECIALIZATION_ACTIVE",
        'Has Garrison building active specialization "{GarrSpecialization}"',
    ],
    157: ["GARRISON_FOLLOWER_ID", 'Has Garrison follower "{GarrFollower}"'],
    158: [
        "QUEST_OBJECTIVE_PROGRESS_EQUAL",
        'Player\'s progress on Quest Objective "{QuestObjective}" is equal to {#Value}',
    ],
    159: [
        "QUEST_OBJECTIVE_PROGRESS_ABOVE",
        'Player\'s progress on Quest Objective "{QuestObjective}" is at least {#Value}',
    ],
    160: ["IS_PTR_REALM", "This is a PTR Realm"],
    161: ["IS_BETA_REALM", "This is a Beta Realm"],
    162: ["IS_QA_REALM", "This is a QA Realm"],
    163: [
        "SHIPMENT_CONTAINER_FULL",
        'Shipment Container "{CharShipmentContainer}" is full',
    ],
    164: [
        "GARRISON_INVASION_PLAYER_COUNT",
        "Player count is valid to start garrison invasion",
    ],
    165: ["INSTANCE_MAX_PLAYERS", "Instance has at most {#Players} players"],
    166: [
        "GARRISON_PLOTLEVELTYPECHECK",
        'All plots are full and at least level {#Level} for garrison type "{GarrType}"',
    ],
    167: ["GARRISON_MISSION_TYPE", 'This mission is type "{GarrMissionType}"'],
    168: [
        "GARRISON_FOLLOWER_ABOVE_ITEM_LEVEL",
        "This follower is at least item level {#Level}",
    ],
    169: [
        "GARRISON_FOLLOWERS_ABOVE_ITEM_LEVEL",
        'At least {#Followers} followers are at least item level {#Level} for follower type "{GarrFollowerType}"',
    ],
    170: [
        "GARRISON_LEVEL_EQUAL",
        'Garrison is exactly tier {#Tier} for garrison type "{GarrType}"',
    ],
    171: ["GARRISON_GROUP_SIZE", "Instance has exactly {#Players} players"],
    172: ["CURRENCY_IS_OF_ID", 'The currency is type "{CurrencyTypes}"'],
    173: ["TARGETING_CORPSE", "Target is player corpse"],
    174: ["ELIGIBLE_FOR_QUEST", 'Player is currently eligible for quest "{QuestV2}"'],
    175: [
        "GARRISON_FOLLOWERS_LEVEL_EQUAL",
        'At least {#Followers} followers exactly level {#Level} for follower type "{GarrFollowerType}"',
    ],
    176: [
        "GARRISON_FOLLOWER_ID_IN_BUILDING",
        'Garrison follower "{GarrFollower}" is in building "{GarrBuilding}"',
    ],
    177: [
        "GARRISON_AVAIL_INPROGRESS_MISSIONS",
        'Player has less than {#Available} available and {#In-Progress} in-progress missions of garrison type "{GarrType}"',
    ],
    178: [
        "GARRISON_AVAILABLE_PLOTS",
        'Player has at least {#Amount} instances of plot "{GarrPlot}" available',
    ],
    179: ["WORLD_PVP_AREA", "Currency source is {$Currency Source}"],
    180: ["NON_OWN_GARRISON", "Player is in another garrison (not their own)"],
    181: ["GARRISON_ACTIVE_FOLLOWER", 'Has active Garrison follower "{GarrFollower}"'],
    182: [
        "DAILY_RANDOM_VALUE_MOD",
        "Player daily random value mod {#Mod Value} equals {#Equals Value}",
    ],
    183: ["HAS_MOUNT", 'Player has Mount "{Mount}"'],
    184: [
        "GARRISON_FOLLOWERS_ITEM_LEVEL_ABOVE",
        'At least {#Followers} followers (including inactive) are at least item level {#Level} for follower type "{GarrFollowerType}"',
    ],
    185: [
        "GARRISON_FOLLOWER_ON_MISSION",
        'Garrison follower "{GarrFollower}" is on a mission',
    ],
    186: [
        "GARRISON_MISSIONSET_INPROGRESSAVAIL",
        'Player has less than {#Missions} available and in-progress missions of set "{GarrMissionSet}" in garrison type "{GarrType}"',
    ],
    187: [
        "GARRISON_FOLLOWER_TYPE",
        'This Garrison Follower is of type "{GarrFollowerType}"',
    ],
    188: [
        "BOOST_TIME_REAL",
        "Player has boosted and boost occurred < {#Hours} hours ago (real time)",
    ],
    189: [
        "BOOST_TIME_GAME",
        "Player has boosted and boost occurred < {#Hours} hours ago (in-game time)",
    ],
    190: ["IS_MERCENARY", "Player is currently Mercenary"],
    191: ["PLAYER_RACE_IS", 'Player effective race is "{ChrRaces}"'],
    192: ["TARGET_RACE_IS", 'Target effective race is "{ChrRaces}"'],
    193: ["HONOR_LEVEL", "Honor level >= {#Level}"],
    194: ["PRESTIGE_LEVEL", "Prestige level >= {#Level}"],
    195: [
        "GARRISON_MISSION_READY",
        'Garrison mission "{GarrMission}" is ready to collect',
    ],
    196: [
        "IS_INSTANCE_OWNER",
        "Player is the instance owner (requires 'Lock Instance Owner' LFGDungeon flag)",
    ],
    197: ["HAS_HEIRLOOM", 'Player has heirloom "{Item}"'],
    198: ["HAS_TEAM_POINTS", "Team has {#Points} Points"],
    199: ["HAS_TOY", 'Player has toy "{Item}"'],
    200: ["ITEM_MODIFIED_APPEARANCE", 'Player has transmog "{ItemModifiedAppearance}"'],
    201: ["GARRISON_SELECTED_TALENT", 'Garrison has talent "{GarrTalent}" selected'],
    202: [
        "GARRISON_RESEARCHED_TALENT",
        'Garrison has talent "{GarrTalent}" researched',
    ],
    203: [
        "HAS_CHARACTER_RESTRICTIONS",
        'Player has restriction of type "{@CHARACTER_RESTRICTION_TYPE}"',
    ],
    204: [
        "CREATED_TIME_REAL",
        "Player has created their character < {#Hours} hours ago (real time)",
    ],
    205: [
        "CREATED_TIME_GAME",
        "Player has created their character < {#Hours} hours ago (in-game time)",
    ],
    206: ["QUEST_INFO_ID", 'Quest has Quest Info "{QuestInfo}"'],
    207: [
        "GARRISON_RESEARCHING_TALENT",
        'Garrison is researching talent "{GarrTalent}"',
    ],
    208: [
        "ARTIFACT_APPEARANCE_SET_USED",
        'Player has equipped Artifact Appearance Set "{ArtifactAppearanceSet}"',
    ],
    209: [
        "CURRENCY_AMOUNT_EQUAL",
        'Player has currency "{CurrencyTypes}" in amount {#Amount} exactly',
    ],
    210: [
        "ITEM_MARK_FOR_SPEC",
        'Minimum average item high water mark is {#Item High Water Mark} for "{$Item History Spec Match}")',
    ],
    211: ["SCENARIO_TYPE", 'Player in scenario of type "{$Scenario Type}"'],
    212: [
        "ACCOUNT_EXPANSION_EQUAL",
        'Player\'s auth expansion level is "{$Expansion Level}" or higher',
    ],
    213: [
        "2V2_RATING",
        "Player achieved at least a rating of {#Rating} in 2v2 last week player played",
    ],
    214: [
        "3V3_RATING",
        "Player achieved at least a rating of {#Rating} in 3v3 last week player played",
    ],
    215: [
        "RBG_RATING",
        "Player achieved at least a rating of {#Rating} in RBG last week player played",
    ],
    216: [
        "NUM_CONNECTED_REALM_PLAYERS",
        "At least {#Num Players} members of the group are from your connected realms",
    ],
    217: [
        "ARTIFACT_NUM_TRAITS",
        'At least {#Num Traits} traits have been unlocked in artifact "{Item}"',
    ],
    218: ["PARAGON_LEVEL_EQUAL_OR_GREATER", 'Paragon level >= "{#Level}"'],
    219: [
        "CHARSHIPMENT_READY",
        'Shipment in container type "{CharShipmentContainer}" ready',
    ],
    220: ["IN_PVP_BRAWL", "Player is in PvP Brawl"],
    221: [
        "PARAGON_LEVEL_WITH_FACTION_EQUAL_OR_GREATER",
        'Paragon level >= "{#Level}" with faction "{Faction}"',
    ],
    222: [
        "ITEM_BONUS_LIST_QUALITY",
        'Player has an item with bonus list from tree "{ItemBonusTree}" and of quality "{$Item Quality}"',
    ],
    223: [
        "EMPTY_INVENTORY_SLOTS",
        'Player has at least "{#Number of empty slots}" empty inventory slots',
    ],
    224: [
        "ITEM_HISTORY_EVENT",
        'Player has item "{Item}" in the item history of progressive event "{ProgressiveEvent}"',
    ],
    225: [
        "ARTIFACT_PURCHASED_POWER_RANKS",
        "Player has at least {#Purchased Ranks} ranks of {ArtifactPower} on equipped artifact",
    ],
    226: ["USED_LEVEL_BOOST", "Player has boosted"],
    227: ["USED_RACE_CHANGE", "Player has race changed"],
    228: [
        "USED_FACTION_CHANGE",
        "Player has been granted levels from Recruit a Friend",
    ],
    229: ["IS_TOURNAMENT_REALM", "Is Tournament Realm"],
    230: ["CAN_ACCESS_ALLIED_RACE", "Player can access allied races"],
    231: [
        "ACHIEVEMENT_GLOBALLY_INCOMPLETED",
        "No More Than {#Group Members} With Achievement {Achievement} In Group (true if no group)",
    ],
    232: [
        "MAIN_HAND_VISIBLE_SUBCLASS",
        'Player has main hand weapon of type "{$Weapon Type}"',
    ],
    233: [
        "OFF_HAND_VISIBLE_SUBCLASS",
        'Player has off-hand weapon of type "{$Weapon Type}"',
    ],
    234: ["PVP_TIER", "Player is in PvP tier {PvpTier}"],
    235: [
        "AZERITE_ITEM_LEVEL",
        'Players\' Azerite Item is at or above level "{#Azerite Level}" ',
    ],
    236: ["ON_QUESTLINE", 'Player is on quest in questline "{QuestLine}"'],
    237: [
        "ON_SWG_UNLOCK_QUEST",
        'Player is on quest associated with current progressive unlock group "{ScheduledWorldStateGroup}"',
    ],
    238: ["IN_RAID_GROUP", "Player is in raid group"],
    239: [
        "PVP_TIER_GREATER",
        'Player is at or above "{@PVP_TIER_ENUM}" for "{@PVP_BRACKET}"',
    ],
    240: [
        "QUESTLINE_ELIGIBLE",
        'Player is eligible for quest in questline "{Questline}"',
    ],
    241: ["QUESTLINE_COMPLETE", 'Player has completed questline "{Questline}"'],
    242: [
        "QUESTLINE_QUEST_COMPLETE",
        'Player has completed "{#Quests}" quests in questline "{Questline}"',
    ],
    243: [
        "QUESTLINE_PCT_COMPLETE",
        'Player has completed "{#Percentage}" % of quests in questline "{Questline}"',
    ],
    244: ["IN_WARMODE", "Player has WarMode Enabled (regardless of shard state)"],
    245: ["IN_WARMODE_SHARD", "Player is on a WarMode Shard"],
    246: ["WARMODE_TOGGLE", "Player is allowed to toggle WarMode in area"],
    247: ["KEYSTONE_LEVEL", "Mythic Plus Keystone Level Atleast {#Level}"],
    248: ["KEYSTONE_COMPLETED_IN_TIME", "Mythic Plus Completed In Time"],
    249: ["KEYSTONE_DUNGEON", "Mythic Plus Map Challenge Mode {MapChallengeMode}"],
    250: ["MYTHIC_SEASON_DISPLAY", "Mythic Plus Display Season {#Season}"],
    251: ["MYTHIC_SEASON_MILESOTNE", "Mythic Plus Milestone Season {#Season}"],
    252: ["SOURCE_DISPLAY_RACE", 'Player visible race is "{ChrRaces}"'],
    253: ["TARGET_DISPLAY_RACE", 'Target visible race is "{ChrRaces}"'],
    254: [
        "FRIENDSHIP_REP_REACTION_EXACT",
        'Friendship rep reaction is exactly "{FriendshipRepReaction}"',
    ],
    255: [
        "SOURCE_AURA_COUNT_EQUAL",
        'Player has exactly {#Stacks} stacks of aura "{Spell}"',
    ],
    256: [
        "TARGET_AURA_COUNT_EQUAL",
        'Target has exactly {#Stacks} stacks of aura "{Spell}"',
    ],
    257: [
        "SOURCE_AURA_COUNT_GREATER",
        'Player has at least {#Stacks} stacks of aura "{Spell}"',
    ],
    258: [
        "TARGET_AURA_COUNT_GREATER",
        'Target has at least {#Stacks} stacks of aura "{Spell}"',
    ],
    259: [
        "UNLOCKED_AZERITE_ESSENCE_RANK_LOWER",
        "Player has Azerite Essence {AzeriteEssence} at less than rank {#rank}",
    ],
    260: [
        "UNLOCKED_AZERITE_ESSENCE_RANK_EQUAL",
        "Player has Azerite Essence {AzeriteEssence} at rank {#rank}",
    ],
    261: [
        "UNLOCKED_AZERITE_ESSENCE_RANK_GREATER",
        "Player has Azerite Essence {AzeriteEssence} at greater than rank {#rank}",
    ],
    262: [
        "SOURCE_HAS_AURA_EFFECT_INDEX",
        "Player has Aura {Spell} with Effect Index {#index} active",
    ],
    263: [
        "SOURCE_SPECIALIZATION_ROLE",
        "Player loot specialization matches role {@LFG_ROLE}",
    ],
    264: ["SOURCE_LEVEL_120", "Player is at max expansion level"],
    265: ["TRANSMOG_SOURCE_IS_OF_ID", 'Transmog Source is "{@TRANSMOG_SOURCE}"'],
    266: [
        "SELECTED_AZERITE_ESSENCE_RANK_LOWER",
        "Player has Azerite Essence in slot {@AZERITE_ESSENCE_SLOT} at less than rank {#rank}",
    ],
    267: [
        "SELECTED_AZERITE_ESSENCE_RANK_GREATER",
        "Player has Azerite Essence in slot {@AZERITE_ESSENCE_SLOT} at greater than rank {#rank}",
    ],
    268: [
        "SOURCE_LEVEL_IN_RANGE_CT",
        "Player has level within Content Tuning {ContentTuning}",
    ],
    269: [
        "TARGET_LEVEL_IN_RANGE_CT",
        "Target has level within Content Tuning {ContentTuning}",
    ],
    270: ["IS_SCENARIO_INITIATOR", "Player is Scenario Initiator"],
    271: [
        "QUEST_IS_ON_OR_HAS_COMPLETED",
        'Player is currently on or previously completed quest "{QuestV2}"',
    ],
    272: [
        "SOURCE_LEVEL_GREATER_CT",
        "Player has level within or above Content Tuning {ContentTuning}",
    ],
    273: [
        "TARGET_LEVEL_GREATER_CT",
        "Target has level within or above Content Tuning {ContentTuning}",
    ],
    274: [
        "SOURCE_LEVEL_GREATER",
        "Player has level within or above Level Range {LevelRange}",
    ],
    275: [
        "TARGET_LEVEL_GREATER",
        "Target has level within or above Level Range {LevelRange}",
    ],
    276: ["JAILER_MAX_TOWER", "Max Jailers Tower Level Atleast {#Level}"],
    277: ["RAF_RECRUIT_IN_PARTY", "Grouped With Recruit"],
    278: ["RAF_RECRUITER_IN_PARTY", "Grouped with Recruiter"],
    279: ["IS_SPECIALIZATION", 'Specialization is "{ChrSpecialization}"'],
    280: ["MAP_OR_COSMETIC_MAP", 'Player is on map or cosmetic child map "{Map}"'],
    281: [
        "HAS_SL_PREPURCHASE",
        "Player can access Shadowlands (9.0) prepurchase content",
    ],
    282: ["HAS_ENTITLEMENT", 'Player has entitlement "{BattlePayDeliverable}"'],
    283: ["HAS_QUEST_SESSION", "Player is in party sync group"],
    284: ["QUEST_PARTYSYNC_ELIGIBLE", "Quest is eligible for party sync rewards"],
    285: [
        "SPECIAL_HONOR_GAIN",
        "Player gained honor from source {@SPECIAL_MISC_HONOR_GAIN_SOURCE}",
    ],
    286: ["ACTIVE_FLOOR_MIN_LEVEL", "Active Floor Index Atleast {#Level}"],
    287: ["ACTIVE_FLOOR_DIFFICULTY", "Active Floor Difficulty Atleast {#Level}"],
    288: ["COVENANT", 'Player is member of covenant "{Covenant}"'],
    289: ["TIME_EVENT_PASSED", 'Has time event "{TimeEvent}" passed'],
    290: [
        "PERMANENT_ANIMA_DIVERSION_TALENT",
        'Garrison has permanent talent "{GarrTalent}"',
    ],
    291: ["ACTIVE_SOULBIND", 'Has Active Soulbind "{Soulbind}"'],
    292: ["HAS_MEMORIZED_SPELL", 'Has memorized spell "{Spell}"'],
    293: ["HAS_APAC_SUB_REWARD", "Player has APAC Subscription Reward 2020"],
    294: ["HAS_TBCC_WARPSTALKER_MOUNT", "Player has TBCC:DE Warp Stalker Mount"],
    295: ["HAS_TBCC_DARKPORTAL_TOY", "Player has TBCC:DE Dark Portal Toy"],
    296: ["HAS_TBCC_ILLIDAN_TOY", "Player has TBCC:DE Path of Illidan Toy"],
    297: [
        "PLAYER_HAS_IMP_SUB_REWARD",
        "Player has Imp in a Ball Toy Subscription Reward",
    ],
    298: ["PLAYER_IN_AREA_GROUP", 'Player is in area group "{AreaGroup}"'],
    299: ["TARGET_IN_AREA_GROUP", 'Target is in area group "{AreaGroup}"'],
    300: [
        "SOURCE_IN_SPECIFIC_CHROMIE_TIME",
        'Player has selected Chromie Time ID "{UiChromieTimeExpansionInfo}"',
    ],
    301: ["SOURCE_IN_ANY_CHROMIE_TIME", "Player has selected ANY Chromie Time ID"],
    302: ["ITEM_IS_AZERITE_ARMOR", "Item is Azerite Armor"],
    303: [
        "RUNEFORGED_LEGENDARY_KNOWN",
        'Player Has Runeforge Power "{RuneforgeLegendaryAbility}"',
    ],
    304: ["IS_IN_CHROMIE_TIME", "Player is Chromie Time for Scaling"],
    305: ["IS_RAF_RECRUIT", "Is RAF recruit"],
    306: ["ALL_IN_GROUP_ACH", 'All Players In Group Have Achievement "{Achievement}"'],
    307: [
        "SOULBIND_CONDUIT_RANK",
        'Player has Conduit "{SoulbindConduit}" at Rank {#Rank} or Higher',
    ],
    308: [
        "SHAPESHIFT_FORM_CUSTOMIZATION_DISPLAY",
        "Player has chosen {CreatureDisplayInfo} for shapeshift form {SpellShapeshiftForm}",
    ],
    309: [
        "SOULBIND_MIN_CONDUITS_AT_RANK",
        "Player has at least {#Level} Conduits at Rank {#Rank} or higher.",
    ],
    310: ["IS_RESTRICTED_ACCOUNT", "Player is a Restricted Account"],
    311: ["SOURCE_FLYING", "Player is flying"],
    312: ["LAST_SCENARIO_STEP", "Player is on the last step of a Scenario"],
    313: ["WEEKLY_REWARD_AVAIL", "Player has weekly rewards available"],
    314: ["TARGET_MEMBER_OF_COVENANT", 'Target is member of covenant "{Covenant}"'],
    315: ["HAS_TBC_CE", "Player has TBC Collector's Edition"],
    316: ["HAS_WOTLK_CE", "Player has Wrath Collector's Edition"],
    317: [
        "GARRISON_TALENT_RESEARCHED_AND_ACTIVE",
        'Garrison has talent "{GarrTalent}" researched and active at or above {#Rank}',
    ],
    318: [
        "CURRENCY_SPENT_IN_GARRTALENT_TREE",
        "Currency {CurrencyTypes} Spent on Garrison Talent Research in Tree {GarrTalentTree} is greater than or equal to {#Quantity}",
    ],
    319: ["RENOWN_CATCHUP_ACTIVE", "Renown Catchup Active"],
    320: ["RAPID_RENOWN_CATCHUP_ACTIVE", "Rapid Renown Catchup Active"],
    321: [
        "MYTHIC_PLUS_RATING_EQ_OR_HIGHER",
        'Player has Mythic+ Rating of at least "{#DungeonScore}"',
    ],
    322: [
        "MYTHIC_PLUS_RUN_COUNT_EQ_OR_HIGHER",
        'Player has completed at least "{#MythicKeystoneRuns}" Mythic+ runs in current expansion',
    ],
    323: [
        "PLAYER_HAS_CUSTOMIZATION_CHOICE",
        'Player has Customization Choice "{ChrCustomizationChoice}"',
    ],
    324: [
        "PLAYER_HAS_WEEKLY_PVPTIER_WIN",
        "Player has best weekly win in PVP tier {PvpTier}",
    ],
    325: [
        "PLAYER_HAS_WEEKLY_PVPTIER_WIN_EQ_OR_HIGHER",
        'Player has best weekly win at or above "{@PVP_TIER_ENUM}" for "{@PVP_BRACKET}"',
    ],
    326: ["HAS_VANILLA_CE", "Player has Vanilla Collector's Edition"],
    327: ["UNK_327", "Unknown type, bag related?"],  # Bag related
    329: ["DISPLAY_SEASON_UNK", "Display Season (unk)"],
    333: ["DISPLAY_SEASON_UNK2", "Display Season (unk2)"],
    335: ["UNK_335", "Unknown type"],  # UNK
    336: ["UNK_336", "Unknown type"],  # UNK
    337: ["UNK_337", "Unknown type"],  # UNK
    338: ["UNK_338", "Unknown type"],  # UNK
    340: ["TRAIT_NODE_ENTRY_UNK", "Trait Node Entry (unk)"],
    341: ["TRAIT_NODE_ENTRY_UNK2", "Trait Node Entry (unk2)"],
    342: ["UNK_342", "Unknown type, trait related?"],  # Also trait related
    343: ["UNK_343", "Unknown type"],  # UNK
    344: ["UNK_344", "Unknown type"],  # UNK
    350: ["UNK_350", "Unknown type"],  # UNK
    351: ["UNK_351", "Unknown type, item mod?"],  # Item mod?
    352: ["BATTLEPET_SPECIES_ID_UNK", "Battlepet species ID (unk)"],
    353: ["UNK_353", "Unknown type"],  # UNK
    355: ["TRAIT_NODE_ENTRY_UNK3", "Trait Node Entry (unk3)"],
    356: ["TRAIT_NODE_ENTRY_UNK4", "Trait Node Entry (unk4)"],
    358: ["ITEM_MODIFIED_APPEARANCE_UNK", "Item modified appearance (unk)"],
    359: ["UNK_359", "Unknown type"],  # UNK
    360: ["ITEM_BONUS_LIST_GROUP_ENTRY_UNK", "Item bonus list group entry (unk)"],
    361: ["UNK_361", "Unknown type"],  # UNK
    362: [
        "UNK_362",
        "Unknown type, achievement/item related?",
    ],  # Achievement/Item related?
    363: ["UNK_363", "Unknown type"],  # UNK
    364: ["UNK_364", "Unknown type"],  # UNK
    365: [
        "SKILL_LINE_ABILITY_OR_MOD_CRAFT_SLOT_UNK",
        "Skill line ability or mod craft slot (unk)",
    ],
    366: ["DUNGEON_ENCOUNTER_UNK", "Dungeon encounter (unk)"],
    367: ["CURRENCY_TYPES_UNK", "Currency types (unk)"],
    368: ["SKILL_LINE_ABILITY_UNK", "Skill line ability (unk)"],
    369: ["UNK_369", "Unknown type, achievement related?"],  # Achievement related?
    370: ["QUEST_LABEL_UNK", "Quest label (unk)"],
    371: ["SCENARIO_STEP_UNK", "Scenario step (unk)"],
    373: ["UNK_373", "Unknown type"],  # UNK
    374: ["UNK_374", "Unknown type"],  # UNK
    375: ["UNK_375", "Unknown type"],  # UNK
    376: ["UNK_376", "Unknown type"],  # UNK
    377: ["UNK_377", "Unknown type"],  # UNK
    378: ["PLAYER_DATA_FLAG_ACCOUNT_UNK", "Player data flag account (unk)"],
    379: ["PLAYER_DATA_FLAG_CHARACTER_UNK", "Player data flag character (unk)"],
    380: ["UNK_380", "Unknown type, map related?"],  # Map related?
    382: ["QUEST_UNK", "Quest (unk)"],
    383: ["QUEST_UNK2", "Quest (unk2)"],
    384: ["QUEST_UNK3", "Quest (unk3)"],
    387: ["UNK_387", "Unknown type"],  # UNK
    388: ["UNK_388", "Unknown type"],  # UNK
    389: ["CREATURE_CLASSIFICATION_UNK", "Creature::Classification (unk)"],
}
