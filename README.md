# doctor_appointment_scheduler
please clone the repository.</br>
It has ai_bot.py , main.py  , requirements.txt  , logic.py , models.py  contains the source code and is written in python.</br>
create a virtual environment.</br>
Framework used: FastApi</br>
run command: pip install -r requirements.txt</br>
run command:  uvicorn main:app --reload</br>
After server start and running open http://127.0.0.1:8000/docs in browser.</br>
Add some time slots using that. For simplicity I have used a time slot for one day only and that is within 24 hrs so I have used time as a string. Please use the time as 1:00 p.m. , 2:00 p.m. , 10:00 a.m.  like that. </br>
After adding a time slot through the api.</br>
Go to the command line and run command: python ai_bot.py</br>
After running You can talk to ai_bot and ai_bot can respond with voice and text on command line.</br>
# Example
Tell me something:</br>
You said:- appointment please</br>
sure just give me a second</br>
Tell me something:</br>
You said:- continue</br>
['1:00 p.m.']</br>
Please select from these time slots:1:00 p.m. . Please select any one from them.</br>
Tell me something:</br>
You said:- 1:00 p.m.</br>
please give me your name</br>
Tell me something:</br>
You said:- Vivek</br>
please give your phone number</br>
Tell me something:</br>
You said:- 636300 8426</br>
{'patient_name': 'Vivek', 'patient_contact': '6363008426', 'time': '1:00 p.m.'}</br>
"Appointment scheduled for Vivek at 1:00 p.m. with id: 1."</br>
Awesome. I have you set up for that time. To cancel or reschedule please call us again. See you soon.</br>
