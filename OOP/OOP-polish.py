import math
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = 3.142 * (self.radius**2)
        return area
    def calculate_perimeter(self):
        perimeter = 3.142 * (self.radius *2)
        return perimeter
from datetime import date
class Person:
   
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.birth_day =date_of_birth

    def calculate_age(self):
        today_date = date.today()
        age = today_date.year - self.birth_day.year
        if today_date < date(today_date.year, self.birth_day.month, self.birth_day.day):
            age -= 1

        return(age)
 
    
    def __str__(self):
        age_in_years = self.calculate_age()
        return(
            f"Name: {self.name}\n"
            f"Country: {self.country}\n"
            f"Year_of_birth: {self.birth_day}\n"
            f"Age: {age_in_years}"

        )

class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = math.pi * (self.radius**2)
        return area
    def calculate_perimeter(self):
        perimeter = 2* math.pi * (self.radius *2)
        return perimeter
    def __str__(self):
        area_circle = self.calculate_area()
        perimeter_circle = self.calculate_perimeter()
        return (
            f"Radius of the Circle: {self.radius}\n"
            f"Area of the Circle: {area_circle}\n"
            f"Perimeter of the Circle: {perimeter_circle}"
        )

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def __str__(self):
        area_rectangle = self.calculate_area()
        perimeter_rectangle= self.calculate_perimeter()
        return (
            f"\n"
            f"Rectangle: Length = {self.length} Width = {self.width}\n"
            f"Area of the Rectangle: {area_rectangle}\n"
            f"Perimeter of the Rectangle: {perimeter_rectangle}"
        )
class Triangle(Shape):
    def __init__(self, base , height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def calculate_perimeter(self):
        return self.side1 + self.side2 +self.side3
    
    def __str__(self):
        area_triangle = self.calculate_area()
        perimeter_triangle= self.calculate_perimeter()
        return (
            f"\n"
            f"Triangle: Base = {self.base}, Height = {self.height}, Side1 = {self.side1}, Side2 = {self.side2}, Side3 = {self.side3}\n"
            f"Area of the Triangle: {area_triangle}\n"
            f"Perimeter of the Triangle: {perimeter_triangle}"
        )


class Stack: 
    def __init__(self):
        self.items = []
    
    def add_items(self, item):
        return self.items.append(item)
    def remove_item(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Cannot pop an empty stack")

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Empty stack!")
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items


class ShoppingCart:
    """
    Requirements:
        Item name 
        Price
    Methods:
        Adding items
        Removing items
        Viewing items picked
        Calculate the total price
        Update quantity of items picked
        Exiting the program

    """
    def __init__(self):
        
        self.items_picked = {}
        self.items_price = {}
    
    def is_Empty(self):
        return len(self.items_picked) == 0
    def add_item(self, productName, quantity, price):
        self.items_picked[productName] = quantity
        self.items_price[productName] = price   
   

    
    def remove_items(self, item):
        try: 
            del self.items_picked[item] 
        except KeyError:
            print("Key Not Found!")
    def show_items_price(self):
        return  list(self.items_price)

    def show_items_quantity(self):
        return self.items_picked
    
    def calculate_price(self):
        total_Price = 0
        for item in self.items_price:
            if item in self.items_picked:
                item_total = self.items_price[item] * self.items_picked[item]
                total_Price += item_total
                print(f"{item}: Quantity = {self.items_picked[item]}, Price = {self.items_price[item]}, Total = {item_total}")

            
        return f"Total:{total_Price}"

def prompt_User():
    print("Welcome to Kenuwn Sales store: \n")
    c1 = ShoppingCart()
    while True:
        
        item = input("Enter the name of goods to buy: ")
        item_price = int(input("Enter the item price: "))
        item_quantity = int(input(f"Enter amount of {item} to buy:  "))
        c1.add_item(item, item_quantity, item_price)
        add_more = input("Do you want to add more items (yes/no): ").lower()
        
        
        
        
        if add_more != "yes":
            remove_inquiry = input("Is there you want to remove (yes/no): ").lower()
            if remove_inquiry == "yes":
                remove_item = input("Enter name of the item you want to remove: ")
                c1.remove_items(remove_item)
            print(c1.show_items_price())
            print(c1.show_items_quantity())
            print(c1.calculate_price())  
            break


prompt_User()
    








    


        
