import secrets
import re

# Standard D&D dice variants (e.g., d4, d8, ...)
STANDARD_DICE = [4, 6, 8, 10, 12, 20, 100]

def parse_dice_notation(dice_notation):
    """
    Parses D&D dice notation (e.g., '2d6+3') and returns the number of dice, number of sides, and modifier.

    Args:
        dice_notation (str): the dice notation string.

    Returns:
        tuple: (num_dice, num_sides, modifier)

    Raises:
        ValueError: If the dice notation is invalid.
    """
    pattern = r'^(\d+)d(\d+)([+-]\d+)?$'
    match = re.fullmatch(pattern, dice_notation.strip())
    if not match:
        raise ValueError("Invalid dice notation. Format: NdM+X or NdM-X (e.g., 2d6+3).")
    
    num_dice = int(match.group(1))
    num_sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    if num_sides not in STANDARD_DICE:
        raise ValueError(f"Unsupported die variant: d{num_sides}. Supported variants are {', '.join(['d'+str(d) for d in STANDARD_DICE])}.")
    
    return num_dice, num_sides, modifier

def roll_dice(num_dice, num_sides):
    """
    Rolls a specified number of dice for a dice of a specified number of sides.

    Args:
        num_dice (int): Number of dice to roll.
        num_sides (int): Number of sides on each die.
    
    Returns:
        list: List of individual dice roll results.
    """
    return [secrets.randbelow(num_sides) + 1 for _ in range(num_dice)]