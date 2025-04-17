import random

name = "Your Name Here"
admission_number = "YourID1234"

print(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

mood = input("\nHow are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        f"Great things await you, {name.split()[0]}! Keep smiling.",
        "Happiness is contagious – spread it everywhere you go!"
    ],
    "sad": [
        "This too shall pass. Keep your head up!",
        "Every storm runs out of rain – better times ahead!"
    ],
    "neutral": [
        "A surprise opportunity is around the corner. Stay alert!",
        "Calm minds build powerful futures. Stay steady!"
    ],
    "stressed": [
        f"Take a deep breath, {name.split()[0]}. You’ve got this.",
        "Stress fades when purpose takes its place. You’re strong!"
    ]
}

if mood in fortunes:
    print("\n✨ Your fortune:", random.choice(fortunes[mood]), "✨")
else:
    print("\n❗ Mood not recognized. Please enter one of: happy/sad/neutral/stressed.")
