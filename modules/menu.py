def start_menu():

    while True:

        print("\n==============================")
        print(" AI VIDEO PIPELINE")
        print("==============================")

        print("1. Generate Script")
        print("2. Generate Voice")
        print("3. Full Pipeline")
        print("4. Settings")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print("Generate Script")

        elif choice == "2":
            print("Generate Voice")

        elif choice == "3":
            print("Run Full Pipeline")

        elif choice == "4":
            print("Settings")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")