import unittest
from DungeonMasterAssist import dice_logic

class TestDiceLogic(unittest.TestCase):
    def test_parse_dice_notation_valid(self):
        test_cases = [
            ('1d4', (1, 4, 0)),
            ('2d6', (2, 6, 0)),
            ('3d8+2', (3, 8, 2)),
            ('4d10-1', (4, 10, -1)),
            ('5d12+5', (5, 12, 5)),
            ('6d20-3', (6, 20, -3)),
            ('7d100+10', (7, 100, 10)),
        ]
        for notation, expected in test_cases:
            with self.subTest(notation=notation):
                result = dice_logic.parse_dice_notation(notation)
                self.assertEqual(result, expected)
    
    def test_parse_dice_notation_invalid(self):
        invalid_notations = ['d6', '2d', '3d7', '4d20++2', '5d6-']
        for notation in invalid_notations:
            with self.subTest(notation=notation):
                with self.assertRaises(ValueError):
                    dice_logic.parse_dice_notation(notation)
    
    def test_roll_dice(self):
        num_dice = 3
        num_sides = 6
        results = dice_logic.roll_dice(num_dice, num_sides)
        self.assertEqual(len(results), num_dice)
        for roll in results:
            self.assertTrue(1 <= roll <= num_sides)

if __name__ == '__main__':
    unittest.main()