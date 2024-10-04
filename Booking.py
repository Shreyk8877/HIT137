import tkinter as tk
from tkinter import messagebox

# Use of Decorator 
# The log_action decorator logs actions when a room is booked.

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Action performed: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Use of Encapsulation
# The Room class has private attributes (__room_number and __price), which can be accessed and modified using public methods.
class Room:
    def __init__(self, room_number, price):
        self.__room_number = room_number  # private attribute to protect the data
        self.__price = price               # private attribute to protect the data
        self.available = True
  
    def get_price(self):
        return self.__price
  
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
  
    def get_description(self):
        return "Room"

    @log_action
    def book_room(self):
        self.available = False
        return f"Room {self.__room_number} booked!"

# Inherited room classes
# Use of Polymorphism:
# The get_description method is overridden in each subclass to provide specific descriptions for each room type.

class SingleRoom(Room):
    def get_description(self):
        return "Single room with one bed"

class DoubleRoom(Room):
    def get_description(self):
        return "Double room with two beds"

class SuiteRoom(Room):
    def get_description(self):
        return "Suite room with luxury amenities"

    def calculate_price(self, days):
        return super().get_price() * days * 1.5  # Suites cost more

# Use of Multiple Inheritance
# SingleRoom, DoubleRoom, and SuiteRoom classes inherit from the base class Room.


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        
        self.rooms = [
            SingleRoom("101", 100),
            DoubleRoom("102", 150),
            SuiteRoom("201", 250)
        ]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Available Rooms:").pack()
        self.room_listbox = tk.Listbox(self.root)
        self.update_room_list()
        self.room_listbox.pack()

        tk.Button(self.root, text="Book Room", command=self.book_room).pack()

    def update_room_list(self):
        self.room_listbox.delete(0, tk.END)
        for room in self.rooms:
            if room.available:
                self.room_listbox.insert(tk.END, room.get_description())
    
# Use of Overriding method
# The book_room method in the Room class is a common method, 
# while the calculate_price method in SuiteRoom overrides the base method to provide a different price calculation.

    def book_room(self):
        selected_index = self.room_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select a room to book.")
            return

        room = self.rooms[selected_index[0]]
        if room.available:
            room.book_room()
            price = room.get_price()  # Get the price of the selected room
            messagebox.showinfo("Success", f"{room.get_description()} booked successfully!\nPrice: ${price}")
            self.update_room_list()
        else:
            messagebox.showwarning("Unavailable", "This room is already booked.")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()


