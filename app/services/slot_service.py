from datetime import datetime, timedelta

def generate_slots(start_time, end_time, duration=30):
    slots = []
    fmt = "%H:%M"

    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)

    while start < end:
        slots.append(start.strftime(fmt))
        start += timedelta(minutes=duration)

    return slots
