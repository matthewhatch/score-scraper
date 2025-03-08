import unittest
from unittest.mock import patch, MagicMock
from classes.game import Game
from classes.team import Team

class TestGame(unittest.TestCase):
    
    @patch('classes.game.get_connection')
    @patch('classes.game.close_connection')
    def test_save_new_game(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        
        game = Game(1, 1, 2, 'Team 1', 'Team 2', 'Network 1', 'Mon, 01 Jan 2021 00:00:00 +0000')
        game.exists = MagicMock(return_value=False)
        
        game.save()
        
        mock_cursor.execute.assert_called()
        mock_conn.commit.assert_called()
        mock_close_connection.assert_called_with(mock_conn, mock_cursor)

    @patch('classes.game.get_connection')
    @patch('classes.game.close_connection')
    def test_update_existing_game(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        
        game = Game(1, 1, 2, 'Team 1', 'Team 2', 'Network 1', 'Mon, 01 Jan 2021 00:00:00 +0000')
        game.exists = MagicMock(return_value=True)
        
        game.save()
        
        mock_cursor.execute.assert_called()
        mock_conn.commit.assert_called()
        mock_close_connection.assert_called_with(mock_conn, mock_cursor)

    @patch('classes.game.get_connection')
    @patch('classes.game.close_connection')
    def test_exists(self, mock_close_connection, mock_get_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cursor)
        mock_cursor.fetchone.return_value = True
        
        game = Game(1, 1, 2, 'Team 1', 'Team 2', 'Network 1', 'Mon, 01 Jan 2021 00:00:00 +0000')
        
        result = game.exists()
        
        self.assertTrue(result)
        mock_cursor.execute.assert_called()
        mock_close_connection.assert_called_with(mock_conn, mock_cursor)

    def test_str(self):
        team = MagicMock()
        team.__str__.return_value = "Team 1"
        with patch('classes.team.Team.find', return_value=team):
            game = Game(1, 1, 2, 'Sharks', 'Bears', 'ESPN', 'Mon, 01 Jan 2021 00:00:00 +0000','1','1','final','Final')
        self.assertEqual(str(game), 'Final ESPN - 1 Bears at 1 Sharks')
if __name__ == '__main__':
    unittest.main()
#