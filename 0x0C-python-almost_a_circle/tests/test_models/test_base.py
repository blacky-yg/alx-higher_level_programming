#!/usr/bin/python3
"""Unittests for the models classes"""
import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """Tests for the initialisation of the class"""

    def test_empty_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_none_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_arg(self):
        self.assertEqual(15, Base(15).id)

    def test_nb_objects(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_set_id(self):
        b = Base(15)
        b.id = 12
        self.assertEqual(12, b.id)

    def test_id_nb_objects(self):
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_objects)

    def test_bad_nb_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
