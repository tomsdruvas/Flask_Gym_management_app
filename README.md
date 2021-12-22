![PostgresQL](https://img.shields.io/badge/PostgreSQL-v14.0-red?style=appveyor&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0.2+-black?style=appveyor&logo=flask&logoColor=white?)
![Python](https://img.shields.io/badge/python-v3.9+-blue.svg?style=appveyor)
![CSS](https://img.shields.io/badge/CSS3-1572B6??&style=appveyor&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26??style=appveyor&logo=html5&logoColor=white+)

## About

Solo project for the Python module at the Professional Software Development Bootcamp at CodeClan.

The web app is full-stack and it's built using Flask, Python, PostgreSQL, HTML and CSS

## Pictures
# A list of gym classes
<img src="/planning_and_dev/class_list1.png" width="400" > 

# Viewing a gym class
<img src="/planning_and_dev/class_view.png" width="400" >

# Members list
<img src="/planning_and_dev/members_list.png" width="400" >

# Viewing a single member
<img src="/planning_and_dev/member_view.png" width="400" >

# Adding member to a class and error message if they are already part of it
<img src="/planning_and_dev/error.png" width="400" >


# Adding multiple people to the same gym class
<img src="/planning_and_dev/add_multiple.png" width="400" >

# Gym Stats
<img src="/planning_and_dev/gym_stats1.png" width="400" >


## Project Description

### Gym

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

#### MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

#### Possible Extensions

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
- The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings. 

## Rules

The project must be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg

It must **NOT** use:

* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it.
* Any pre-built CSS libraries, such as Bootstrap.
* Authentication. Assume that the user already has secure access to the app.

## Setup For Demo

To run a demo locally, in your terminal:

1. Clone the repository
```
git clone https://github.com/tomsdruvas/Gym_management_app
```
2. Go to project directory and cd into /src directory:
```
cd /path/to/project/src
```
3. Install dependencies:
```
pip install psycopg2 flask
```
4. Create database.
```
createdb gym_manager
```
5. Import tables to database
```
psql -d gym_manager -f db/gym_manager.sql
```
6. Populate database
```
python3 console.py
```
7. Run the flask application
```
flask run
```
or
```
python3 -m flask run
```
8. You should see something like this:

```
Serving Flask app 'app.py' (lazy loading)
Environment: development
Debug mode: on
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
```

9. Go to http://127.0.0.1:5000/ or whichever port the 
app is running on in your local machine.

10. Have fun!
