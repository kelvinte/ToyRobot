import unittest

from constant.Face import Face
from robot.action.impl.MoveAction import MoveAction


class TestMoveAction(unittest.TestCase):
    action = MoveAction()

    def testMoveLeft(self):
        state = {
            'x': 1,
            'y': 1,
            'f': Face.WEST
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.WEST)
        self.assertEqual(state['x'], 0)
        self.assertEqual(state['y'], 1)


    def testMoveRight(self):
        state = {
            'x': 1,
            'y': 1,
            'f': Face.EAST
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.EAST)
        self.assertEqual(state['x'], 2)
        self.assertEqual(state['y'], 1)

    def testMoveUp(self):
        state = {
            'x': 1,
            'y': 1,
            'f': Face.NORTH
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.NORTH)
        self.assertEqual(state['x'], 1)
        self.assertEqual(state['y'], 2)

    def testMoveDown(self):
        state = {
            'x': 1,
            'y': 1,
            'f': Face.SOUTH
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.SOUTH)
        self.assertEqual(state['x'], 1)
        self.assertEqual(state['y'], 0)


    def testWillNotExceedYAxis(self):
        state = {
            'x': 1,
            'y': 4,
            'f': Face.NORTH
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.NORTH)
        self.assertEqual(state['x'], 1)
        self.assertEqual(state['y'], 4)
        state = {
            'x': 1,
            'y': 0,
            'f': Face.SOUTH
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.SOUTH)
        self.assertEqual(state['x'], 1)
        self.assertEqual(state['y'], 0)

    def testWillNotExceedXAxis(self):
        state = {
            'x': 4,
            'y': 1,
            'f': Face.EAST
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.EAST)
        self.assertEqual(state['x'], 4)
        self.assertEqual(state['y'], 1)

        state = {
            'x': 0,
            'y': 1,
            'f': Face.WEST
        }
        self.action.set_param([5, 5])
        self.action.accept(state)
        self.assertEqual(state['f'], Face.WEST)
        self.assertEqual(state['x'], 0)
        self.assertEqual(state['y'], 1)


if __name__ == '__main__':
    unittest.main()