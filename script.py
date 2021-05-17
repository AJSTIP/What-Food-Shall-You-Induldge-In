import random

Italian = ["Chicken Alfredo", "Uncle Vinnys Pasta and Sauce", "Lasanaga"]
Mexican = ["Tacos", "Elotes", "Sweet Tamales"]
Japanease = ["Tempura", "Udon", "Soba"]
French = ["  Potatoes Dauphinoise", "Cassoulet", "Jambon-Beurre"]


def what_to_eat():
    place = input("What kind of food are you interested in chowing on" + "\n" + "1) Italian" + "\n" + "2) Mexican" +
                  "\n" + "3) Japanease" + "\n" + "4) French" + "\n" + "5) Random" + "\n" + "Would you please enter a number 1-5: ")
    if place == "1":
        print("\n" + "No problem give me a moment.")
        print("You should consider eating: " + random.choice(Italian))
    elif place == "2":
        print("\n" + "No problem give me a moment.")
        print("You should consider eating: " + random.choice(Mexican))
    elif place == "3":
        print("\n" + "No problem give me a moment.")
        print("You should consider eating: " + random.choice(Japanease))
    elif place == "4":
        print("\n" + "No problem give me a moment.")
        print("You should consider eating: " + random.choice(French))
    elif place == "5":
        random_number = random.randint(1, 4)
        print("\n" + "To many options? Let me try to pick something for you!")
        if random_number == 1:
            print("You should consider eating: " + random.choice(Italian))
        elif random_number == 2:
            print("You should consider eating: " + random.choice(Mexican))
        elif random_number == 3:
            print("You should consider eating: " + random.choice(Japanease))
        elif random_number == 4:
            print("You should consider eating: " + random.choice(French))
    else:
        print("Make sure you only enter a number 1 - 5 only")


what_to_eat()
