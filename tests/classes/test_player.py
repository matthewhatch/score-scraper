import unittest
from unittest.mock import patch, MagicMock
from classes.player import Player
from classes.team import Team

class TestPlayer(unittest.TestCase):

    @patch('classes.player.get_connection')
    @patch('classes.player.close_connection')
    def test_save_new_player(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        
        player = Player(1, 'John', 'Doe', 1, 10)
        player.exists = MagicMock(return_value=False)
        
        player.save()
        
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_close_connection.assert_called_once_with(mock_conn, mock_cursor)

    @patch('classes.player.get_connection')
    @patch('classes.player.close_connection')
    def test_update_existing_player(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        
        player = Player(1, 'John', 'Doe', 1, 10)
        player.exists = MagicMock(return_value=True)
        
        player.save()
        
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_close_connection.assert_called_once_with(mock_conn, mock_cursor)

    @patch('classes.player.get_connection')
    @patch('classes.player.close_connection')
    def test_exists(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        mock_cursor.fetchone.return_value = True
        
        player = Player(1, 'John', 'Doe', 1, 10)
        
        result = player.exists()
        
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once()
        mock_close_connection.assert_called_once_with(mock_conn, mock_cursor)

    def test_str(self):
        team = MagicMock()
        team.__str__.return_value = "Team 1"
        with patch('classes.team.Team.find', return_value=team):
            player = Player(1, 'John', 'Doe', 1, 10)
            self.assertEqual(str(player), '1 10 - John Doe - 1')

if __name__ == '__main__':
    unittest.main()