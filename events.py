import database


def create_event():
    event_id = input("Enter a unique Event ID: ")
    if event_id in database.events:
        print("Error: Event ID already exists. Please use a unique ID.")
        return

    name = input("Enter Event Name: ")
    date = input("Enter Event Date and Time (e.g., YYYY-MM-DD, 12:00): ")

    # Updated Selection menu
    print("\nSelect Event Type:")
    print("1. Workshop | 2. Conference | 3. Concert | 4. Social | 5. Wedding | 6. Other")
    type_choice = input("Enter choice (1-6): ")

    types = {
        "1": "Workshop",
        "2": "Conference",
        "3": "Concert",
        "4": "Social",
        "5": "Wedding",
        "6": "Other"
    }

    # Logic for "Other" or custom input
    if type_choice == "6":
        event_type = input("Enter the custom event type: ").capitalize()
    else:
        event_type = types.get(type_choice, "General")

    try:
        max_attendees = int(input("Enter Maximum Attendees: "))
    except ValueError:
        print("Error: Maximum attendees must be a number.")
        return

    database.events[event_id] = {
        "name": name,
        "date": date,
        "type": event_type,
        "max_attendees": max_attendees,
        "attendees": [],
        "status": "active"
    }


    print(f"Event '{name}' ({event_type}) created successfully with ID {event_id}.")


def search_events():
    if not database.events:
        print("No events available to search.")
        return

    print("\nSearch By: 1. ID | 2. Name | 3. Type")
    criteria = input("Enter your choice (1-3): ")

    if criteria == "1":
        search_id = input("Enter Event ID: ")
        if search_id in database.events:
            display_event_details(search_id, database.events[search_id])
        else:
            print(f"Error: No event found with ID {search_id}.")

    elif criteria == "2" or criteria == "3":
        query = input("Enter search term: ").lower()
        found = False
        # Search through both 'name' and 'type' keys
        for eid, info in database.events.items():
            if query in info['name'].lower() or query in info['type'].lower():
                print(
                    f"ID: {eid} | Name: {info['name']} | Type: {info['type']} | Spots: {info['max_attendees'] - len(info['attendees'])}")
                found = True
        if not found:
            print("No matching events found.")


def display_event_details(eid, event):
    """Helper function to keep code clean."""
    print(f"\n--- Event Details ---")
    print(f"ID: {eid} | Type: {event['type']}")
    print(f"Name: {event['name']} | Status: {event['status']}")
    print(f"Registered: {len(event['attendees'])}/{event['max_attendees']}")


def list_events():
    """Displays all created events and their details."""
    if not database.events:
        print("No events found.")
        return

    print("\nCurrent Events:")
    for event_id, event in database.events.items():
        print(f"\nID: {event_id}")
        print(f"Name: {event['name']}")
        print(f"Date: {event['date']}")
        print(f"Capacity: {len(event['attendees'])}/{event['max_attendees']}")
        print(f"Spots Left: {event['max_attendees'] - len(event['attendees'])}")
        print(f"Attendees: {', '.join(event['attendees']) if event['attendees'] else 'None'}")

def cancel_event():
    """Cancels an existing event by ID (Hard Delete)"""
    event_id = input("Enter the Event ID to cancel: ")
    if event_id not in database.events:
        print("Error: Event ID not found")
        return

    event = database.events[event_id]

    confirm = input(f"Are you sure you want to cancel '{event['name']}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancel operation aborted.")
        return

    del database.events[event_id]

    database.save_events(database.events)

    print(f"Event '{event['name']}' (ID: ) {event_id}) has been canceled.")




def list_by_type():
    """Displays events filtered by a specific category."""
    if not database.events:
        print("No events available.")
        return

    # Show available types to help the user
    print("Available types: Workshop, Conference, Concert, Social, Wedding, Other")
    search_type = input("Enter the type of event to filter by: ").capitalize()

    found = False
    print(f"\n--- {search_type} Events ---")

    for event_id, event in database.events.items():
        if event.get("type") == search_type:
            print(
                f"ID: {event_id} | Name: {event['name']} | Capacity: {len(event['attendees'])}/{event['max_attendees']}")
            found = True

    if not found:
        print(f"No events found with type: {search_type}")

def edit_event():
    """Edits an existing event by ID (soft update)."""
    event_id = input("Enter the Event ID to edit: ")
    if event_id not in database.events:
        print("Error: Event ID not found")
        return

    print(f"What would you like to edit? ")
    print(f"1. Name")
    print(f"2. Date")
    print(f"3. Time")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        database.events[event_id]['name'] = input("Enter new name: ")

    elif choice == '2':
        print("Enter the new Event Date:")
        database.events[event_id]['date'] = input("Date(YYYY-MM-DD, 12:00): ")
    else:
        print("Invalid choice.")
        return  # Stops the function early so the success message doesn't print
    database.save_events(database.events)

    print("Event updated successfully!")


