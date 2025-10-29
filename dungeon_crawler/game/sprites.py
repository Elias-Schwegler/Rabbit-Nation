"""Sprite Classes for Player and Enemies"""
import arcade
import math
from .constants import (
    RIGHT_FACING, LEFT_FACING, DIRECTION_IDLE, DIRECTION_RIGHT, DIRECTION_LEFT,
    DIRECTION_UP, DIRECTION_DOWN, DIRECTION_UP_RIGHT, DIRECTION_UP_LEFT,
    DIRECTION_DOWN_RIGHT, DIRECTION_DOWN_LEFT, UPDATES_PER_FRAME
)


def load_texture_pair(filename):
    """
    Load a texture pair. In newer arcade versions, we'd flip the second texture.
    For compatibility, we load the same texture twice and handle direction via sprite rotation.
    """
    texture = arcade.load_texture(filename)
    return [texture, texture]


class PlayerSprite(arcade.Sprite):
    """
    Custom player sprite with 8-directional animation support.
    
    Animation structure:
    - 2 idle frames (left and right facing)
    - 16 walking frames (8 directions × 2 frames each)
    Total: 18 frames
    """
    
    def __init__(self, character_path=":resources:images/animated_characters/female_person/femalePerson", scale=0.4):
        super().__init__(scale=scale)
        
        # Track which direction the character is facing
        self.character_face_direction = RIGHT_FACING
        
        # Current texture index for animation
        self.cur_texture = 0
        
        # Track current movement direction
        self.current_direction = DIRECTION_IDLE
        
        # Load textures for idle standing (2 frames: left and right)
        self.idle_texture_pair = load_texture_pair(f"{character_path}_idle.png")
        
        # Load textures for walking (8 frames × 2 for left/right = 16 frames)
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{character_path}_walk{i}.png")
            self.walk_textures.append(texture)
        
        # Set the initial texture
        self.texture = self.idle_texture_pair[0]
    
    def update_animation(self, delta_time: float = 1/60):
        """Update animation based on movement direction."""
        # Idle state
        if self.change_x == 0 and self.change_y == 0:
            self.current_direction = DIRECTION_IDLE
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return
        
        # Calculate angle of movement for 8-directional detection
        angle = math.atan2(self.change_y, self.change_x)
        angle_degrees = math.degrees(angle)
        
        # Normalize angle to 0-360 range
        if angle_degrees < 0:
            angle_degrees += 360
        
        # Determine direction based on angle (8 directions)
        if 337.5 <= angle_degrees or angle_degrees < 22.5:
            self.current_direction = DIRECTION_RIGHT
            self.character_face_direction = RIGHT_FACING
        elif 22.5 <= angle_degrees < 67.5:
            self.current_direction = DIRECTION_UP_RIGHT
            self.character_face_direction = RIGHT_FACING
        elif 67.5 <= angle_degrees < 112.5:
            self.current_direction = DIRECTION_UP
        elif 112.5 <= angle_degrees < 157.5:
            self.current_direction = DIRECTION_UP_LEFT
            self.character_face_direction = LEFT_FACING
        elif 157.5 <= angle_degrees < 202.5:
            self.current_direction = DIRECTION_LEFT
            self.character_face_direction = LEFT_FACING
        elif 202.5 <= angle_degrees < 247.5:
            self.current_direction = DIRECTION_DOWN_LEFT
            self.character_face_direction = LEFT_FACING
        elif 247.5 <= angle_degrees < 292.5:
            self.current_direction = DIRECTION_DOWN
        elif 292.5 <= angle_degrees < 337.5:
            self.current_direction = DIRECTION_DOWN_RIGHT
            self.character_face_direction = RIGHT_FACING
        
        # Walking animation - cycle through frames
        self.cur_texture += 1
        if self.cur_texture >= len(self.walk_textures) * UPDATES_PER_FRAME:
            self.cur_texture = 0
        
        frame = self.cur_texture // UPDATES_PER_FRAME
        self.texture = self.walk_textures[frame][self.character_face_direction]


class EnemySprite(arcade.Sprite):
    """Animated enemy sprite (zombie)."""
    
    def __init__(self, character_path=":resources:images/animated_characters/zombie/zombie", scale=0.4):
        super().__init__(scale=scale)
        
        self.character_face_direction = RIGHT_FACING
        self.cur_texture = 0
        self.health = 50  # Will be set properly in game logic
        
        # Load idle texture
        self.idle_texture_pair = load_texture_pair(f"{character_path}_idle.png")
        
        # Load walking textures
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{character_path}_walk{i}.png")
            self.walk_textures.append(texture)
        
        # Set initial texture
        self.texture = self.idle_texture_pair[0]
    
    def update_animation(self, delta_time: float = 1/60):
        """Update enemy animation."""
        # Determine facing direction
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
        
        # Idle or moving?
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return
        
        # Walking animation
        self.cur_texture += 1
        if self.cur_texture >= len(self.walk_textures) * UPDATES_PER_FRAME:
            self.cur_texture = 0
        
        frame = self.cur_texture // UPDATES_PER_FRAME
        self.texture = self.walk_textures[frame][self.character_face_direction]
