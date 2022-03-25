import unittest

from constant.Face import Face
from robot.action.impl.PlaceAction import PlaceAction


class TestPlaceAction(unittest.TestCase):
    action = PlaceAction()

    def testPlace(self):
        state = {
            'x': 1,
            'y': 1,
            'f': Face.NORTH
        }
        self.action.set_param([5,5, 1, 1, 'WEST'])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.WEST)
        self.assertEqual(state['x'], 1)
        self.assertEqual(state['y'], 1)

    def testPlaceExceedBorder(self):
        state = {
            'x': 0,
            'y': 0,
            'f': Face.NORTH
        }
        self.action.set_param([5,5, 6, 6, 'WEST'])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.NORTH)
        self.assertEqual(state['x'], 0)
        self.assertEqual(state['y'], 0)

if __name__ == '__main__':
    unittest.main()