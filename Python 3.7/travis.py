#List of known users

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

#Travis' Intro

while True:
    print ("Hi! My name is Travis the Security Bot.")
    name = input("What is your name?: ").strip().capitalize()

#Remove user

    if name in known_users:
        print ("Hello {}!".format(name))
        remove = input ("Would you like to be removed from the system (y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
            print ("You have been successfully removed from the system. Have a great day!")
            
        elif remove == "n" :
            print ("No problem, I didn't want you to leave anyway!")

#Add user

    else:
        print ("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input ("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y" :
            known_users.append(name)
            print("Welcome {}, you have been successfully aded to the system!".format(name))
        elif add_me == "n" :
            print ("No worries, see you around!")
    break
