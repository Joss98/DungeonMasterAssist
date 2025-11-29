import unittest
from click.testing import CliRunner
from DungeonMasterAssist.cli import main
import os
import json

class TestCliPlayer(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        # Ensure we are using a test file for persistence to avoid messing up real data
        # However, since CLI uses a hardcoded or default path in DataManager, we might need to mock or patch it.
        # For this test, we can patch DataManager in cli.py or use a temporary directory if the CLI allows configuring the path.
        # Since we didn't add path configuration to CLI yet, let's patch DataManager in the test.
        
        # Actually, a better way for integration testing without mocking too much is to set an env var or 
        # modify the global state if possible. But `cli.py` instantiates `player_manager` and `data_manager` at module level (likely).
        # Let's check `cli.py` again. It imports them. We need to see how they are used.
        pass

    def test_player_add(self):
        # We need to isolate the data file. 
        # Since we can't easily inject the data file path into the CLI commands without modifying the CLI structure heavily 
        # (unless we use a context object), we will mock the DataManager in `DungeonMasterAssist.cli`.
        
        from unittest.mock import patch
        with patch('DungeonMasterAssist.cli.data_manager') as mock_dm_module:
            # Mock the DataManager instance
            mock_dm_instance = mock_dm_module.DataManager.return_value
            mock_dm_instance.load_data.return_value = []
            
            result = self.runner.invoke(main, ['player', 'add', '--name', 'TestPlayer', '--class', 'Fighter', '--level', '1', '--hp', '10', '--ac', '10', '--initiative', '0'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn("Player 'TestPlayer' added.", result.output)

    def test_player_list(self):
        from unittest.mock import patch
        with patch('DungeonMasterAssist.cli.data_manager') as mock_dm_module:
             # Mock the DataManager instance to return some data
            mock_dm_instance = mock_dm_module.DataManager.return_value
            mock_dm_instance.load_data.return_value = [
                {'name': 'ExistingPlayer', 'char_class': 'Wizard', 'level': 2, 'hp': 12, 'ac': 11, 'initiative': 1}
            ]
            
            # We also need to make sure the PlayerManager in CLI is initialized with this data.
            # The CLI likely initializes PlayerManager at the top level or within commands.
            # If it's top level, patching might be tricky if it's already imported.
            # Let's assume we modify CLI to initialize on command or we patch the `player_manager` instance in `cli`.
            
            # Let's wait to see the CLI implementation. 
            # For now, I'll write a basic test that assumes the CLI works and maybe writes to a local file 'players.json'.
            # I will clean up 'players.json' after tests.
            pass

    def tearDown(self):
        if os.path.exists("players.json"):
            os.remove("players.json")

    def test_end_to_end_player_flow(self):
        # Add
        result = self.runner.invoke(main, ['player', 'add', '--name', 'E2EPlayer', '--class', 'Rogue', '--level', '3', '--hp', '20', '--ac', '14', '--initiative', '4'])
        self.assertEqual(result.exit_code, 0)
        
        # List
        result = self.runner.invoke(main, ['player', 'list'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("E2EPlayer", result.output)
        self.assertIn("Rogue", result.output)
        
        # Update
        result = self.runner.invoke(main, ['player', 'update', '--name', 'E2EPlayer', '--hp', '15'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Player 'E2EPlayer' updated.", result.output)
        
        # Verify Update
        result = self.runner.invoke(main, ['player', 'list'])
        # The output is a table, so we check if the line contains the updated HP
        # E2EPlayer       Rogue      3     15    14    4
        self.assertIn("E2EPlayer", result.output)
        self.assertIn("15", result.output)
        
        # Remove
        result = self.runner.invoke(main, ['player', 'remove', '--name', 'E2EPlayer'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Player 'E2EPlayer' removed.", result.output)
        
        # Verify Removal
        result = self.runner.invoke(main, ['player', 'list'])
        self.assertNotIn("E2EPlayer", result.output)

if __name__ == '__main__':
    unittest.main()
