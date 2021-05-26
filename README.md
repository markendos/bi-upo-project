# bi_upo_project
Repository to host the Business Intelligence course project

## How to run?

### Docker

`docker build -t firsttag .`

`docker-compose up --build`

The build process should take about 30 s and the app is then available on: `localhost:8555`


### Without Docker

Requirements: 
- python2 or python3
- pip package manager

Steps: 
- Create the empty database called `bi_solutions`
- Import the data to the database with the command: `mysql -u <user> -p<password> bi_solutions < mysql-dump/dump.sql`
- Modify DBConnection.py connection parameters according to the local setup
- Install dependencies with the command: `pip install -r requirements.txt`
- Run the app with: `python src/main.py` (the app should be available on: 0.0.0.0:8080)

