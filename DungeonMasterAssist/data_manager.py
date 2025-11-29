import json
import os
from typing import List, Dict, Any

class DataManager:
    def __init__(self, file_path: str = "players.json"):
        self.file_path = file_path

    def save_data(self, data: List[Dict[str, Any]]):
        """Saves a list of dictionaries to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self) -> List[Dict[str, Any]]:
        """Loads a list of dictionaries from the JSON file."""
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []