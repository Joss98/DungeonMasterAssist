import unittest
from DungeonMasterAssist.player_manager import PlayerManager, Player

class TestPlayerManager(unittest.TestCase):
    def setUp(self):
        self.pm = PlayerManager()

    def test_add_player(self):
        player = Player(name="Aragorn", char_class="Ranger", level=5, hp=45, ac=16, initiative=3)
        self.pm.add_player(player)
        self.assertEqual(len(self.pm.players), 1)
        self.assertEqual(self.pm.get_player("Aragorn"), player)

    def test_add_duplicate_player(self):
        player = Player(name="Aragorn", char_class="Ranger", level=5, hp=45, ac=16, initiative=3)
        self.pm.add_player(player)
        with self.assertRaises(ValueError):
            self.pm.add_player(player)

    def test_remove_player(self):
        player = Player(name="Legolas", char_class="Ranger", level=5, hp=40, ac=15, initiative=5)
        self.pm.add_player(player)
        self.pm.remove_player("Legolas")
        self.assertEqual(len(self.pm.players), 0)

    def test_remove_nonexistent_player(self):
        with self.assertRaises(ValueError):
            self.pm.remove_player("Gimli")

    def test_update_player(self):
        player = Player(name="Gimli", char_class="Fighter", level=5, hp=50, ac=17, initiative=2)
        self.pm.add_player(player)
        self.pm.update_player("Gimli", hp=45, level=6)
        updated_player = self.pm.get_player("Gimli")
        self.assertEqual(updated_player.hp, 45)
        self.assertEqual(updated_player.level, 6)
        self.assertEqual(updated_player.ac, 17) # Should remain unchanged

    def test_update_nonexistent_player(self):
        with self.assertRaises(ValueError):
            self.pm.update_player("Frodo", hp=10)

    def test_list_players(self):
        p1 = Player(name="Aragorn", char_class="Ranger", level=5, hp=45, ac=16, initiative=3)
        p2 = Player(name="Legolas", char_class="Ranger", level=5, hp=40, ac=15, initiative=5)
        self.pm.add_player(p1)
        self.pm.add_player(p2)
        players = self.pm.list_players()
        self.assertEqual(len(players), 2)
        self.assertIn(p1, players)
        self.assertIn(p2, players)

if __name__ == '__main__':
    unittest.main()
