# for a character sheet, we need to be able to store the following information:
# - name
# - race: human, elf, dwarf, etc.
# - class: warrior, mage, rogue, etc.
# - level
# - background: acolyte, charlatan, criminal, etc.
# - alignment: lawful good, neutral evil, chaotic neutral, etc.
# - experience points
# - inspiration
# - proficiencies
# - equipment
# - features and traits
# - spells and abilities
# - other notes

class CharacterSheet:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.char_class = ""
        self.level = 0
        self.background = ""
        self.alignment = ""
        self.experience_points = 0
        self.inspiration = 0
        self.proficiencies = []
        self.equipment = []
        self.features_and_traits = []
        self.spells_and_abilities = []
        self.other_notes = []

    def __str__(self):
        return f"Character Sheet for {self.name}"
