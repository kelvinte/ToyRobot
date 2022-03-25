import unittest
from unittest.mock import patch
from  core.impl.StdinUserInputProcessor import StdinUserInputProcessor
import sys
from io import StringIO


class TestStdinUserInputProcessor(unittest.TestCase):
    stdInUserInputProcessor = StdinUserInputProcessor()

    def test_get_input(self):
        stdin = sys.stdin
        sys.stdin = StringIO('MOVE\nRIGHT')
        inp = self.stdInUserInputProcessor.get_input()
        self.assertEqual(inp, ['MOVE','RIGHT'])


if __name__ == '__main__':
    unittest.main()