#Films info

films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghostbusters": [12, 5]
}

print("Welcome to the cinema! We are currently showing four movies which include Finding Dory, Tarzan, Bourne,"
      "and Ghost Busters.")


while True:

    # Viewer's choice
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:
            # check enough seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
