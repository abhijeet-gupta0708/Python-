# Virtual Pet Simulator

def feed_pet(hunger, happiness):
    hunger -= 20
    happiness -= 5

    hunger = max(0, hunger)
    happiness = max(0, happiness)

    print("\nYou fed your pet.")
    return hunger, happiness


def play_with_pet(hunger, happiness):
    hunger += 10
    happiness += 15

    hunger = min(100, hunger)
    happiness = min(100, happiness)

    print("\nYou played with your pet.")
    return hunger, happiness


def check_status(name, hunger, happiness):
    print("\n------ Pet Status ------")
    print("Pet Name:", name)
    print("Hunger:", hunger)
    print("Happiness:", happiness)
    print("------------------------")


# Bonus: Pet Naming
pet_name = input("Enter your pet's name: ")

hunger = 50
happiness = 50

while True:

    print("\n===== Virtual Pet Menu =====")
    print("1. Feed Pet")
    print("2. Play With Pet")
    print("3. Check Status")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hunger, happiness = feed_pet(hunger, happiness)

    elif choice == "2":
        hunger, happiness = play_with_pet(hunger, happiness)

    elif choice == "3":
        check_status(pet_name, hunger, happiness)

    elif choice == "4":
        print("\nThanks for playing!")
        break

    else:
        print("\nInvalid Choice!")
        continue

    # Automatic changes
    hunger += 5
    happiness -= 5

    hunger = min(100, hunger)
    happiness = max(0, happiness)

    # Game Over Conditions
    if hunger >= 100:
        print("\nYour pet became too hungry!")
        print("Game Over.")
        break

    if happiness <= 0:
        print("\nYour pet became too sad!")
        print("Game Over.")
        break