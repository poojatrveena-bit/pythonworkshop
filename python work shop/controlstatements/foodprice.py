menu = {
    "Puri": 50,
    "Upma": 40,
    "Kesari Bath": 35,
    "Masala Dosa": 70,
    "Kachori": 45,
    "Paneer Tikka": 180,
    "Veg Momos": 90,
    "Chicken Momos": 120,
    "Samosa": 20,
    "Pav Bhaji": 80,
    "Chole Bhature": 100,
    "Veg Roll": 60,
    "Chicken Roll": 110,
    "Gobi Manchurian": 90,
    "Falooda": 120
}

dish = input("Enter the dish name: ")
dish = dish.title()

if dish in menu:
    print(f"The price of {dish} is ₹{menu[dish]}")
else:
    print("Sorry, this dish is not available in the menu.")