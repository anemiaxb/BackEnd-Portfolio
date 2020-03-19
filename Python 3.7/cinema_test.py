# Film Selection with Tickets
# Author: anemiaxb
# Date : 2/2020
# Version: 3.8


# Films' information

films = {
    "film" : "Sonic The Hedgehog", "Harley Quinn:Birds Of Prey", "Bad Boys For Life", "Fantasy Island",
    "showtime" : 


    "showtime" :[11, 1, 3],

    "age" : 7,

    
    : [17, 10, 109],
    : [17, 10, 124],
    : [13, 10, 109]
}

# Showtimes

showtime = {
    "Sonic The Hedgehog": ["11 AM", "1 PM", "3 PM"],
    "Harley Quinn:Birds Of Prey": ["2 PM", "4 PM", "6 PM", "8 PM"],
    "Bad Boys For Life": ["4 PM", "7 PM", "10 PM"],
    "Fantasy Island": ["7 PM", "9 PM"]
}

print(
"Welcome to the cinema! We are currently showing four movies which include Sonic the Hedgehog, Harley Quinn:Birds "
    "of Prey, Bad Boys for Life, and Fantasy Island.")

while True:

    # Viewer's choice
    choice = input("What film would you like to watch?: ").strip().title()
    print(films("films", value))
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:
            # check enough seats

            while True:

            # Check seats/ask how many tickets to buy/compare to remaining tickets

                num_seats = films[choice][1]
                rem_tix_before = films[choice][1]
                buy_tix = int(input("There are {} tickets available for purchase. How many would you like to buy?: ".format(
                    films[choice][1])))
                rem_tix_after = rem_tix_before - buy_tix

                if rem_tix_after >= buy_tix:
                    print("Please proceed to checkout.")
                    break
                else:
                    print("Sorry, your purchase exceeds how many tickets are remaining.")
        else:
            print("You are too young for that film.")

    else:
        print("Sorry, we are not playing that movie.")
