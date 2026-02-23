import database

def register_attendee():

    """Prompts the user to register multiple attendees for an existing event."""
    event_id = input("Enter the Event ID for registration: ")
    if event_id not in database.events:
        print("Error: Event ID not found.")
        return

    event = database.events[event_id]

    print(f"Registering for: {event['name']} (Capacity: {len(event['attendees'])}/{event['max_attendees']})")
    print("Type 'done' as the name to finish registering attendees.")

    while True:
        # Check capacity before accepting more
        if len(event['attendees']) >= event['max_attendees']:
            print("Error: Event is full. Cannot register more attendees.")
            break

        attendee_name = input("Enter Attendee Name: ").strip()

        if attendee_name.lower() == 'done':
            break

        if not attendee_name:
            print("Name cannot be empty.")
            continue

        if attendee_name in event['attendees']:
            print(f"Error: {attendee_name} is already registered.")
            continue

        event['attendees'].append(attendee_name)

        database.save_events(database.events)

        print(f"Attendee {attendee_name} registered successfully. "
                f"({len(event['attendees'])}/{event['max_attendees']})")
