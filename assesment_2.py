# FixTrack Console Application

orders = []

def add_order():
    name = input("Enter customer name: ")
    device = input("Enter device type: ")
    issue = input("Enter issue: ")
    due_date = input("Enter due date: ")

    order = {
        "name": name,
        "device": device,
        "issue": issue,
        "due_date": due_date
    }

    orders.append(order)
    print("\nRepair order added successfully!\n")


def generate_bill():
    if not orders:
        print("No repair orders found.\n")
        return

    fee = float(input("Enter repair fee: "))
    parts = float(input("Enter parts cost: "))

    subtotal = fee + parts
    tax = subtotal * 0.18
    discount = float(input("Enter discount (0 if none): "))

    total = subtotal + tax - discount

    print("\n----- FIXTRACK INVOICE -----")
    print("Repair Fee:", fee)
    print("Parts Cost:", parts)
    print("Tax (0.18%):", tax)
    print("Discount:", discount)
    print("Total Amount:", total)
    print("----------------------------\n")


def main():
    while True:
        print("1. Add Repair Order")
        print("2. Generate Bill")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            generate_bill()
        elif choice == "3":
            print("Exiting FixTrack. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
