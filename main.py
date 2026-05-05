seats = 50
bookings = {}
booking_id = 1

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available seats:", seats)

    elif choice == "2":
        if seats <= 0:
            print("No seats available!")
        else:
            name = input("Enter name: ")
            age = input("Enter age: ")

            bookings[booking_id] = {
                "name": name,
                "age": age,
                "seat": seats
            }

            print("Ticket booked successfully!")
            print("Booking ID:", booking_id)

            seats -= 1
            booking_id += 1

    elif choice == "3":
        bid = int(input("Enter Booking ID: "))
        if bid in bookings:
            print("Name:", bookings[bid]["name"])
            print("Age:", bookings[bid]["age"])
            print("Seat:", bookings[bid]["seat"])
        else:
            print("Invalid Booking ID")

    elif choice == "4":
        bid = int(input("Enter Booking ID to cancel: "))
        if bid in bookings:
            del bookings[bid]
            seats += 1
            print("Ticket cancelled successfully!")
        else:
            print("Invalid Booking ID")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
