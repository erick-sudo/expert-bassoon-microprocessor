import unittest
from unittest.mock import patch
import io
from main import *

class Test(unittest.TestCase):
    # helper for testing a single operation
    def check_op(self, op, expected):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            process(op)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_noop(self):
        self.check_op('noop', '\n')
        self.check_op('noop 1 10', 'invalid operation noop 1 10\n')

    def test_add(self):
        self.check_op('add 4 8', '12\n')
        self.check_op('add -5 15', '10\n')
        self.check_op('add -5.3 15', 'invalid operation add -5.3 15\n')

    def test_mul(self):
        self.check_op('mul 2 13', '26\n')
        self.check_op('mul -1 50', '-50\n')
        self.check_op('mul -1', 'invalid operation mul -1\n')

    def test_gt(self):
        self.check_op('gt 2 13', '0\n')
        self.check_op('gt 10 5', '1\n')
        self.check_op('gt -2 -5', '1\n')
        self.check_op('gt 2 5 10', 'invalid operation gt 2 5 10\n')

    def test_or(self):
        self.check_op('or 0 0', '0\n')
        self.check_op('or 0 1', '1\n')
        self.check_op('or 1 0', '1\n')
        self.check_op('or 1 1', '1\n')
        self.check_op('or 10 -91', '1\n')
        self.check_op('or 2 5 10', 'invalid operation or 2 5 10\n')

    def test_nand(self):
        self.check_op('nand 0 0', '1\n')
        self.check_op('nand 0 1', '1\n')
        self.check_op('nand 1 0', '1\n')
        self.check_op('nand 1 1', '0\n')
        self.check_op('nand 10 -91', '0\n')
        self.check_op('nand 2 5 10', 'invalid operation nand 2 5 10\n')

    def test_min(self):
        self.check_op('min 1 3', '1\n')
        self.check_op('min 10 -9', '-9\n')
        self.check_op('min 3 4 2 5 9', '2\n')
        self.check_op('min 3.9 4', 'invalid operation min 3.9 4\n')

    def test_shift(self):
        self.check_op('shift 1 3', '8\n')
        self.check_op('shift 1 5', '32\n')
        self.check_op('shift 23 12', '94208\n')
        self.check_op('shift 0 5', 'invalid operation shift 0 5\n')

    def test_invalid(self):
        self.check_op('min 1 3', '1\n')
        self.check_op('min 10 -9', '-9\n')

    def test_sample1(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample1.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['24', '30', '1','0', '']))

    def test_sample2(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample2.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['0', '', '0', '55', '1', '1', '0', '1', '0', '0',
                        '3582', '1', '-90', '26', '176160768', '0', '1', '69',
                        '0', '10240', '', '1', '']))

    def test_sample3(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            run('samples/sample3.txt')
            self.assertEqual(
                    mock_stdout.getvalue(), 
                    "\n".join(['0', '24', '36', 'invalid operation shift 0 40', 
                        '222', '1', '32', '1', '0', '1', '1', '215', '-70', 
                        'invalid operation shift -13 30', '0', '53', '1', '1', 
                        '0', '1288', '1', '19516331393024', '0', '292057776128', 
                        '1', '0', 'invalid operation shift -64 28', '109', '17',
                        '0', '']))

if __name__ == '__main__':
    unittest.main()