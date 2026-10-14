
"""Parking lot management system with safer coding practices."""

import hashlib
import secrets

PARKING_SLOTS = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

total_collections = 0.0


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle and record its parking charge."""
    global total_collections

    if entry_logs is None:
        entry_logs = []

    if slot_id not in PARKING_SLOTS:
        return False

    slot = PARKING_SLOTS[slot_id]
    if slot["is_occupied"]:
        return False

    slot["plate"] = plate_no
    slot["hours"] = hours_booked
    slot["is_occupied"] = True

    charge = slot["rate"] * hours_booked
    total_collections += charge

    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours with total charge calculated"
    )
    return True


def release_slot(slot_id):
    """Release an occupied parking slot."""
    if slot_id not in PARKING_SLOTS:
        return False

    PARKING_SLOTS[slot_id]["is_occupied"] = False
    PARKING_SLOTS[slot_id]["plate"] = ""
    PARKING_SLOTS[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a parking slot is available."""
    slot = PARKING_SLOTS.get(slot_id)

    if slot is None:
        return False

    return not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier):
    """Calculate a parking fee using a numeric surge multiplier."""
    if slot_id not in PARKING_SLOTS:
        raise ValueError("Invalid parking slot")

    if not isinstance(surge_multiplier, (int, float)):
        raise TypeError("Surge multiplier must be numeric")

    if surge_multiplier < 0:
        raise ValueError("Surge multiplier cannot be negative")

    base_rate = PARKING_SLOTS[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Generate a SHA-256 hash of a vehicle registration number."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a four-digit ticket PIN using a secure random generator."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename="parking_manifest.txt"):
    """Export the current parking slot information to a UTF-8 file."""
    with open(filename, "w", encoding="utf-8") as manifest_file:
        manifest_file.write(str(PARKING_SLOTS))

    print("Parking manifest exported to:", filename)


def get_available_summary(slots):
    """Count the number of vacant parking slots."""
    vacant_count = 0

    for details in slots.values():
        if not details["is_occupied"]:
            vacant_count += 1

    return vacant_count


def main():
    """Run a demonstration of the parking lot system."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())

    export_parking_manifest()
    print("Vacant slots:", get_available_summary(PARKING_SLOTS))

    # Do not print or expose the actual barrier secret.
    barrier_key_configured = True
    print("Barrier Key active:", barrier_key_configured)


if __name__ == "__main__":
    main()
