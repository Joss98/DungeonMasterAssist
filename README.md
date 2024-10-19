# Dungeon Master Assist

A command-line tool for Dungeon Masters to handle dice rolling and common DM tasks in Dungeons and Dragons 5e.

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/joss98/DungeonMasterAssist.git
    ```

2. Navigate to the project directory
    ```bash
    cd DungeonMasterAssist
    ```

3. Create and activate a virtual environment
    ```bash
    python -m venv venv

    source venv/bin/activate
    ```

4. Install the package in editable mode
    ```bash
    pip install --editable .
    ```

## Usage

Use the ```dma``` command followed by the desired sub-command.

### Roll Dice
```bash
dma roll 2d6+3
```

#### Example output
```bash
Rolling 2d6+3: [1, 6] +3 (total: 10)
```

### Help

To see all available commands and options:
```bash
dma --help
```