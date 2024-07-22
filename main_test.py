import unittest
from db import db


class TestDb(unittest.TestCase):
    def test_one_p_two(self):
        self.assertEqual(db.check_path(), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
