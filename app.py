import streamlit as st
from database import Database
from typing import Dict, List

db = Database()
st.set_page_config(
    page_title="D&D Character Sheet Creator",
    page_icon="🎲",
    layout="wide"
)

st.title("D&D Character Sheet Creator 🐉")

def create_basic_info_section() -> Dict[str, str | int]:
    """Creates and returns the basic character information section.
    
    Returns:
        Dict[str, str | int]: Dictionary containing character details where values are either strings or integers
    """
    print("Creating basic info section")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Character Name")
        race = st.selectbox(
            "Race",
            db.get_races(),
            )
        with st.expander("Race Description"):
            st.write(db.get_race_descriptions_from_race(race))
            st.write("**Pros:**")
            pros = db.get_race_pros_from_race(race)
            for pro in pros:
                st.write(f"• {pro}")
            st.write("**Considerations:**")
            considerations = db.get_race_considerations_from_race(race)
            for consideration in considerations:
                st.write(f"• {consideration}")
        char_class = st.selectbox(
            "Class",
            db.get_classes(),
        )
        with st.expander("Class Description"):
            st.write(db.get_class_descriptions_from_class(char_class))
    with col2:
        level = st.number_input("Level", min_value=1, max_value=20, value=1)
        background = st.selectbox(
            "Background",
            db.get_backgrounds(),
        )
        with st.expander("Background Description"):
            st.write(db.get_background_descriptions_from_background(background))
        alignment = st.selectbox("Alignment", db.get_alignments())
    return {
        "name": name,
        "race": race,
        "class": char_class,
        "level": level,
        "background": background,
        "alignment": alignment
    }

def create_ability_scores_section() -> Dict[str, int]:
    """Creates and returns the ability scores section.
    
    Returns:
        Dict[str, int]: Dictionary of ability scores where keys are ability names and values are scores
    """
    st.header("Ability Scores")

    # add ability score pool
    remaining_points = st.empty()  # Placeholder for remaining points display
    total_points = 27
    
    # Create two columns for ability scores
    col1, col2 = st.columns(2)
    
    ability_scores = {}
    used_points = 0
    
    # First column of abilities
    with col1:
        for ability in ["Strength", "Dexterity", "Constitution"]:
            score = st.number_input(
                ability,
                min_value=8,  # Standard D&D point buy minimum
                max_value=15,  # Standard D&D point buy maximum
                value=8,
                help=get_ability_help_text(ability)
            )
            ability_scores[ability] = score
            used_points += calculate_point_cost(score)
    
    # Second column of abilities
    with col2:
        for ability in ["Intelligence", "Wisdom", "Charisma"]:
            score = st.number_input(
                ability,
                min_value=8,
                max_value=15,
                value=8,
                help=get_ability_help_text(ability)
            )
            ability_scores[ability] = score
            used_points += calculate_point_cost(score)
    
    # Display remaining points
    points_left = total_points - used_points
    remaining_points.markdown(f"**Remaining Points: {points_left}** (Total: {total_points})")
    if points_left < 0:
        st.error("You have used too many points! Please adjust your ability scores.")
    
    # Display modifiers
    st.subheader("Ability Modifiers")
    for ability, score in ability_scores.items():
        modifier = (score - 10) // 2
        st.text(f"{ability}: {'+' if modifier >= 0 else ''}{modifier}")
    
    return ability_scores

def calculate_point_cost(score: int) -> int:
    """Calculate the point cost for a given ability score using standard D&D 5e point buy rules."""
    point_costs = {
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 4,
        13: 5,
        14: 7,
        15: 9
    }
    return point_costs.get(score, 0)

def get_ability_help_text(ability: str) -> str:
    """Return help text for each ability score."""
    help_texts = {
        "Strength": "Affects melee attacks, athletic checks, and carrying capacity",
        "Dexterity": "Affects AC, ranged attacks, and agility-based skills",
        "Constitution": "Affects HP and concentration saves",
        "Intelligence": "Affects knowledge-based skills and wizard spellcasting",
        "Wisdom": "Affects perception and cleric/druid spellcasting",
        "Charisma": "Affects social skills and bard/sorcerer/warlock spellcasting"
    }
    return help_texts.get(ability, "")

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
