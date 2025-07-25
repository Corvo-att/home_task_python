# Home Task 1 : Control Structures and Functions
import datetime
def calc_total_price():
    global item_list,qty
    total_price = 0.0

    for i, key in enumerate(item_list):
        total_price += item_list[key] * (1 + (tax[i] / 100)) * qty[i]  # To allow the user to input the number directly without having to worry about fractions

    return total_price

item_list = {}
qty  = []
tax  = []
item = ""

def collect_prices():

    global item_list
    global tax,qty
    global item
    # Using Global Variables, so I can update and use them outside the function

    print("When you are done type 'D' ")

    while True:
        item = input("Enter the name of the item... \nInput:")
        if item == "D" or item == "d":
            break
        else:
            price = float(input("Enter its price... \nInput:"))
            item_list[item] = price
    # This allows the user to keep entering items and prices until they are done they and simply type "d"

    for key in item_list:
        rate = float(input(f"Enter the tax-rate for {key} \nInput:"))
        tax.append(rate)
        value = int(input(f"Enter the Quantity for {key} \nInput:"))
        qty.append(value)
    # Then the user is asked for the tax rates and Quantity




print("                                          \n")
print("______Welcome to Self-checkout Kiosk______\n")
#Just some print statements for visuals

collect_prices()
final_price = calc_total_price()
print(f"\nYour Final Price is {final_price:.2f} after tax.\nThank you Please Come again!\nDate:{datetime.datetime.now().replace(microsecond=0)}\n")


