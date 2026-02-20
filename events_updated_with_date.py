


def create_event():
    """Prompts the user to create a new event."""
    event_id = input("Enter a unique Event ID: ")
    if event_id in events:
        print("Error: Event ID already exists. Please use a unique ID.")
        return

    name = input("Enter Event Name: ")
    date = input("Enter Event Date (e.g., YYYY-MM-DD): ")

    try:
        max_attendees = int(input("Enter Maximum Attendees: "))
    except ValueError:
        print("Error: Maximum attendees must be a number.")
        return

    events[event_id] = {
        'name': name,
        'date': date,
        'max_attendees': max_attendees,
        'attendees': [],  # List to store registered attendees
        'status': 'active'
    }
    print(f"Event '{name}' created successfully for {date} with ID {event_id} and capacity {max_attendees}.")


def search_events():
    """Allows the user to search for events by ID or Name."""
    if not events:
        print("No events available to search.")
        return

    print("\nSearch By:")
    print("1. Event ID")
    print("2. Event Name")
    criteria = input("Enter your choice (1-2): ")

    if criteria == '1':
        # Search by exact Event ID
        search_id = input("Enter Event ID: ")
        if search_id in events:
            event = events[search_id]
            print(f"\n--- Event Found ---")
            print(f"ID: {search_id}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Status: {len(event['attendees'])}/{event['max_attendees']} attendees registered")
            print(f"Attendee List: {', '.join(event['attendees']) if event['attendees'] else 'Empty'}")
        else:
            print(f"Error: No event found with ID '{search_id}'.")

    elif criteria == '2':
        # Search by Name (partial match, case-insensitive)
        search_name = input("Enter Event Name (or part of it): ").lower()
        found = False

        print("\n--- Search Results ---")
        for event_id, event in events.items():
            if search_name in event['name'].lower():
                print(
                    f"ID: {event_id} | Name: {event['name']} | Date: {event['date']} | Spots Left: {event['max_attendees'] - len(event['attendees'])}")
                found = True

        if not found:
            print("No events found matching that name.")

    else:
        print("Invalid choice.")


def list_events():
    """Displays all created events and their details."""
    if not events:
        print("No events found.")
        return

    print("\nCurrent Events:")
    for event_id, event in events.items():
        print(f"\nID: {event_id}")
        print(f"Name: {event['name']}")
        print(f"Date: {event['date']}")
        print(f"Capacity: {len(event['attendees'])}/{event['max_attendees']}")
        print(f"Spots Left: {event['max_attendees'] - len(event['attendees'])}")
        print(f"Attendees: {', '.join(event['attendees']) if event['attendees'] else 'None'}")


def cancel_event():
    """Cancels an existing event by ID (soft delete)."""
    event_id = input("Enter the Event ID to cancel: ")
    if event_id not in events:
        print("Error: Event ID not found")
        return

    event = events[event_id]
    if event['status'] == 'canceled':
        print(f"Event '{event['name']}' is already canceled.")
        return

    confirm = input(f"Are you sure you want to cancel '{event['name']}' on {event['date']}? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancel operation aborted.")
        return

    event['status'] = 'canceled'
    print(f"Event '{event['name']}' (ID: {event_id}) has been canceled.")