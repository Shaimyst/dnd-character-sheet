import streamlit as st
from character_sheet import CharacterSheet
from constants import (
    RACES, 
    CLASSES, 
    BACKGROUNDS, 
    ALIGNMENTS, 
    RACE_DESCRIPTIONS, 
    CLASS_DESCRIPTIONS, 
    BACKGROUND_DESCRIPTIONS
)
from database import Database

db = Database()
st.set_page_config(
    page_title="D&D Character Sheet Creator",
    page_icon="🎲",
    layout="wide"
)

st.title("D&D Character Sheet Creator 🐉")

def create_basic_info_section() -> dict[str, str]:
    print("Creating basic info section")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Character Name")
        race = st.selectbox(
            "Race",
            db.get_races(),
            help=RACE_DESCRIPTIONS.get(
                st.session_state.get(
                    'race', RACES[0]), {}).get("description", "No description available"
            )
        )
        char_class = st.selectbox(
            "Class",
            CLASSES,
            help=CLASS_DESCRIPTIONS.get(
                st.session_state.get('class', CLASSES[0]), {}).get("description", "No description available"
            )
        )
    with col2:
        level = st.number_input("Level", min_value=1, max_value=20, value=1)
        background = st.selectbox(
            "Background",
            BACKGROUNDS,
        )
        with st.expander("Background Description"):
            st.write(db.get_background_descriptions_from_background(background))
        alignment = st.selectbox("Alignment", ALIGNMENTS)
    return {
        "name": name,
        "race": race,
        "class": char_class,
        "level": level,
        "background": background,
        "alignment": alignment
    }

def create_ability_scores_section():
    st.header("Ability Scores")
    
    # Create two columns for ability scores
    col1, col2 = st.columns(2)
    
    ability_scores = {}
    
    # First column of abilities
    with col1:
        ability_scores["Strength"] = st.number_input(
            "Strength",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects melee attacks, athletic checks, and carrying capacity"
        )
        ability_scores["Dexterity"] = st.number_input(
            "Dexterity",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects AC, ranged attacks, and agility-based skills"
        )
        ability_scores["Constitution"] = st.number_input(
            "Constitution",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects HP and concentration saves"
        )
    
    # Second column of abilities
    with col2:
        ability_scores["Intelligence"] = st.number_input(
            "Intelligence",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects knowledge-based skills and wizard spellcasting"
        )
        ability_scores["Wisdom"] = st.number_input(
            "Wisdom",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects perception and cleric/druid spellcasting"
        )
        ability_scores["Charisma"] = st.number_input(
            "Charisma",
            min_value=3,
            max_value=20,
            value=10,
            help="Affects social skills and bard/sorcerer/warlock spellcasting"
        )
    
    # Display modifiers
    st.subheader("Ability Modifiers")
    for ability, score in ability_scores.items():
        modifier = (score - 10) // 2
        st.text(f"{ability}: {'+' if modifier >= 0 else ''}{modifier}")
    
    return ability_scores

# Call the function to display the form
character_info = create_basic_info_section()
ability_scores = create_ability_scores_section()

# write a file with the character info
with open("character_info.txt", "w") as f:
    print("Writing character info to file")
    for key, value in character_info.items():
        f.write(f"{key}: {value}\n")
    f.write("\nAbility Scores:\n")
    for ability, score in ability_scores.items():
        modifier = (score - 10) // 2
        f.write(f"{ability}: {score} ({'+' if modifier >= 0 else ''}{modifier})\n")

st.write("Character info has been written to character_info.txt")

# Next Steps After Basic Setup
    # play around with database file
    # read a little more about type annotations
    # change help back to being simple text
    # add picture of character types
    # Create proficiency selection system
    # Design equipment management interface
    # Add spell system for spellcasting classes
    # add file saving and loading
    # add possibility for subclasses

# Product ideas
# - call chatgpt to generate a backstory based on the character info
# - call chatgpt to generate a character image based on the character info
# - ability to save and load multiple character sheets
# - ability scores should be allocated from a pool of points
