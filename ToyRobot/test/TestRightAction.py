import unittest

from constant.Face import Face
from robot.action.impl.RightAction import RightAction


class TestLeftAction(unittest.TestCase):
    rightAction = RightAction()

    def testAccept(self):
        state = {
            'x': 0,
            'y': 0,
            'f': Face.NORTH
        }
        self.rightAction.set_param([5, 5])
        self.rightAction.accept(state)
        self.assertEqual(state['f'], Face.EAST)


if __name__ == '__main__':
    unittest.main()