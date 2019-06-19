from unittest import TestCase

from convertbooleantostring.ConvertBooleanToString import ConvertBooleanToString


class TestConvertBooleanToString(TestCase):
    def setUp(self):
        self.convertBooleanToString = ConvertBooleanToString()

    def test_is_string(self):
        self.assertEqual("True", self.convertBooleanToString.convert_boolean_to_string(True))
