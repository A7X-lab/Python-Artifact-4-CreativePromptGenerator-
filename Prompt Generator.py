# Creative Prompt Generator Developed By Kirklen Allen
import random
from prompts import prompts

def generate_prompt():
    print("Welcome to the Creative Prompt Generator!")
    print("Choose a category:")
    print("1. Story Ideas")
    print("2. Artwork Inspiration")
    print("3. Personal Challenges")
    print("4. Exit")

    categories = list(prompts.keys())

    while True:
        try:
            choice = int(input("Enter the number of your chosen category: "))
            if choice == 4:  # Exit
                print("Thank you for using the Creative Prompt Generator. Stay inspired!")
                break
            elif choice in range(1, 4):
                category = categories[choice - 1]
                prompt = random.choice(prompts[category])
                print(f"\nCategory: {category}")
                print(f"Your Prompt: {prompt}")
                print("\nWould you like another prompt? Type 'yes' or 'no'.")
                if input().strip().lower() != "yes":
                    break
            else:
                print("Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    generate_prompt()