from constants import (
    RACES, 
    CLASSES, 
    BACKGROUNDS, 
    ALIGNMENTS, 
    RACE_DESCRIPTIONS, 
    CLASS_DESCRIPTIONS, 
    BACKGROUND_DESCRIPTIONS
)

class Database:

    def get_races(self):
        return RACES

    def get_class_descriptions_from_class(self, char_class: str):
        return CLASS_DESCRIPTIONS.get(char_class, {}).get("description", "No description available")

    def get_background_descriptions_from_background(self, background: str):
        return BACKGROUND_DESCRIPTIONS.get(background, {}).get("description", "No description available")
