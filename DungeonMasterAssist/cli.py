import click
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import shlex

from DungeonMasterAssist import dice_logic, data_manager, player_manager

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

class DmaCompleter(Completer):
    """Custom completer for DungeonMasterAssist interactive mode."""
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        commands = ['roll', 'help', 'exit', 'quit']
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