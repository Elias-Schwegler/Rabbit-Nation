# Dungeon Crawler Game

A Python arcade game with 8-directional movement, maze generation, and combat system.

## Features

- **8-Directional Movement**: Move with Arrow Keys or WASD
- **Combat System**: Attack enemies with SPACE bar
- **Procedural Maze Generation**: Each game has a unique maze layout
- **Configurable Map Sizes**: Choose from Small, Medium, Large, or Huge maps
- **Persistent Highscores**: Scores are saved between sessions
- **Menu System**: Start, Settings, Highscores, Pause, and Game Over screens
- **Animated Sprites**: Player and enemies have walking animations

## Installation

```bash
pip install arcade
```

## Running the Game

```bash
python main.py
```

Or use the legacy monolithic version:
```bash
python g2.py
```

## Project Structure

```
dungeon_crawler/
├── main.py                 # Main game entry point (modular version)
├── g2.py                   # Legacy monolithic version
├── highscores.json         # Saved highscores
├── game/                   # Game modules
│   ├── __init__.py
│   ├── constants.py        # Game constants and configuration
│   ├── sprites.py          # Player and Enemy sprite classes
│   ├── maze_generator.py  # Procedural maze generation
│   ├── highscore.py        # Highscore management with persistence
│   └── menu.py             # Menu rendering functions
└── README.md               # This file
```

## Controls

### Movement
- **Arrow Keys** or **WASD**: Move in 8 directions
- Diagonal movement is automatically normalized

### Combat
- **SPACE**: Attack nearby enemies (1.5 tile range)
- **Cooldown**: 0.5 seconds between attacks

### Menu Navigation
- **ENTER**: Start game / Play again
- **M**: Map size selection
- **S**: Settings/Controls
- **H**: Highscores
- **P** or **ESC**: Pause game
- **Q**: Quit to menu (from pause screen)
- **ESC**: Exit game (from main menu)

## Map Sizes

Choose your challenge level in the Map Size menu:

1. **Small**: 800x600px (Default) - Good for quick games
2. **Medium**: 1200x900px - Balanced gameplay
3. **Large**: 1600x1200px - Extended exploration
4. **Huge**: 2000x1500px - Epic adventures

Larger maps have:
- More coins to collect
- More enemies to fight
- Bigger, more complex mazes

## Gameplay Tips

1. **Health Management**: Your health decreases when touching enemies. Keep moving!
2. **Attack Range**: Get close to enemies and press SPACE to damage them
3. **Score Points**: 
   - +10 points per coin collected
   - +50 points per enemy defeated
4. **Win Condition**: Collect all coins to win
5. **Lose Condition**: Health reaches 0

## Highscores

- Highscores are automatically saved to `highscores.json`
- Top 10 scores are maintained
- Scores are saved even if you quit mid-game
- View highscores from the main menu

## Code Architecture

The modular version (`main.py`) separates concerns into focused modules:

- **constants.py**: Central configuration and game constants
- **sprites.py**: Sprite classes with animation logic
- **maze_generator.py**: Recursive backtracker maze algorithm
- **highscore.py**: JSON-based score persistence
- **menu.py**: All menu rendering in one place
- **main.py**: Game loop and state management

This makes the code:
- Easier to maintain
- Easier to test
- Easier to extend with new features

## Development

To add new features:

1. **New game constants**: Add to `game/constants.py`
2. **New sprite types**: Extend classes in `game/sprites.py`
3. **New menus**: Add rendering methods to `game/menu.py`
4. **New map generation**: Modify `game/maze_generator.py`
5. **New game logic**: Update `main.py`

## License

Educational project - feel free to modify and extend!
