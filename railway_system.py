# railway_system.py
from train import Train

class RailWayManagementSystem:
    def __init__(self):
        self.trains = []  # list of Train objects

    def add_train(self, train):
        self.trains.append(train)

    def view_trains(self):
        if not self.trains:
            print("No trains available")
        else:
            for train in self.trains:
                print(f"Train Name: {train.name}, Train ID: {train.train_id}, Available Seats: {train.available_seats()}")

    def book_ticket(self, train_id, num=1):
        for train in self.trains:
            if train.train_id == train_id:
                if train.book_seats(num):
                    return "Ticket booked successfully."
                else:
                    return "No seats available."
        return "Train not found."

    def cancel_ticket(self, train_id, num=1):
        for train in self.trains:
            if train.train_id == train_id:
                if train.cancel_seats(num):
                    return "Ticket cancelled successfully."
                else:
                    return "Not enough booked seats to cancel."
        return "Train not found."

    def find_train_by_id(self, train_id):
        """Return Train object by ID, or None if not found."""
        for t in self.trains:
            if t.train_id == train_id:
                return t
        return None

    def remove_train(self, train_id):
        """Remove a train from the system by its ID."""
        for t in self.trains:
            if t.train_id == train_id:
                self.trains.remove(t)
                print(f"Train {t.name} (ID: {t.train_id}) has been removed.")
                return
        print("Train not found.")
