# Dungeon Master Assist

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A command-line tool for Dungeon Masters to handle dice rolling and common DM tasks in Dungeons and Dragons 5e.

## Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Roll Dice](#roll-dice)
  - [Interactive Mode](#interactive-mode)
  - [Help](#help)
- [Features](#features)
- [Roadmap](#roadmap)
- [License](#license)
- [Support](#support)
- [Changelog](#changelog)

## Prerequisites

- Python 3.6 or higher
- `pip` package manager

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/joss98/DungeonMasterAssist.git
    ```

2. Navigate to the project directory:
    ```bash
    cd DungeonMasterAssist
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    ```
    - On Unix or MacOS:
    ```bash
    source venv/bin/activate
    ```
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```

4. Install the package in editable mode:
    ```bash
    pip install --editable .
    ```

## Usage

### Roll Dice

Use standard D&D dice notation NdS+M, where:
- N is the number of dice
- S is the number of sides per die
- M is an optional modifier

Example:
```bash
dma roll 2d6+3
```

Example output:
```bash
Rolling 2d6+3: [1, 6] +3 (total: 10)
```

### Interactive Mode

Start the interactive mode to execute commands in a REPL-like environment.

```bash
dma interactive
```

Example usage:
```bash
dma> roll 1d20+5
Rolling 1d20+5: [15] +5 (total: 20)

dma> help
Available Commands:
  roll <dice_notation>     Roll dice using D&D notation (e.g., 2d6+3).
  help                     Show this help message.
  exit, quit               Exit interactive mode.

dma> exit
Exiting interactive mode.
```

### Help

To see all available commands and options:
```bash
dma --help
```

## Features

- Interactive Mode: A REPL-like environment for executing commands efficiently.
- Dice Rolling: Support for rolling standard D&D dice using standard notation.
- Auto-Completion: Command auto-completion in interactive mode.
- Session History: Navigate through command history using arrow keys.
- Robust Error Handling: Graceful handling of exceptions and user interruptions.

## Roadmap

- Player Management: Features for tracking player stats and information.
- Shortcut Support: Implementing shortcuts for commonly used commands.
- Automated DM Tasks: Tools for automating tasks like stealth checks.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Support

If you have any questions or run into issues, please open an [issue](https://github.com/joss98/DungeonMasterAssist/issues) on GitHub.

## Changelog

You can view the [full changelog here](./CHANGELOG.md).