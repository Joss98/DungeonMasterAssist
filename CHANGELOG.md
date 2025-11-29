# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2025-11-29

### Added
- **Player Management**: Added commands to manage player characters (`add`, `list`, `update`, `remove`).
- **Data Persistence**: Player data is now persisted in a `players.json` file.
- **CLI Integration**: Integrated player management commands into the main CLI and interactive mode.

## [1.1.0] - 2024-11-23

### Added
- **Interactive Mode**: Introduced an interactive CLI mode (`dma interactive`) that allows users to enter commands in a REPL-like environment.
  - **Command Completion**: Implemented auto-completion for available commands within interactive mode.
  - **History Support**: Users can navigate through their command history using the up/down arrow keys.
  - **Help Command**: Added a `help` command within interactive mode to display available commands and usage information.
- **Custom Completer**: Added a custom completer to enhance user experience in interactive mode.

### Fixed
- **Error Handling**: Improved error messages and exception handling within interactive mode.
- **Keyboard Interrupts**: Handled `KeyboardInterrupt` and `EOFError` exceptions to prevent crashes during unexpected exits.

## [1.0.2] - 2024-10-19

### Fixed
- Corrected typographical error in CHANGELOG file.

## [1.0.1] - 2024-10-19

### Fixed
- Corrected typographical errors and pointed to CHANGELOG file in the README file.

## [1.0.0] - 2024-10-19

### Added
- **Core functionality**: Initial release of the DungeonMasterAssist MVP, including basic CLI functionality.
- **Dice rolling command**: Support for rolling standard Dungeons and Dragons dice (d4, d6, d8, d10, d12, d20, d100) using standard dice notation (e.g., `1d20`, `2d6+3`).
- **Modifier support**: Dice rolls can include modifiers (e.g., `1d20+5` or `3d6-1`).
- **Error handling**: Provides meaningful error messages for invalid dice notation.
- **Roll results display**: Outputs individual dice results and the total sum.
- **Basic test suite**: Unit tests for core dice rolling functionality.
- **Initial project setup**: Project structure established, with `setup.py` for packaging and a virtual environment setup for local development.