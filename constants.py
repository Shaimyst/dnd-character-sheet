RACES = ["Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]

CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

BACKGROUNDS = ["Acolyte", "Criminal", "Folk Hero", "Noble", "Sage", "Soldier"]

ALIGNMENTS = [
    "Lawful Good", "Neutral Good", "Chaotic Good",
    "Lawful Neutral", "True Neutral", "Chaotic Neutral",
    "Lawful Evil", "Neutral Evil", "Chaotic Evil"
] 

RACE_DESCRIPTIONS = {
    "Dragonborn": {
        "description": "Dragonborn are descendants of mighty dragons and are typically depicted as strong martial heroes who deeply value their clans. They are reptilian-like and get a breath weapon based on the type of dragon their lineage is tied to.",
        "pros": [
            "You get to be a quasi-dragon, with draconic features",
            "Dragonborn have breath weapons that deal 2d6 damage (scales with level)",
            "Resistant to damage type associated with their ancestry"
        ],
        "considerations": [
            "No darkvision, unlike most PHB races",
            "Breath weapon uses full Action and only usable once per rest",
            "Breath weapon damage can be weak if enemies make saves"
        ]
    },
    "Dwarf": {
        "description": "Dwarves in D&D possess a knack for mining and a love for their clans and kingdoms, which stretch far into the earth. All dwarves are great for martial classes, though dwarven spellcasters are also common. The subraces in the Player's Handbook include the hill dwarf and the mountain dwarf. Hill dwarves boast a higher Wisdom score and hit points. Mountain dwarves benefit from greater Strength.",
        "pros": [
            "High Constitution (+2) and excellent defensive abilities",
            "Dwarven Resilience gives advantage on poison saves and resistance to poison damage",
            "Start with many weapon proficiencies including battleaxe and warhammer",
            "Darkvision and Stonecunning make them excellent dungeon delvers"
        ],
        "considerations": [
            "No Charisma bonus makes them suboptimal for warlocks and sorcerers",
            "Slower movement speed (25 feet)",
            "Less nimble due to emphasis on Strength over Dexterity"
        ]
    },
    "Elf": {
        "description": "Elves are D&D's longest lived race. Most elves possess an ethereal beauty reminiscent of the Feywild, as well as the potential to excel in both martial and magical pursuits. There are three elven subraces in the Player's Handbook: high elves, wood elves, and drow.",
        "pros": [
            "Extremely long-lived (adult at 100, live to 750)",
            "Only need 4 hours of meditation for a long rest",
            "High elves and drow get free magic abilities",
            "Darkvision and other racial bonuses"
        ],
        "considerations": [
            "Drow have Sunlight Sensitivity",
            "Traditional elf stereotypes might feel limiting",
            "Some may find the 'aloof elf' trope overdone"
        ]
    },
    "Gnome": {
        "description": "Gnomes are tinkerers, inventors, and lovers of life. They relish in making the most of their years, and possess infectious humor and fascination for the world. Gnomes have two subraces: Forest gnomes and Rock gnomes.",
        "pros": [
            "Second longest-lived race in the Player's Handbook",
            "Gnome Cunning grants advantage on INT, WIS, and CHA saves against magic",
            "Forest gnomes get minor illusion and can speak with Small animals",
            "Rock gnomes can construct useful devices"
        ],
        "considerations": [
            "Slow movement speed of 25 feet",
            "Intelligence boost (+2) mainly benefits wizards",
            "Small size can limit weapon choices"
        ]
    },
    "Half-Elf": {
        "description": "Half-elves are often caught between two worlds, not entirely accepted by humans nor their elvish brethren. Some manage to effortlessly exist within both worlds like cultural chameleons.",
        "pros": [
            "Combine flexibility of humans with Fey Ancestry and darkvision of elves",
            "Charisma increase of +2 and two other ability scores of choice increase by +1",
            "Start with proficiency in any two skills of choice",
            "Can't be magically put to sleep"
        ],
        "considerations": [
            "Charisma bonus might be wasted on non-Charisma based classes",
            "May face social challenges in some settings due to mixed heritage"
        ]
    },
    "Halfling": {
        "description": "Halflings are gentle folk who enjoy the pleasures of home. Those who adventure tend to be defenders of their communities or have wanderlust. There are two subraces: Lightfoot and Stout halflings.",
        "pros": [
            "Lucky trait allows rerolling 1s on d20 rolls",
            "Advantage on saving throws against being frightened",
            "Lightfoot halflings can hide behind larger creatures",
            "Stout halflings get poison resistance and saving throw advantages"
        ],
        "considerations": [
            "Slow walking speed of 25 feet",
            "Small size limits weapon options",
            "May struggle to reach enemies in melee combat"
        ]
    },
    "Half-Orc": {
        "description": "Half-orcs often navigate complex relationships with their heritage and society's treatment of their orcish side. They excel as martial powerhouses and can be compelling characters dealing with identity.",
        "pros": [
            "Relentless Endurance lets you survive at 1 HP once per long rest",
            "Savage Attacks adds extra weapon damage die on critical hits",
            "Natural strength and endurance make excellent warriors",
            "Intimidation proficiency and darkvision"
        ],
        "considerations": [
            "Limited to human/orc hybrids",
            "May face prejudice in some settings",
            "Ability score improvements mainly benefit martial classes"
        ]
    },
    "Human": {
        "description": "Humans are the most populous race in D&D. Their brief lifespans compared to longer-lived races often make them the movers and shakers who propel dramatic world events forward.",
        "pros": [
            "All ability scores increase by 1",
            "Variant humans can get a feat at 1st level",
            "Most flexible race for backstory and character concepts",
            "Fit naturally into any D&D world"
        ],
        "considerations": [
            "No special racial traits",
            "No darkvision",
            "Can feel 'vanilla' without variant human rules",
            "Shorter lifespan than most races"
        ]
    },
    "Tiefling": {
        "description": "Tieflings are individuals with devil blood in their veins, often due to ancestral pacts with denizens of the Nine Hells. They typically have horns and tails that reveal their devilish origins.",
        "pros": [
            "Resistance to fire damage",
            "Innate spellcasting (thaumaturgy, hellish rebuke, darkness)",
            "Strong Charisma (+2) and Intelligence (+1) bonuses",
            "Darkvision and unique appearance"
        ],
        "considerations": [
            "No Constitution or Dexterity bonuses",
            "May face prejudice in some settings",
            "Limited innate spell uses (once per long rest)",
            "Ability scores favor specific classes"
        ]
    }
} 

BACKGROUND_DESCRIPTIONS = {
    "Acolyte": {
        "description": "You have spent your life in service to a temple, learning sacred rites and providing various religious services. You are well-versed in religious traditions and have strong ties to a specific temple or religious organization.",
        "pros": [
            "Proficiency in Insight and Religion skills",
            "Knowledge of two additional languages",
            "Shelter of the Faithful feature lets you seek aid at temples",
            "Strong religious connections and knowledge"
        ],
        "considerations": [
            "May face conflicts between religious duties and adventure",
            "Religious beliefs might clash with party decisions",
            "Limited non-religious expertise"
        ]
    },
    "Criminal": {
        "description": "You have a history of breaking the law and still maintain contacts within the criminal underworld. You might be a reformed thief, a smuggler, or someone who was falsely accused.",
        "pros": [
            "Proficiency in Deception and Stealth",
            "Proficiency with thieves' tools and a gaming set",
            "Criminal Contact feature provides underground connections",
            "Street-smart knowledge and survival skills"
        ],
        "considerations": [
            "Past may catch up with you",
            "Law enforcement might be suspicious",
            "Criminal contacts may expect favors"
        ]
    },
    "Folk Hero": {
        "description": "You come from a humble background but are celebrated by common folk for a great deed or standing up against injustice. Your fame precedes you among ordinary people.",
        "pros": [
            "Proficiency in Animal Handling and Survival",
            "Proficiency with land vehicles and one type of artisan's tools",
            "Rustic Hospitality feature grants aid from commoners",
            "Popular among common folk"
        ],
        "considerations": [
            "Nobility might view you as uncouth",
            "Expected to help common folk in need",
            "Fame can be both helpful and hindering"
        ]
    },
    "Noble": {
        "description": "You were born into a family of wealth, power, and privilege. You carry a noble title and are accustomed to a life of luxury and responsibility.",
        "pros": [
            "Proficiency in History and Persuasion",
            "Proficiency with one gaming set",
            "Position of Privilege feature grants high-society access",
            "Wealthy background and connections"
        ],
        "considerations": [
            "May struggle with 'common' life",
            "Expected to maintain certain standards",
            "Family obligations and politics"
        ]
    },
    "Sage": {
        "description": "You spent years learning the lore of the multiverse, studying scrolls and tomes in libraries and universities. You're a scholar and academic.",
        "pros": [
            "Proficiency in Arcana and History",
            "Knowledge of two additional languages",
            "Researcher feature helps find information",
            "Broad knowledge base"
        ],
        "considerations": [
            "May lack practical experience",
            "Knowledge might be theoretical rather than practical",
            "Could be viewed as bookish or impractical"
        ]
    },
    "Soldier": {
        "description": "You were a professional fighter in an army. You might have been part of a national military, a mercenary company, or a local militia.",
        "pros": [
            "Proficiency in Athletics and Intimidation",
            "Proficiency with land vehicles and gaming set",
            "Military Rank feature grants authority with soldiers",
            "Combat experience and tactical knowledge"
        ],
        "considerations": [
            "May have enemies from past conflicts",
            "Military mindset might clash with civilians",
            "Could be called upon by former military contacts"
        ]
    }
} 

CLASS_DESCRIPTIONS = {
    "Barbarian": {
        "description": "A fierce warrior who can enter a battle rage, drawing on primal forces to enhance combat abilities. Barbarians excel at dealing and taking damage, relying on their physical might and instincts.",
        "pros": [
            "Highest hit points of any class",
            "Rage ability provides damage resistance and bonus damage",
            "Excellent physical abilities and combat skills",
            "Simple to play for beginners"
        ],
        "considerations": [
            "Limited use of magic",
            "Rage has limited uses per day",
            "May struggle in social situations",
            "Primarily melee-focused"
        ]
    },
    "Bard": {
        "description": "A magical entertainer who weaves music and performance into their spellcasting. Bards are excellent support characters who can do a bit of everything.",
        "pros": [
            "Jack of all trades feature helps with all skills",
            "Full spellcasting with unique spell list",
            "Strong social abilities and skill proficiencies",
            "Versatile support capabilities"
        ],
        "considerations": [
            "Jack of all trades, master of none",
            "Lower hit points than martial classes",
            "Requires careful spell selection",
            "Performance aspect may not appeal to all"
        ]
    },
    "Cleric": {
        "description": "A holy warrior who channels divine magic from their deity. Clerics are versatile spellcasters who can heal, fight, and support their allies.",
        "pros": [
            "Full spellcasting with divine magic",
            "Strong healing abilities",
            "Domain choices offer variety and specialization",
            "Good armor and weapon options"
        ],
        "considerations": [
            "Religious aspect may limit character choices",
            "Expected to be the party healer",
            "Divine intervention is unreliable",
            "Some domains more complex than others"
        ]
    },
    "Druid": {
        "description": "A nature-based spellcaster who can shapeshift into animals. Druids are versatile characters with strong connections to the natural world.",
        "pros": [
            "Wild Shape allows transformation into animals",
            "Full spellcasting with nature-based magic",
            "Strong utility and battlefield control",
            "Versatile role-playing opportunities"
        ],
        "considerations": [
            "Complex spell management",
            "Limited armor and weapon choices",
            "Wild Shape can be overwhelming for new players",
            "Nature theme might feel restrictive"
        ]
    },
    "Fighter": {
        "description": "A master of martial combat and weapons expertise. Fighters are reliable, versatile warriors who excel in many types of combat.",
        "pros": [
            "Multiple attacks per round",
            "Action Surge for extra actions",
            "Many fighting styles and weapon options",
            "Good for both new and experienced players"
        ],
        "considerations": [
            "Can feel simple compared to other classes",
            "Limited out-of-combat utility without specific builds",
            "May need feats to stand out",
            "Some subclasses more complex than others"
        ]
    },
    "Monk": {
        "description": "A master of martial arts who harnesses the power of ki. Monks are mobile fighters who excel at unarmed combat and quick strikes.",
        "pros": [
            "High mobility with increased movement",
            "Multiple attacks without weapons",
            "Unique abilities through ki points",
            "Strong defensive abilities"
        ],
        "considerations": [
            "Ki points are limited resource",
            "Lower hit points than other martial classes",
            "Very dependent on multiple ability scores",
            "Limited armor and weapon options"
        ]
    },
    "Paladin": {
        "description": "A holy warrior who combines martial prowess with divine magic. Paladins are powerful frontline fighters with healing and support abilities.",
        "pros": [
            "Strong damage output with Divine Smite",
            "Good healing and support abilities",
            "Excellent defensive capabilities",
            "Powerful aura effects at higher levels"
        ],
        "considerations": [
            "Must follow oath tenets",
            "Limited spell slots",
            "Requires good physical and mental stats",
            "Less effective at range"
        ]
    },
    "Ranger": {
        "description": "A warrior who combines martial skill with nature magic. Rangers excel at exploration, tracking, and specialized combat situations.",
        "pros": [
            "Good mix of combat and utility abilities",
            "Strong in wilderness settings",
            "Versatile fighting styles",
            "Unique spellcasting options"
        ],
        "considerations": [
            "Some features very situation-dependent",
            "Limited spell slots",
            "Can feel underwhelming in urban settings",
            "Favored Enemy may not come up often"
        ]
    },
    "Rogue": {
        "description": "A skilled expert who uses stealth and cunning. Rogues excel at precision strikes, skill use, and avoiding danger.",
        "pros": [
            "High single-target damage with Sneak Attack",
            "Excellent skill coverage",
            "Strong defensive abilities",
            "Useful in and out of combat"
        ],
        "considerations": [
            "Requires tactical positioning",
            "Limited multi-target abilities",
            "Can be vulnerable if caught alone",
            "Sneak Attack requirements can be restrictive"
        ]
    },
    "Sorcerer": {
        "description": "A spellcaster with innate magical abilities. Sorcerers have fewer spells known but can modify them in unique ways.",
        "pros": [
            "Full spellcasting with metamagic options",
            "Flexible spell casting through sorcery points",
            "Strong bloodline features",
            "Charisma-based social skills"
        ],
        "considerations": [
            "Limited number of spells known",
            "Low hit points and armor",
            "Resource management can be complex",
            "Less versatile than wizards"
        ]
    },
    "Warlock": {
        "description": "A spellcaster who gains power through a pact with a powerful entity. Warlocks have unique spellcasting and customization options.",
        "pros": [
            "Highly customizable through pact and invocations",
            "Spell slots recover on short rest",
            "Strong cantrip (Eldritch Blast)",
            "Unique abilities from patron"
        ],
        "considerations": [
            "Limited spell slots",
            "Complex decision-making in character building",
            "Patron may influence story",
            "Different playstyle from other spellcasters"
        ]
    },
    "Wizard": {
        "description": "A scholarly magic-user who learns spells through study. Wizards have the largest spell selection and excel at utility and control magic.",
        "pros": [
            "Largest spell list in the game",
            "Can learn new spells from scrolls",
            "Strong utility and control options",
            "Powerful high-level spells"
        ],
        "considerations": [
            "Low hit points and armor",
            "Requires careful spell preparation",
            "Dependent on spellbook",
            "Can be complex to play effectively"
        ]
    }
} 
