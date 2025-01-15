import streamlit as st
from character_sheet import CharacterSheet
from constants import RACES, CLASSES, BACKGROUNDS, ALIGNMENTS, RACE_DESCRIPTIONS, CLASS_DESCRIPTIONS, BACKGROUND_DESCRIPTIONS

st.set_page_config(
    page_title="D&D Character Sheet Creator",
    page_icon="🎲",
    layout="wide"
)

st.title("D&D Character Sheet Creator 🐉")

def create_basic_info_section():
    print("Creating basic info section")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Character Name")
        race = st.selectbox("Race", RACES)
        race_description = RACE_DESCRIPTIONS.get(race, "No description available.")
        char_class = st.selectbox("Class", CLASSES)
        class_description = CLASS_DESCRIPTIONS.get(char_class, "No description available.")
    with col2:
        level = st.number_input("Level", min_value=1, max_value=20, value=1)
        background = st.selectbox("Background", BACKGROUNDS)
        background_description = BACKGROUND_DESCRIPTIONS.get(background, "No description available.")
        alignment = st.selectbox("Alignment", ALIGNMENTS)
    
    return {
        "name": name,
        "race": race,
        "race_description": race_description,
        "class": char_class,
        "class_description": class_description,
        "level": level,
        "background": background,
        "background_description": background_description,
        "alignment": alignment
    }

# Call the function to display the form
character_info = create_basic_info_section()

# write a file with the character info
with open("character_info.txt", "w") as f:
    print("Writing character info to file")
    for key, value in character_info.items():
        f.write(f"{key}: {value}\n")

st.write("Character info has been written to character_info.txt")

# Next Steps After Basic Setup
    # Implement ability scores with modifiers
    # Add background features based on selection
    # Create proficiency selection system
    # Design equipment management interface
    # Add spell system for spellcasting classes
