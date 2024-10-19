# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

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

---

### Example of Using the CLI in Version 1.0.0

```bash
# Rolling a d20:
dma roll 1d20

# Rolling a 3d6+2:
dma roll 3d6+2
```

---

### Instructions for Setting Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/joss98/DungeonMasterAssist.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd DungeonMasterAssist
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install the package in editable mode:**
   ```bash
   pip install --editable .
   ```

5. **Use the CLI for rolling dice:**
   ```bash
   dma roll 1d20
    ```
---

### Summary of Features for Version 1.0.0

- **Dice Rolling**: Allows users to roll all D&D dice types using standard notation.
- **Modifier Support**: Rolls can include modifiers to adjust the final result.
- **Error Handling**: Proper validation and error messages for incorrect inputs.
- **Initial Unit Tests**: Basic test cases included for core functionality.

---

### What to Keep in Mind for Future Versions

- **Future Features**: New features such as player management, shortcut support, and automated DM tasks (e.g., stealth checks) will be added in future updates.
- **Bug Fixes**: Any discovered issues or bugs will be addressed in subsequent patch releases.

---

## Notes

This is the first stable release of DungeonMasterAssist, a simple command-line tool for DMs to manage dice rolls efficiently during Dungeons & Dragons sessions.

---