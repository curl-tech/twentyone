#!/bin/sh
#To Start MongoDB Server
sudo systemctl start mongod
#To Activate the Virtual Environment
source venv/bin/activate
#To Start the FastAPI server
python3 api.py
#Moving into the frontend directory
cd Frontend/pr21/
#Installing the required node dependencies for react
#npm i
#Starting the react server
#npm start