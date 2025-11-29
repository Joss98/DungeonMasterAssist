import click
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import shlex
import os

from DungeonMasterAssist import dice_logic
from DungeonMasterAssist.player_manager import PlayerManager, Player
from DungeonMasterAssist.data_manager import DataManager

# Initialize Managers
DATA_FILE = "players.json"
data_manager = DataManager(DATA_FILE)
player_manager = PlayerManager()

# Load data on startup
loaded_data = data_manager.load_data()
for p_data in loaded_data:
    try:
        player = Player.from_dict(p_data)
        player_manager.add_player(player)
    except Exception as e:
        click.echo(f"Warning: Failed to load player data: {e}")

def save_players():
    data = [p.to_dict() for p in player_manager.list_players()]
    data_manager.save_data(data)

@click.group()
def main():
    """Dungeon Master Assist CLI."""
    pass

@main.command()
@click.argument('dice_notation', required=False)
def roll(dice_notation):
    """Roll dice using D&D notation (e.g., 2d6+3)."""
    if dice_notation:
        try:
            num_dice, num_sides, modifier = dice_logic.parse_dice_notation(dice_notation)
            results = dice_logic.roll_dice(num_dice, num_sides)
            total = sum(results) + modifier
            click.echo(f"Rolling {dice_notation}: {results} {'+' if modifier >= 0 else ''}{modifier} (total: {total})")
        except ValueError as e:
            click.echo(f"Error: {str(e)}")
    else:
        click.echo("Please provide dice notation. Example: dma roll 2d6+3")

# Player Management Commands
@main.group()
def player():
    """Manage players."""
    pass

@player.command()
@click.option('--name', required=True, help='Player Name')
@click.option('--class', 'char_class', required=True, help='Character Class')
@click.option('--level', required=True, type=int, help='Level')
@click.option('--hp', required=True, type=int, help='Hit Points')
@click.option('--ac', required=True, type=int, help='Armor Class')
@click.option('--initiative', required=True, type=int, help='Initiative Modifier')
def add(name, char_class, level, hp, ac, initiative):
    """Add a new player."""
    try:
        new_player = Player(name, char_class, level, hp, ac, initiative)
        player_manager.add_player(new_player)
        save_players()
        click.echo(f"Player '{name}' added.")
    except ValueError as e:
        click.echo(f"Error: {e}")

@player.command()
def list():
    """List all players."""
    players = player_manager.list_players()
    if not players:
        click.echo("No players found.")
        return
    
    click.echo(f"{'Name':<15} {'Class':<10} {'Lvl':<5} {'HP':<5} {'AC':<5} {'Init':<5}")
    click.echo("-" * 50)
    for p in players:
        click.echo(f"{p.name:<15} {p.char_class:<10} {p.level:<5} {p.hp:<5} {p.ac:<5} {p.initiative:<5}")

@player.command()
@click.option('--name', required=True, help='Player Name to remove')
def remove(name):
    """Remove a player."""
    try:
        player_manager.remove_player(name)
        save_players()
        click.echo(f"Player '{name}' removed.")
    except ValueError as e:
        click.echo(f"Error: {e}")

@player.command()
@click.option('--name', required=True, help='Player Name to update')
@click.option('--class', 'char_class', help='New Character Class')
@click.option('--level', type=int, help='New Level')
@click.option('--hp', type=int, help='New Hit Points')
@click.option('--ac', type=int, help='New Armor Class')
@click.option('--initiative', type=int, help='New Initiative Modifier')
def update(name, char_class, level, hp, ac, initiative):
    """Update a player's stats."""
    updates = {}
    if char_class: updates['char_class'] = char_class
    if level is not None: updates['level'] = level
    if hp is not None: updates['hp'] = hp
    if ac is not None: updates['ac'] = ac
    if initiative is not None: updates['initiative'] = initiative
    
    if not updates:
        click.echo("No updates provided.")
        return

    try:
        player_manager.update_player(name, **updates)
        save_players()
        click.echo(f"Player '{name}' updated.")
    except ValueError as e:
        click.echo(f"Error: {e}")


class DmaCompleter(Completer):
    """Custom completer for DungeonMasterAssist interactive mode."""
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        commands = ['roll', 'help', 'exit', 'quit', 'player']
        # Basic completion for top-level commands
        # TODO: Improve nested command completion
        for cmd in commands:
            if cmd.startswith(text):
                yield Completion(cmd, start_position=-len(text))

@main.command()
def interactive():
    """Start interactive mode."""
    click.echo("Entering interactive mode. Type 'help' for available commands. Type 'exit' or 'quit' to leave.")

    session = PromptSession(
        completer=DmaCompleter(),
        history=InMemoryHistory(),
        auto_suggest=AutoSuggestFromHistory()
    )

    while True:
        try:
            user_input = session.prompt('dma> ')
            stripped_input = user_input.strip()

            if not stripped_input:
                continue
            if stripped_input.lower() in ['exit', 'quit']:
                break
            elif stripped_input.lower() == 'help':
                click.echo("""
Available Commands:
  roll <dice_notation>     Roll dice using D&D notation (e.g., 2d6+3).
  player                   Manage players (add, list, remove, update).
  help                     Show this help message.
  exit, quit               Exit interactive mode.
""")
                continue
            else:
                # Split input into arguments
                args = shlex.split(stripped_input)
                # Invoke main CLI with arguments
                try:
                    # Click expects a list of arguments, without the program name
                    main(args, standalone_mode=False)
                except SystemExit:
                    # Prevent Click from closing interactive mode
                    pass
        except KeyboardInterrupt:
            # Handle Ctrl+C
            click.echo("\nUse 'exit' or 'quit' to leave interactive mode.")
        except EOFError:
            # Handle Ctrl+D to exit
            break
        except Exception as e:
            click.echo(f"Error: {e}")
    click.echo("Exiting interactive mode.")

if __name__ == '__main__':
    main()