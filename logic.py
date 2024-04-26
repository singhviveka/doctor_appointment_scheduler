from models import Appointment, TimeSlot
import itertools

# In-memory data storage
appointments = []
time_slots = []
id_counter = itertools.count(1)


def get_available_time_slots():
    res = []
    print(time_slots)
    for time_slot in time_slots:
        if time_slot.available:
            res.append(time_slot.time)
    return res


def add_time_slot(time: str):
    time_slots.append(TimeSlot(time=time, available=True))
    return "Time slot added."


def schedule_appointment(patient_name: str, patient_contact: str, time: str):
    # Check if the time slot is available
    slot = next((s for s in time_slots if s.time == time and s.available), None)
    if not slot:
        return "Time slot is not available."
    slot.available = False
    appointment = Appointment(
        id=next(id_counter),
        patient_name=patient_name,
        patient_contact=patient_contact,
        time_slot=time
    )
    appointments.append(appointment)
    return f"Appointment scheduled for {patient_name} at {time} with id: {appointment.id}."


def cancel_appointment(appointment_id: int):
    appointment = next((a for a in appointments if a.id == appointment_id), None)
    if not appointment:
        return "Appointment not found."
    appointments.remove(appointment)
    # Mark the time slot as available again
    slot = next(s for s in time_slots if s.time == appointment.time_slot)
    slot.available = True
    return "Appointment cancelled."


def reschedule_appointment(appointment_id: int, new_time: str):
    appointment = next((a for a in appointments if a.id == appointment_id), None)
    cancel_appointment(appointment_id)
    return schedule_appointment(appointment.patient_name, appointment.patient_contact, new_time)
