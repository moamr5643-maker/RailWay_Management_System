# main.py
from railway_system import RailWayManagementSystem
from train import Train

def main():
    system = RailWayManagementSystem()

    while True:
        print("\n--- Railway Management System ---")
        print("1. Add Train")
        print("2. View Trains")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. Search Train by ID")
        print("6. Remove Train")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter train name: ")
            train_id = input("Enter train ID: ")
            seats = int(input("Enter number of seats: "))
            train = Train(name, train_id, seats)
            system.add_train(train)
            print("Train added successfully.")

        elif choice == 2:
            system.view_trains()

        elif choice == 3:
            train_id = input("Enter train ID: ")
            num = int(input("Enter number of seats to book: "))
            result = system.book_ticket(train_id, num)
            print(result)

        elif choice == 4:
            train_id = input("Enter train ID: ")
            num = int(input("Enter number of seats to cancel: "))
            result = system.cancel_ticket(train_id, num)
            print(result)

        elif choice == 5:
            train_id = input("Enter train ID to search: ")
            t = system.find_train_by_id(train_id)
            if t:
                print("Train found:")
                print(f"  Name: {t.name}")
                print(f"  ID: {t.train_id}")
                print(f"  Seats total: {t.seats}")
                print(f"  Seats booked: {t.booked_seats}")
                print(f"  Seats available: {t.available_seats()}")
            else:
                print("Train not found.")

        elif choice == 6:
            train_id = input("Enter train ID to remove: ")
            system.remove_train(train_id)

        elif choice == 7:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
