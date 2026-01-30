skills = []

while True:
    print("\nMENU")
    print("1. Enter Your Skill")
    print("2. My Skills")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        skill = input("Enter Your Skill: ")
        skills.append(skill)
        print("Skill saved successfully!")

    elif choice == 2:
        print("Your Skills Are:")
        for s in skills:
            print("-", s)

    elif choice == 3:
        print("Exited!")
        break

    else:
        print("Invalid Choice")
