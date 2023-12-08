import unittest
from unittest.mock import mock_open, patch

from main import (read_file_lines,
                  ValidationType,
                  is_valid_passphrase,
                  is_last_char_valid_python,
                  is_all_valid_python,
                  is_last_char_valid_general,
                  is_all_valid_general)


class TestFileOperations(unittest.TestCase):

    def test_read_file_lines_file_exists_with_content(self):
        mock_data = "line1\nline2\nline3"
        mock_file = mock_open(read_data=mock_data)
        with patch("builtins.open", mock_file):
            result = read_file_lines("dummy_path")

        self.assertEqual(result, ["line1\n", "line2\n", "line3"])

    def test_read_file_lines_file_not_found(self):
        mock_file = mock_open()
        mock_file.side_effect = FileNotFoundError
        with patch("builtins.open", mock_file):
            with self.assertRaises(FileNotFoundError):
                read_file_lines("non_existent_path")

    def test_read_file_lines_empty_file(self):
        mock_file = mock_open(read_data="")
        with patch("builtins.open", mock_file):
            result = read_file_lines("empty_file_path")
        self.assertEqual(result, [])


class TestValidationTypes(unittest.TestCase):

    def test_validation_type_enum_contains_general_and_python(self):
        self.assertTrue(ValidationType.GENERAL in ValidationType)
        self.assertTrue(ValidationType.PYTHON in ValidationType)

    def test_validation_type_enum_values(self):
        self.assertEqual(ValidationType.GENERAL.value, 1)
        self.assertEqual(ValidationType.PYTHON.value, 2)


class TestGeneralFunctions(unittest.TestCase):

    def test_is_last_char_valid_general(self):
        self.assertTrue(is_last_char_valid_general("test!"))
        self.assertTrue(is_last_char_valid_general("example?"))
        self.assertTrue(is_last_char_valid_general("example."))
        self.assertFalse(is_last_char_valid_general("fail"))

    def test_is_all_valid_general(self):
        self.assertTrue(is_all_valid_general("all lowercase."))
        self.assertFalse(is_all_valid_general("UpperCase!"))
        self.assertFalse(is_all_valid_general("mixed Case."))

    def test_check_occurrences_general(self):
        self.assertTrue(is_valid_passphrase("alma korte!", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("szilva.", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("citrom lime", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("korte korte?", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("dinnye ananasz fuge", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("Alma Korte!", ValidationType.GENERAL))
        self.assertFalse(is_valid_passphrase("repeat repeat", ValidationType.GENERAL))


class TestPythonFunctions(unittest.TestCase):

    def test_is_last_char_valid_python(self):
        self.assertTrue(is_last_char_valid_python("test!"))
        self.assertTrue(is_last_char_valid_python("example?"))
        self.assertTrue(is_last_char_valid_python("example."))
        self.assertFalse(is_last_char_valid_python("fail"))

    def test_is_all_valid_python(self):
        self.assertTrue(is_all_valid_python("all lowercase."))
        self.assertFalse(is_all_valid_python("UpperCase!"))
        self.assertFalse(is_all_valid_python("mixed Case."))

    def test_check_occurrences_python(self):
        self.assertTrue(is_valid_passphrase("alma korte!", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("szilva.", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("citrom lime", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("korte korte?", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("dinnye ananasz fuge", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("Alma Korte!", ValidationType.PYTHON))
        self.assertFalse(is_valid_passphrase("repeat repeat", ValidationType.PYTHON))


if __name__ == '__main__':
    unittest.main()
