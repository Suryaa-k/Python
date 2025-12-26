# Q8. Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).

class HotelRoom:
    base_price_per_night = 2000

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    @staticmethod
    def is_valid_nights(nights):
        nights_str = str(nights)
        if nights_str == "" or nights_str is None:
            return False
        if nights_str[0] == '-':
            return False
        total = 0
        for char in nights_str:
            if char < '0' or char > '9':
                return False
            total = total * 10 + (ord(char) - ord('0'))
        return total > 0

    def calculate_total_bill(self):
        return self.nights_booked * HotelRoom.base_price_per_night

    @classmethod
    def update_base_price(cls, new_price):
        if new_price > 0:
            cls.base_price_per_night = new_price

print(" HOTEL ROOM BILLING SYSTEM")

room101 = HotelRoom("101", 3, "Rahul Sharma")
room205 = HotelRoom("205", 5, "Priya Singh")
room315 = HotelRoom("315", 2, "Amit Patel")

print("\n INITIAL BILLS (Base price ₹2000/night):")
print(f"Room {room101.room_number}: ₹{room101.calculate_total_bill()}")
print(f"Room {room205.room_number}: ₹{room205.calculate_total_bill()}")
print(f"Room {room315.room_number}: ₹{room315.calculate_total_bill()}")


print("\n Updating base price to ₹2500...")
HotelRoom.update_base_price(2500)

print(f"Room {room101.room_number}: ₹{room101.calculate_total_bill()}")
print(f"Room {room205.room_number}: ₹{room205.calculate_total_bill()}")
print()
print("3 nights:", HotelRoom.is_valid_nights(3))
print("0 nights:", HotelRoom.is_valid_nights(0))
print("-5 nights:", HotelRoom.is_valid_nights("-5"))
print("abc:", HotelRoom.is_valid_nights("abc"))

