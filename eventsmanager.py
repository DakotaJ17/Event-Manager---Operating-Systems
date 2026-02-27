import events
import attendee

def main_menu():
    """Provides a command-line interface for the user to interact with the system."""
    while True:
        print("\nEvent Management System Menu:")
        print("1. Create an Event")
        print("2. Register an Attendee")
        print("3. Search Events")
        print("4. List All Events")
        print("5. Cancel an Event")
        print("6. Remove an Attendee")
        print("7. Filter By Event")
        print("8. Edit Event")
        print("9. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            events.create_event()
        elif choice == '2':
            attendee.register_attendee()
        elif choice == '3':
            events.search_events()
        elif choice == '4':
            events.list_events()
        elif choice == '5':
            events.cancel_event()
        elif choice == '6':
            attendee.remove_attendee()
        elif choice == "7":
            events.list_by_type()
        elif choice == '8':
            events.edit_event()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
if __name__ == "__main__":

    main_menu()

