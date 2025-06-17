Step 1: Navigate to the Project Folder
Open Command Prompt and run:
cd "C:\Users\satyam gagre\OneDrive\Desktop\PDF\CVGENERATOR"


Step 2: Activate the Virtual Environment
Move one level up, activate the environment, and return to the project folder:
cd ..
.\env\Scripts\activate
cd CVGENERATOR

Step 3: Run the Development Server
Start the Django development server:
python manage.py runserver

Then open your browser and visit:
http://127.0.0.1:8000/