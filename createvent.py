events = {} # Global dictionary to store events

def create_event():
    """Prompts the user to create a new event."""
    event_id = input("Enter a unique Event ID: ")
    if event_id in events:
        print("Error: Event ID already exists. Please use a unique ID.")
        return

    name = input("Enter Event Name: ")
    try:
        max_attendees = int(input("Enter Maximum Attendees: "))
    except ValueError:
        print("Error: Maximum attendees must be a number.")
        return

    events[event_id] = {
        'name': name,
        'max_attendees': max_attendees,
        'attendees': [] # List to store registered attendees
    }
    print(f"Event '{name}' created successfully with ID {event_id} and capacity {max_attendees}.")

def register_attendee():
    """Prompts the user to register an attendee for an existing event."""
    event_id = input("Enter the Event ID for registration: ")
    if event_id not in events:
        print("Error: Event ID not found.")
        return

    event = events[event_id]
    if len(event['attendees']) >= event['max_attendees']:
        print("Error: Event is full. Cannot register more attendees.")
        return

    attendee_name = input("Enter Attendee Name: ")
    if attendee_name in event['attendees']:
        print("Error: Attendee is already registered for this event.")
        return

    event['attendees'].append(attendee_name)
    print(f"Attendee '{attendee_name}' registered for event '{event['name']}' successfully.")

def list_events():
    """Displays all created events and their details."""
    if not events:
        print("No events found.")
        return

    print("\nCurrent Events:")
    for event_id, event in events.items():
        print(f"\nID: {event_id}")
        print(f"Name: {event['name']}")
        print(f"Capacity: {len(event['attendees'])}/{event['max_attendees']}")
        print(f"Spots Left: {event['max_attendees'] - len(event['attendees'])}")
        print(f"Attendees: {', '.join(event['attendees']) if event['attendees'] else 'None'}")

def main_menu():
    """Provides a command-line interface for the user to interact with the system."""
    while True:
        print("\nEvent Management System Menu:")
        print("1. Create an Event")
        print("2. Register an Attendee")
        print("3. List All Events")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_event()
        elif choice == '2':
            register_attendee()
        elif choice == '3':
            list_events()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
