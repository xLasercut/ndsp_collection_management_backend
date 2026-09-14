# NDSP Collection Management Backend Test

## Pre-requisites
- Python 3.13 or higher
- poetry
- docker


## Setup Instructions
1. Clone the repository
2. If using asdf or mise-en-place, run the install command
3. Install the dependencies using poetry:
   ```bash
   poetry install
   ```
4. Set up the database using Docker:
   ```bash
   docker-compose up
   ```
5. Create test data 
   ```bash
   poetry run python main.py
   ```
   

Then run the two sql files against the mysql database