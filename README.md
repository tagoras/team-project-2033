# Infrastructure Reporting System - Team 32

This project was created by the members of Team 32 for the CSC2033 Group Project at Newcastle University.

## Requirements: 
- [Python](https://www.python.org/)
- [NodeJS](https://nodejs.org/en/download/)
- [Git](https://git-scm.com/)
- [Make](https://www.gnu.org/software/make/) (Included in git bash but necessary in Linux)

## Instructions:
For the application to work you need both react front-end and python back-end running simultaniously:

### Windows:

In a Git Bash terminal:

Clone the project:

```bash
git clone https://github.com/tagoras/team-project-2033
cd team-project-2033
```

Try:

```bash
make
```

If this worked for you can skip setup instructions and go straight to starting both programs, otherwise continue

Front-end setup :

```bash
npm install
npm update
```

Back-end setup :

```bash
cd api/
python -m venv venv
source venv/bin/Scripts/activate
pip install -r requirements.txt
python __init__.py
```


To start the React server run:

```bash
npm start # Starts on localhost:3000
```

In a second git-bash window:

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

Setup:
```bash
make
```
To start the React server run:
```bash
npm start # Starts on localhost:3000
```

In another terminal window:

To start the Back-end server:
```bash
python app.py # Starts on localhost:5000
```

## Testing

To start the testing suite:

```bash
#Linux
api/venv/bin/python3 testing.py
#Windows
api/venv/Scripts/python.exe testing.py
```
or

```bash
#Linux
api/venv/bin/python3 -m unittest testing.py
#Windows
api/venv/Lib/python.exe -m unittest testing.py
```



## Website Features

The homepage has a navbar which allows the user to select different pages to view.

