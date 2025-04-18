# Assignment 1: Design Your Own Class!
# Activity 2: Polymorphism Challenge!

# ==============================
# Part 1: Smartphone Class Design
# ==============================

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        # Constructor to initialize attributes
        self.__brand = brand  # Encapsulation: Private attribute
        self.__model = model  # Encapsulation: Private attribute
        self.storage = storage
        self.battery_life = battery_life

    # Getter for private attribute 'brand'
    def get_brand(self):
        return self.__brand

    # Getter for private attribute 'model'
    def get_model(self):
        return self.__model

    # Method to display smartphone details
    def display_info(self):
        print(
            f"Smartphone Info: {self.__brand} {self.__model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours")

    # Method to simulate making a call
    def make_call(self, number):
        print(f"Calling {number} from your {self.__brand} {self.__model}...")

# Inheritance: Subclass of Smartphone


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        # Call the parent class constructor
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu  # Additional attribute for gaming smartphones

    # Overriding the display_info method to include GPU info
    def display_info(self):
        print(
            f"Gaming Smartphone Info: {self.get_brand()} {self.get_model()}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours, GPU: {self.gpu}")

    # Method specific to gaming smartphones
    def play_game(self, game_name):
        print(
            f"Playing {game_name} on your {self.get_brand()} {self.get_model()} with {self.gpu} GPU!")


# ==============================
# Part 2: Polymorphism Challenge
# ==============================

# Base class for vehicles
class Vehicle:
    def move(self):
        # This method will be overridden in subclasses
        print("Moving...")

# Subclass Car


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass Boat


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


# ==============================
# Main Program to Test Everything
# ==============================

if __name__ == "__main__":
    print("=== Assignment 1: Smartphone Class ===")
    # Create a Smartphone object
    my_phone = Smartphone("Apple", "iPhone 14", 128, 24)
    my_phone.display_info()
    my_phone.make_call("123-456-7890")

    # Create a GamingSmartphone object
    gaming_phone = GamingSmartphone("Asus", "ROG Phone", 256, 12, "Adreno 730")
    gaming_phone.display_info()
    gaming_phone.play_game("Call of Duty")

    print("\n=== Activity 2: Polymorphism Challenge ===")
    # Create instances of different vehicles
    car = Car()
    plane = Plane()
    boat = Boat()

    # Store them in a list to demonstrate polymorphism
    vehicles = [car, plane, boat]

    # Call the move() method for each vehicle
    for vehicle in vehicles:
        vehicle.move()
