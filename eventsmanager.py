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
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

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
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main_menu()