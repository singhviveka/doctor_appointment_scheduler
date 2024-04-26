from typing import List, Optional
from pydantic import BaseModel, Field


class Appointment(BaseModel):
    id: int
    patient_name: str
    patient_contact: str
    time_slot: str


class TimeSlot(BaseModel):
    time: str
    available: bool = True
