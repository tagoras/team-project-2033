# Infrastructure Reporting System - Team 32

This project was created by the members of Team 32 for the CSC2033 Group Project at Newcastle University.

## Requirements: 
- [Python](https://www.python.org/)
- [NodeJS](https://nodejs.org/en/download/)
- [Git](https://git-scm.com/)
- [Make](https://www.gnu.org/software/make/) (Included in git bash but necessary in Linux)

## Instructions:
For the application to work you need both react front-end and python back-end running simultaneously:

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
cd api/ && make.bat html
```

If this worked for you can skip setup instructions and go straight to starting both programs, otherwise keep reading:

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
make.bat html
```

### Starting on Windows
To start the React server run:

```bash
npm start # Starts on localhost:3000
```

In a second git-bash window:
While in the python virtual environment ([venv](https://docs.python.org/3/library/venv.html)):

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
cd api/ && make html
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

While in the python virtual environment ([venv](https://docs.python.org/3/library/venv.html)):
```bash
#Linux
python testing.py
#Windows
python testing.py
```
or

```bash
#Linux
python -m unittest testing.py
#Windows
python -m unittest testing.py
```

## Documentation

While in the python virtual environment ([venv](https://docs.python.org/3/library/venv.html)):

```bash
#Linux
cd api
Makefile html
#Windows
cd api
make.bat html
```

The Documentation will be in the form of a navigable website in the [/docs](./docs) the, start reading
from [here](./docs/html/index.html)
after you have generated it.

## Website Features

The homepage has a navbar which allows the user to select different pages to view.

