from fastapi import FastAPI, HTTPException
import logic

app = FastAPI()


@app.post("/add-time-slot/")
def add_time_slot(time: str):
    return logic.add_time_slot(time)


@app.post("/schedule-appointment/")
def schedule_appointment(patient_name: str, patient_contact: str, time: str):
    return logic.schedule_appointment(patient_name, patient_contact, time)


@app.post("/cancel-appointment/")
def cancel_appointment(appointment_id: int):
    return logic.cancel_appointment(appointment_id)


@app.post("/reschedule-appointment/")
def reschedule_appointment(appointment_id: int, new_time: str):
    return logic.reschedule_appointment(appointment_id, new_time)


@app.get('/get_all_available_slots')
def get_available_slots():
    return logic.get_available_time_slots()
