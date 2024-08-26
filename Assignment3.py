# 1. Nested Decisions: The Adventure Game 🏰

print("Task 1: Code Correction")
place = input("Choose a place: forest or cave? ").lower()  # Convert input to lowercase for consistency

if place == "forest":  # Use '==' for comparison
    action = input("climb a tree or cross a river? ").lower()  # Convert input to lowercase for consistency
    if action == "climb a tree":  # Use '==' for comparison
        print("You found a bird's nest!")
    elif action == "cross a river":  # Use '==' for comparison and add 'elif'
        print("You found a boat!")
    else:  # Handle invalid action
        print("Invalid action. Please choose 'climb a tree' or 'cross a river'.")
elif place == "cave":  # Use '==' for comparison
    action = input("light a torch or proceed in the dark? ").lower()  # Convert input to lowercase for consistency
    if action == "light a torch":  # Use '==' for comparison
        print("You see the glitter of ancient gems!")
    elif action == "proceed in the dark":  # Use '==' for comparison
        print("You stumble upon a hidden treasure!")
    else:  # Handle invalid action
        print("Invalid action. Please choose 'light a torch' or 'proceed in the dark'.")
else:  # Handle invalid place
    print("Invalid place. Please choose 'forest' or 'cave'.")

print("\n")  # New line for separation

# 2. Quick Decisions: The Event Planner 🎉

print("Task 1: Code Correction")
attendees = int(input("Enter number of attendees: "))  # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"
print("Recommended venue:", venue)

# Task 2: Venue Selection
if attendees > 100:
    print("You might also need an audio system and a projector.")
else:
    print("A projector should be sufficient.")

# Task 3: Catering Choices
food_choice = input("Do you want vegetarian food? (yes or no) ").lower()
if food_choice == "yes":
    print("Recommended caterer: Veggie Delight Caterers.")
elif food_choice == "no":
    print("Recommended caterer: Gourmet Meals Caterers.")
else:
    print("Invalid choice for catering. Please choose 'yes' or 'no'.")
