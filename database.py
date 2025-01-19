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

    def get_classes(self):
        return CLASSES

    def get_backgrounds(self):
        return BACKGROUNDS

    def get_alignments(self):
        return ALIGNMENTS

    def get_class_descriptions_from_class(self, char_class: str):
        return CLASS_DESCRIPTIONS.get(char_class, {}).get("description", "No description available")

    def get_background_descriptions_from_background(self, background: str):
        return BACKGROUND_DESCRIPTIONS.get(background, {}).get("description", "No description available")
        
    def get_race_descriptions_from_race(self, race: str):
        return RACE_DESCRIPTIONS.get(race, {}).get("description", "No description available")
    
    def get_race_pros_from_race(self, race: str):
        return RACE_DESCRIPTIONS.get(race, {}).get("pros", [])
    
    def get_race_considerations_from_race(self, race: str):
        return RACE_DESCRIPTIONS.get(race, {}).get("considerations", [])
