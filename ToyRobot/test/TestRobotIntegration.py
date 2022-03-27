import asyncio
import unittest

from constant.Face import Face
from robot.ToyRobot import ToyRobot


class TestRobotIntegration(unittest.TestCase):
    broadcaster = None
    robot = ToyRobot(broadcaster)


    def testStart(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.robot.processV2("PLACE 1,1,NORTH"))
        state = self.robot.get_state()
        self.assertEqual(1, state['x'])
        self.assertEqual(1, state['y'])
        self.assertEqual(Face.NORTH, state['f'])

        loop.run_until_complete(self.robot.processV2("MOVE"))
        state = self.robot.get_state()
        self.assertEqual(1, state['x'])
        self.assertEqual(2, state['y'])
        self.assertEqual(Face.NORTH, state['f'])


        loop.run_until_complete(self.robot.processV2("LEFT"))
        state = self.robot.get_state()
        self.assertEqual(1, state['x'])
        self.assertEqual(2, state['y'])
        self.assertEqual(Face.WEST, state['f'])



if __name__ == '__main__':
    unittest.main()