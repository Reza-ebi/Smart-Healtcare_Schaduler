"""
Smart Healthcare Appointment Scheduler (Optimized)
A simple scheduling system using greedy logic to assign patients to the earliest available time slot for each doctor.
"""

def schedule_appointments(patients, doctors, time_slots):
    schedule = []
    doctor_availability = {doctor: list(time_slots) for doctor in doctors}

    for patient in patients:
        # Choose the doctor with earliest available time
        selected_doctor = min(doctor_availability, key=lambda d: len(doctor_availability[d]))
        if doctor_availability[selected_doctor]:
            time_slot = doctor_availability[selected_doctor].pop(0)
            schedule.append((patient, selected_doctor, time_slot))
        else:
            schedule.append((patient, "No available doctor", "N/A"))

    return schedule

def main():
    patients = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fay", "George"]
    doctors = ["Dr. Smith", "Dr. Lee"]
    time_slots = ["09:00", "09:30", "10:00", "10:30", "11:00"]

    schedule = schedule_appointments(patients, doctors, time_slots)

    print("Optimized Smart Healthcare Appointment Schedule:")
    for patient, doctor, time in schedule:
        print(f"{patient} -> {doctor} at {time}")

if __name__ == "__main__":
    main()
