import unittest
import os
import json
import tempfile
from DungeonMasterAssist.data_manager import DataManager
from DungeonMasterAssist.player_manager import Player

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False).name
        self.dm = DataManager(file_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_data(self):
        players = [
            Player(name="Aragorn", char_class="Ranger", level=5, hp=45, ac=16, initiative=3),
            Player(name="Legolas", char_class="Ranger", level=5, hp=40, ac=15, initiative=5)
        ]
        
        # Convert players to dict for saving (simulating what PlayerManager might pass or DataManager handles)
        # Assuming DataManager handles list of Player objects or dicts. Let's assume it handles list of dicts for simplicity in this test, 
        # or we test the integration. 
        # Better: DataManager should probably handle serialization of Player objects if we want it to be robust, 
        # or PlayerManager converts to dict. Let's assume PlayerManager converts to dicts for storage.
        
        data_to_save = [p.to_dict() for p in players]
        self.dm.save_data(data_to_save)

        loaded_data = self.dm.load_data()
        self.assertEqual(len(loaded_data), 2)
        self.assertEqual(loaded_data[0]['name'], "Aragorn")
        self.assertEqual(loaded_data[1]['name'], "Legolas")

    def test_load_nonexistent_file(self):
        # If file doesn't exist, should return empty list or handle gracefully
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
        data = self.dm.load_data()
        self.assertEqual(data, [])

    def test_save_empty_data(self):
        self.dm.save_data([])
        loaded_data = self.dm.load_data()
        self.assertEqual(loaded_data, [])

if __name__ == '__main__':
    unittest.main()
