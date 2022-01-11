# Infrastructure Reporting System - Team 32

This project was created by the members of Team 32 for the CSC2033 Group Project at Newcastle University.

## Requirements: 
- [Python](https://www.python.org/)
- [NodeJS](https://nodejs.org/en/download/)
- [Git](https://git-scm.com/)

## Instructions:
For the application to work you need both react front-end and python back-end running simultaniously:

### Windows: 

In a Git Bash terminal:

Clone the project:
```bash
git clone https://github.com/tagoras/team-project-2033
cd team-project-2033
```

Front-end setup :
```bash
npm install
npm update
```
To start the React server run:
```bash
npm start # Starts on localhost:3000
```
In a second git-bash window:

Back-end setup : 
```bash
cd api/
python -m venv venv
source venv/bin/Scripts/activate
pip install -r requirements.txt
```
Start python: 
```bash
python
```
then:
```python
>>> from models import init_db
>>> init_db()
>>> exit()
```
To start the Back-end server:
```bash
python app.py # Starts on localhost:5000
```
Press `Ctrl+C` (in the terminal) to stop any server.

### Mac/Linux:

Open terminal:

Clone the project:
```bash
git clone https://github.com/tagoras/team-project-2033 && cd team-project-2033
```

Front-end setup :
```bash
npm install && npm update
```
To start the React server run:
```bash
npm start # Starts on localhost:3000
```
In a second terminal:   

Back-end setup : 
```bash
cd api/ && python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Start python: 
```bash
python
```
then:
```python
>>> from models import init_db
>>> init_db()
>>> exit()
```
To start the Back-end server:
```bash
python app.py # Starts on localhost:5000
```

## Testing

To start the testing suite:

```bash
python testing.py
```
or
```bash
python -m unittest testing.py
```



## Website Features

The homepage has a navbar which allows the user to select different pages to view.

