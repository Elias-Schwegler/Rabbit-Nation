"""Game Constants and Configuration"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dungeon Crawler"
TILE_SIZE = 64

# Gameplay constants
PLAYER_SPEED = 5
ENEMY_SPEED = 2
PLAYER_HEALTH = 100
ENEMY_HEALTH = 50
ATTACK_DAMAGE = 25
ATTACK_COOLDOWN = 0.5  # seconds
UPDATES_PER_FRAME = 7  # How many updates before we advance a frame

# Game States
STATE_MENU = 0
STATE_SETTINGS = 1
STATE_HIGHSCORE = 2
STATE_PLAYING = 3
STATE_PAUSED = 4
STATE_GAME_OVER = 5
STATE_MAP_SIZE = 6

# Direction constants for 8-way movement
RIGHT_FACING = 0
LEFT_FACING = 1

DIRECTION_IDLE = 0
DIRECTION_RIGHT = 1
DIRECTION_LEFT = 2
DIRECTION_UP = 3
DIRECTION_DOWN = 4
DIRECTION_UP_RIGHT = 5
DIRECTION_UP_LEFT = 6
DIRECTION_DOWN_RIGHT = 7
DIRECTION_DOWN_LEFT = 8

# Map size presets (width, height in tiles)
MAP_SIZES = {
    'small': (800, 600),
    'medium': (1200, 900),
    'large': (1600, 1200),
    'huge': (2000, 1500)
}

DEFAULT_MAP_SIZE = 'small'
