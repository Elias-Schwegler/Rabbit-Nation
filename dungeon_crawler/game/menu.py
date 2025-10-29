"""Menu Rendering Functions"""
import arcade
from .constants import (
    STATE_MENU, STATE_SETTINGS, STATE_HIGHSCORE, STATE_PAUSED, STATE_GAME_OVER, STATE_MAP_SIZE,
    SCREEN_WIDTH, SCREEN_HEIGHT, MAP_SIZES
)


class MenuRenderer:
    """Handles all menu rendering."""
    
    @staticmethod
    def draw_main_menu():
        """Draw the main menu."""
        arcade.draw_text(
            "DUNGEON CRAWLER",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
            arcade.color.WHITE,
            54,
            anchor_x="center",
            bold=True
        )
        
        arcade.draw_text(
            "Press ENTER to Start",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
            arcade.color.WHITE,
            32,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press M for Map Size",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press S for Settings",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press H for Highscores",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press ESC to Quit",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
    
    @staticmethod
    def draw_map_size_menu(current_size):
        """Draw the map size selection menu."""
        arcade.draw_text(
            "SELECT MAP SIZE",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 180,
            arcade.color.WHITE,
            44,
            anchor_x="center",
            bold=True
        )
        
        y_start = SCREEN_HEIGHT / 2 + 80
        for i, (name, (width, height)) in enumerate(MAP_SIZES.items()):
            color = arcade.color.GOLD if name == current_size else arcade.color.WHITE
            key_num = i + 1
            arcade.draw_text(
                f"{key_num}. {name.upper()}: {width}x{height}px",
                SCREEN_WIDTH / 2, y_start - i * 50,
                color,
                28 if name == current_size else 24,
                anchor_x="center",
                bold=name == current_size
            )
        
        arcade.draw_text(
            f"Current: {current_size.upper()}",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,
            arcade.color.LIGHT_GRAY,
            20,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press 1-4 to select, ESC to return",
            SCREEN_WIDTH / 2, 50,
            arcade.color.LIGHT_GRAY,
            18,
            anchor_x="center"
        )
    
    @staticmethod
    def draw_settings():
        """Draw the settings screen."""
        arcade.draw_text(
            "CONTROLS",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 180,
            arcade.color.WHITE,
            44,
            anchor_x="center",
            bold=True
        )
        
        controls = [
            "Movement: Arrow Keys or WASD",
            "Attack: SPACE (damages nearby enemies)",
            "Pause: P or ESC",
            "",
            "OBJECTIVE:",
            "Collect all coins while avoiding/defeating zombies!",
            "Your health is shown in the top-left corner.",
        ]
        
        y_start = SCREEN_HEIGHT / 2 + 100
        for i, text in enumerate(controls):
            arcade.draw_text(
                text,
                SCREEN_WIDTH / 2, y_start - i * 40,
                arcade.color.WHITE if text else arcade.color.DARK_GRAY,
                20 if not text.endswith(":") else 24,
                anchor_x="center",
                bold=text.endswith(":")
            )
        
        arcade.draw_text(
            "Press ESC to return to menu",
            SCREEN_WIDTH / 2, 50,
            arcade.color.LIGHT_GRAY,
            18,
            anchor_x="center"
        )
    
    @staticmethod
    def draw_highscores(highscores):
        """Draw the highscore screen."""
        arcade.draw_text(
            "HIGH SCORES",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 180,
            arcade.color.WHITE,
            44,
            anchor_x="center",
            bold=True
        )
        
        y_start = SCREEN_HEIGHT / 2 + 100
        for i, score in enumerate(highscores[:10]):
            arcade.draw_text(
                f"{i + 1}. {score}",
                SCREEN_WIDTH / 2, y_start - i * 40,
                arcade.color.GOLD if i == 0 else arcade.color.WHITE,
                28 if i == 0 else 24,
                anchor_x="center",
                bold=i < 3
            )
        
        arcade.draw_text(
            "Press ESC to return to menu",
            SCREEN_WIDTH / 2, 50,
            arcade.color.LIGHT_GRAY,
            18,
            anchor_x="center"
        )
    
    @staticmethod
    def draw_pause_overlay():
        """Draw pause menu overlay."""
        # Semi-transparent overlay
        arcade.draw_lrbt_rectangle_filled(
            0, SCREEN_WIDTH, 0, SCREEN_HEIGHT,
            (0, 0, 0, 180)
        )
        
        arcade.draw_text(
            "PAUSED",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 80,
            arcade.color.WHITE,
            54,
            anchor_x="center",
            bold=True
        )
        
        arcade.draw_text(
            "Press P or ESC to Resume",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press Q to Quit to Menu",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
    
    @staticmethod
    def draw_game_over(player_health, score, is_high_score):
        """Draw game over screen."""
        # Semi-transparent overlay
        arcade.draw_lrbt_rectangle_filled(
            0, SCREEN_WIDTH, 0, SCREEN_HEIGHT,
            (0, 0, 0, 200)
        )
        
        game_over_text = "YOU DIED!" if player_health <= 0 else "YOU WIN!"
        text_color = arcade.color.RED if player_health <= 0 else arcade.color.GOLD
        
        arcade.draw_text(
            game_over_text,
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
            text_color,
            54,
            anchor_x="center",
            bold=True
        )
        
        arcade.draw_text(
            f"Final Score: {score}",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30,
            arcade.color.WHITE,
            32,
            anchor_x="center"
        )
        
        # Check if it's a new highscore
        if is_high_score:
            arcade.draw_text(
                "NEW HIGH SCORE!",
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20,
                arcade.color.GOLD,
                28,
                anchor_x="center",
                bold=True
            )
        
        arcade.draw_text(
            "Press ENTER to Play Again",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
        
        arcade.draw_text(
            "Press ESC to Return to Menu",
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )
