CORRECT_PASSWORD = "12345"

def main() -> None:
    prompt = "Enter password: "
    user = input(prompt)
    while user != CORRECT_PASSWORD:
        print("Incorrect password. Try again.")
        user = input(prompt)

    print("Access granted. Correct password entered.")


if __name__ == "__main__":
    main()