### Tiango
A Quiz Web App using Python Flask, Jinja2 and HTML/CSS. 
It has 6 sections:
  * C++
  * Java
  * Python
  * MySQL
  * JavaScript
  * Aptitude
  
Solve quiz and move up the leaderboard!

### Run Application
- Download zip file or clone this repository onto your local machine.
- Open `app.py` file and change the database path to `Database/Tiango.sqlite` wherever needed.
- Open terminal and run `app.py`
- Open your browser and run the web app at localhost at port 5000.

## Folders
### 1. Database:
    This folder consists of:
    - createDB.py : which defines the schema of all the tables in database.
    - run.py : defines queries to insert data into tables.
    - Tiango.sqlite : Sqlite database to store all the Quiz data
    
### 2. static:
    This folder consists of:
      - css : To define styles for web pages.
      - images : Contains all images for web page.
      
### 3. templates:
    This folder has several html files which define the layout of the web page.
    
### 4. app.py:
    This python file defines the core logic of the application.
  
