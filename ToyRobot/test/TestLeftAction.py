import unittest

from constant.Face import Face
from robot.action.impl.LeftAction import LeftAction


class TestLeftAction(unittest.TestCase):
    leftAction = LeftAction()

    def testAccept(self):
        state = {
            'x': 0,
            'y': 0,
            'f': Face.NORTH
        }
        self.leftAction.set_param([5, 5])
        self.leftAction.handle(state)
        self.assertEqual(state['f'], Face.WEST)


if __name__ == '__main__':
    unittest.main()