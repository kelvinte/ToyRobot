There are 2 modules here
1. ToyRobot
2. ToyRobot-html

ToyRobot is a python application that serves the main functionality.

To Run the python application please install the ff dependencies
1. pip install websockets

Then to run the application go to ToyRobot folder then
python main.py

or 

py main.py

If you want to run the GUI go to ToyRobot-html folder
execute this command
python -m http.server 9000
or 
py -m http.server 9000

Then open your browser to localhost:9000


Try entering the ff:
PLACE 1,1,NORTH
REPORT
MOVE
REPORT
MOVE
REPORT
MOVE
REPORT
STOP to exit


To Run Tests:
python -m unittest discover test
