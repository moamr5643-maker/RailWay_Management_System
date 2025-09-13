# train.py
class Train:
    def __init__(self, name, train_id, seats):
        self.name = name
        self.train_id = train_id  
        self.seats = seats
        self.booked_seats = 0

    def book_seats(self, num=1):
        """Book a number of seats (default 1)."""
        if self.booked_seats + num <= self.seats:
            self.booked_seats += num
            return True
        else:
            return False

    def cancel_seats(self, num=1):
        """Cancel a number of booked seats (default 1)."""
        if self.booked_seats >= num:
            self.booked_seats -= num
            return True
        else:
            return False

    def available_seats(self):
        """Return number of seats available for booking."""
        return self.seats - self.booked_seats
