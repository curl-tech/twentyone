#!/bin/sh

#The below function will be called in case Ctrl+C is pressed, i.e, Interrupt
terminationFunction () {
    trap INT                    #Restore signal handling to previous before exit.
    echo ''
    echo 'Exiting... MongoDB Server Being Closed...'    # Printing Message
    sudo systemctl stop mongod
    echo 'Exited.'
    exit                        #To exit the script
}

# Set up SIGINT trap to call terminationFunction.
trap "terminationFunction" INT

#To Start MongoDB Server
sudo systemctl start mongod

#To Activate the Virtual Environment
. venv/bin/activate

#To Start React - Frontend Server
/bin/sh -ec 'cd Frontend/pr21 && npm start &'

#To Start FastAPI - Backend Server
/bin/sh -ec 'python3 api.py'

# Restore signal handling to previous before exit.
trap INT