import click
from DungeonMasterAssist import dice_logic, data_manager, player_manager

@click.group()
def main():
    """Dungeon Master Assist CLI."""
    pass

@main.command()
@click.argument('dice_notation')
def roll(dice_notation):
    """Roll dice using D&D notation."""
    try:
        num_dice, num_sides, modifier = dice_logic.parse_dice_notation(dice_notation)
        results = dice_logic.roll_dice(num_dice, num_sides)
        total = sum(results) + modifier
        click.echo(f"Rolling {dice_notation}: {results} {'+' if modifier >= 0 else ''}{modifier} (total: {total})")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    main()