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
