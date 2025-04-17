import sys

# Personal Info
name = "Your Name Here"          # ✏️ Replace with your full name
admission_number = "YourID1234"  # ✏️ Replace with your admission number

# Welcome Message
print(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

# Ask for mood
mood = input("\nHow are you feeling today? (happy/sad/neutral): ").strip().lower()

# Fortune responses
if mood == "happy":
    print(f"\n✨ Your fortune: Great things await you, {name.split()[0]}! Keep smiling. ✨")
elif mood == "sad":
    print("\n✨ Your fortune: Tough times don’t last, but tough people do. Better days are coming! ✨")
elif mood == "neutral":
    print("\n✨ Your fortune: A surprise opportunity is around the corner. Stay alert! ✨")
else:
    print("\n❗ I don't have a fortune for that mood. Try again with happy/sad/neutral.")
    sys.exit(1)
