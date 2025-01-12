import unittest
from unittest.mock import patch, mock_open
import datetime

class TestSucceeded(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('datetime.datetime')
    def test_log_entry(self, mock_datetime, mock_file):
        # Configurar la marca de tiempo fija
        mock_datetime.now.return_value = datetime.datetime(2023, 1, 1, 12, 0, 0)
        mock_datetime.now().isoformat.return_value = "2023-01-01T12:00:00"

        # Importar el módulo a probar
        import succeeded

        # Verificar la entrada del registro
        expected_log_entry = "[2023-01-01T12:00:00] Status: succeeded, Message: The process completed successfully."
        mock_file().write.assert_called_once_with(expected_log_entry + "\n")

        # Verificar la salida en consola
        with patch('builtins.print') as mock_print:
            succeeded.main()
            mock_print.assert_called_once_with(expected_log_entry)

if __name__ == '__main__':
    unittest.main()