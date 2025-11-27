capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
}

def ask_question(country: str, capital: str) -> bool:
    """Ask one question and return True if correct."""
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is {capital}.")
        return False

def main() -> None:
    print("European Capitals Quiz\n")
    score = 0
    for country, capital in capitals.items():
        if ask_question(country, capital):
            score += 1

    print(f"\nYour final score: {score}/{len(capitals)}")

if __name__ == "__main__":
    main()