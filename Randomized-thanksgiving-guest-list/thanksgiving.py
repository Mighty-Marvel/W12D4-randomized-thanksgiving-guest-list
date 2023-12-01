import random
from faker import Faker

fake = Faker()

class ThanksgivingGuestList:
    def __init__(self, num_guests):
        self.guests = [fake.first_name() for i in range(num_guests)]
        self.menu = [
            "turkey", "stuffing", "cranberry sauce", "mashed potatoes", "gravy",
            "sweet potatoes", "green bean casserole", "rolls", "macaroni and cheese",
            "dressing", "green beans", "corn", "winter squash", "biscuits",
            "salad", "pecan pie", "pumpkin pie", "apple pie", "sweet potato pie",
            "quiche", "fresh fruit plate", "coffee", "tea", "apple cider", "cru de te",
            "butter"
        ]

    def randomize_guest_list(self):
        random.shuffle(self.menu)
        self.guest_assignments = dict(zip(self.guests, self.menu))

    def print_guest_list(self):
        print("Thanksgiving Guest List:")
        for guest, dish in self.guest_assignments.items():
            print(f"Guest {guest}: {dish}")

    def print_individual_guest_dish(self, guest):
        print(f"Guest {guest}'s Dish: {self.guest_assignments.get(guest, 'Unknown')}")

# Example usage
num_guests = 26
guest_list = ThanksgivingGuestList(num_guests)
guest_list.randomize_guest_list()
guest_list.print_guest_list()
guest_list.print_individual_guest_dish(guest_list.guests[2])
