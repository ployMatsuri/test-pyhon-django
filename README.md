# Python & Django APIs

This project contains five exam problems implemented using Python and Django REST Framework. Each problem is located in its respective folder and implements different aspects of programming and API development.

## Installation

**Clone the repository:**
```
git clone https://github.com/ployMatsuri/test-python-django.git
cd test-python-django
```

# Problems 1–4: Python Logic 
Each problem is written in **main.py** inside its respective folder

**To run:**
```
cd 1_find_tailing_zero
python main.py
```
(Do the same for problems 2–4)

# Problem 5: Django API Project
Located in the ```5-rest_api/``` folder.

This project uses Django and Django REST Framework to build a school management API, including endpoints for:
- Schools
- Classrooms
- Teachers
- Students

## ER Diagram
The following ER Diagram visualizes the database design for the school management system: ```School_DB.png```

## How to run

**1. Install dependencies:**
```
pip install -r requirements.txt
```

**2. Migrate the database:**
```
python manage.py migrate
```

**3. Run the server:**
```
python manage.py runserver
```

## Run Tests
```
python manage.py test
```

