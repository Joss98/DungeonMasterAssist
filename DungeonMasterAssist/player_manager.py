from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class Player:
    name: str
    char_class: str
    level: int
    hp: int
    ac: int
    initiative: int

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class PlayerManager:
    def __init__(self):
        self.players: List[Player] = []

    def add_player(self, player: Player):
        if any(p.name == player.name for p in self.players):
            raise ValueError(f"Player with name '{player.name}' already exists.")
        self.players.append(player)

    def remove_player(self, name: str):
        player = self.get_player(name)
        if player:
            self.players.remove(player)
        else:
            raise ValueError(f"Player with name '{name}' not found.")

    def get_player(self, name: str) -> Optional[Player]:
        for player in self.players:
            if player.name == name:
                return player
        return None

    def update_player(self, name: str, **kwargs):
        player = self.get_player(name)
        if not player:
            raise ValueError(f"Player with name '{name}' not found.")
        
        for key, value in kwargs.items():
            if hasattr(player, key):
                setattr(player, key, value)
            else:
                raise AttributeError(f"Player has no attribute '{key}'")

    def list_players(self) -> List[Player]:
        return self.players