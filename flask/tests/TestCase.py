import os
import unittest
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TestCase(unittest.TestCase):
    def test_db(self):
        bind = db.metadata.bind
        assert bind == None


if __name__ == '__main__':
    unittest.main()
