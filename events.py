from database import events

def create_event():
    """Prompts the user to create a new event."""
    event_id = input("Enter a unique Event ID: ")
    if event_id in events:
        print("Error: Event ID already exists. Please use a unique ID.")
        return

    name = input("Enter Event Name: ")
    print(f"Enter the Event Date: ")
    month = input(f"Month: ")
    day = input(f"Day: ")
    year = input(f"Year: ")
    time = input(f"Time: ")
    
    try:
        max_attendees = int(input("Enter Maximum Attendees: "))
    except ValueError:
        print("Error: Maximum attendees must be a number.")
        return

    events[event_id] = {
        'name': name,
        'month': month,
        'day': day,
        'year': year,
        'time': time,
        'max_attendees': max_attendees,
        'attendees': [], # List to store registered attendees
        'status': 'active'
    }
    print(f"Event '{name}', on {month} {day}, {year}, created successfully with ID {event_id} and capacity {max_attendees}.")

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
             print(f"Date: {event['month']} {event['day']}, {event['year']} at {event['time']}")
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
                    f"ID: {event_id} | Name: {event['name']} | Spots Left: {event['max_attendees'] - len(event['attendees'])}")
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
        print(f"Date: {event['month']} {event['day']}, {event['year']} at {event['time']}")
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

    confirm = input(f"Are you sure you want to cancel '{event['name']}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancel operation aborted.")
        return

    event['status'] = 'canceled'
    print(f"Event '{event['name']}' (ID: ) {event_id}) has been canceled.")


def edit_event():
    """Edits an existing event by ID (soft update)."""
    event_id = input("Enter the Event ID to edit: ")
    if event_id not in events:
        print("Error: Event ID not found")
        return

    print(f"What would you like to edit? ")
    print(f"1. Name")
    print(f"2. Date")
    print(f"3. Time")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        events[event_id]['name'] = input("Enter new name: ")

    elif choice == '2':
        print("Enter the new Event Date:")
        events[event_id]['month'] = input("Month: ")

        # --- Day Validation ---
        while True:
            day = input("Day (1-31): ")
            if day.isdigit() and 1 <= int(day) <= 31:
                events[event_id]['day'] = day
                break  # Exits the loop if the input is valid
            else:
                print("Error: Please enter a valid number for the day (1-31).")

        # --- Year Validation ---
        while True:
            year = input("Year (YYYY): ")
            if year.isdigit() and len(year) == 4:
                events[event_id]['year'] = year
                break  # Exits the loop if the input is valid
            else:
                print("Error: Please enter a valid 4-digit year.")

    elif choice == '3':
        events[event_id]['time'] = input("Enter new time: ")

    else:
        print("Invalid choice.")
        return  # Stops the function early so the success message doesn't print

    print("Event updated successfully!")


