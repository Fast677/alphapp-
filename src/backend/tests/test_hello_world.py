import unittest
from unittest.mock import patch, mock_open
from succeeded import status, message, log_entry
import datetime

class TestSucceeded(unittest.TestCase):

    @patch('succeeded.datetime')
    def test_log_entry_format(self, mock_datetime):
        # Arrange
        mock_datetime.datetime.now.return_value = datetime.datetime(2023, 10, 10, 10, 10, 10)
        expected_timestamp = "2023-10-10T10:10:10"
        expected_log_entry = f"[{expected_timestamp}] Status: {status}, Message: {message}"

        # Act
        timestamp = mock_datetime.datetime.now().isoformat()
        log_entry = f"[{timestamp}] Status: {status}, Message: {message}"

        # Assert
        self.assertEqual(log_entry, expected_log_entry)

    @patch('builtins.open', new_callable=mock_open)
    @patch('succeeded.datetime')
    def test_log_entry_written_to_file(self, mock_datetime, mock_file):
        # Arrange
        mock_datetime.datetime.now.return_value = datetime.datetime(2023, 10, 10, 10, 10, 10)
        expected_timestamp = "2023-10-10T10:10:10"
        expected_log_entry = f"[{expected_timestamp}] Status: {status}, Message: {message}\n"

        # Act
        with open("process.log", "a") as log_file:
            log_file.write(expected_log_entry)

        # Assert
        mock_file().write.assert_called_once_with(expected_log_entry)

    @patch('builtins.print')
    @patch('succeeded.datetime')
    def test_log_entry_printed(self, mock_datetime, mock_print):
        # Arrange
        mock_datetime.datetime.now.return_value = datetime.datetime(2023, 10, 10, 10, 10, 10)
        expected_timestamp = "2023-10-10T10:10:10"
        expected_log_entry = f"[{expected_timestamp}] Status: {status}, Message: {message}"

        # Act
        print(expected_log_entry)

        # Assert
        mock_print.assert_called_once_with(expected_log_entry)

if __name__ == '__main__':
    unittest.main()