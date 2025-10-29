"""
Dungeon Crawler Game - Main Entry Point
Modular version with clean code organization
"""
import arcade
import random
import math

from game.constants import *
from game.sprites import PlayerSprite, EnemySprite
from game.maze_generator import MazeGenerator
from game.highscore import HighscoreManager
from game.menu import MenuRenderer


class DungeonCrawler(arcade.Window):
    """Main game window with modular design."""
    
    def __init__(self):
        # Start with default map size
        self.current_map_size = DEFAULT_MAP_SIZE
        map_width, map_height = MAP_SIZES[self.current_map_size]
        
        super().__init__(map_width, map_height, SCREEN_TITLE, resizable=True)
        
        # Game state
        self.current_state = STATE_MENU
        
        # Game objects
        self.player_sprite = None
        self.player_list = None
        self.walls = None
        self.coins = None
        self.enemies = None
        self.enemy_physics_engines = []
        
        # Game stats
        self.score = 0
        self.player_health = PLAYER_HEALTH
        self.physics_engine = None
        self.attack_cooldown_timer = 0
        
        # Track key states for 8-directional movement
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        
        # Highscores with persistence
        self.highscore_manager = HighscoreManager()
        
        # Menu renderer
        self.menu_renderer = MenuRenderer()
        
        arcade.set_background_color(arcade.color.DARK_GRAY)
    
    def setup(self):
        """Set up the game. Call this function to start/restart the game."""
        # Get current map dimensions
        map_width, map_height = MAP_SIZES[self.current_map_size]
        
        # Resize window if needed
        if self.width != map_width or self.height != map_height:
            self.set_size(map_width, map_height)
        
        # Reset game state
        self.score = 0
        self.player_health = PLAYER_HEALTH
        self.attack_cooldown_timer = 0
        self.current_state = STATE_PLAYING
        
        # Create player
        self.player_sprite = PlayerSprite(
            ":resources:images/animated_characters/female_person/femalePerson",
            scale=0.4
        )
        self.player_sprite.center_x = TILE_SIZE + TILE_SIZE // 2
        self.player_sprite.center_y = TILE_SIZE + TILE_SIZE // 2
        
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        
        # Create border walls
        self.walls = arcade.SpriteList()
        self._create_border_walls(map_width, map_height)
        
        # Generate maze obstacles
        wall_positions = MazeGenerator.generate_maze(
            map_width, map_height,
            self.player_sprite.center_x,
            self.player_sprite.center_y
        )
        
        for wx, wy in wall_positions:
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", scale=TILE_SIZE / 128)
            wall.center_x = wx
            wall.center_y = wy
            self.walls.append(wall)
        
        # Create coins
        self.coins = arcade.SpriteList()
        num_coins = 10 + (len(MAP_SIZES) - list(MAP_SIZES.keys()).index(self.current_map_size)) * 5
        for _ in range(num_coins):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.5)
            
            placed = False
            attempts = 0
            while not placed and attempts < 200:
                coin.center_x = TILE_SIZE + random.random() * (map_width - 2 * TILE_SIZE)
                coin.center_y = TILE_SIZE + random.random() * (map_height - 2 * TILE_SIZE)
                
                hit_wall = arcade.check_for_collision_with_list(coin, self.walls)
                too_close_to_player = math.hypot(
                    coin.center_x - self.player_sprite.center_x,
                    coin.center_y - self.player_sprite.center_y
                ) < TILE_SIZE * 3
                
                if not hit_wall and not too_close_to_player:
                    placed = True
                attempts += 1
            
            if placed:
                self.coins.append(coin)
        
        # Create enemies
        self.enemies = arcade.SpriteList()
        self.enemy_physics_engines = []
        
        num_enemies = 3 + (len(MAP_SIZES) - list(MAP_SIZES.keys()).index(self.current_map_size)) * 2
        for _ in range(num_enemies):
            enemy = EnemySprite(":resources:images/animated_characters/zombie/zombie", scale=0.4)
            
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                enemy.center_x = TILE_SIZE + random.randint(1, (map_width - 2 * TILE_SIZE) // TILE_SIZE - 1) * TILE_SIZE
                enemy.center_y = TILE_SIZE + random.randint(1, (map_height - 2 * TILE_SIZE) // TILE_SIZE - 1) * TILE_SIZE
                
                hit_wall = arcade.check_for_collision_with_list(enemy, self.walls)
                too_close_to_player = math.hypot(
                    enemy.center_x - self.player_sprite.center_x,
                    enemy.center_y - self.player_sprite.center_y
                ) < TILE_SIZE * 5
                
                if not hit_wall and not too_close_to_player:
                    placed = True
                attempts += 1
            
            if placed:
                enemy.health = ENEMY_HEALTH
                self.enemies.append(enemy)
                enemy_physics = arcade.PhysicsEngineSimple(enemy, self.walls)
                self.enemy_physics_engines.append(enemy_physics)
        
        # Set up physics engine for player
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.walls)
    
    def _create_border_walls(self, map_width, map_height):
        """Create border walls around the play area."""
        # Top and bottom walls
        for x in range(0, map_width + TILE_SIZE, TILE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", scale=TILE_SIZE / 128)
            wall.center_x = x
            wall.center_y = 0
            self.walls.append(wall)
            
            wall2 = arcade.Sprite(":resources:images/tiles/grassCenter.png", scale=TILE_SIZE / 128)
            wall2.center_x = x
            wall2.center_y = map_height
            self.walls.append(wall2)
        
        # Left and right walls
        for y in range(TILE_SIZE, map_height, TILE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", scale=TILE_SIZE / 128)
            wall.center_x = 0
            wall.center_y = y
            self.walls.append(wall)
            
            wall2 = arcade.Sprite(":resources:images/tiles/grassCenter.png", scale=TILE_SIZE / 128)
            wall2.center_x = map_width
            wall2.center_y = y
            self.walls.append(wall2)
    
    def on_draw(self):
        """Render the screen."""
        self.clear()
        
        if self.current_state == STATE_MENU:
            self.menu_renderer.draw_main_menu()
        elif self.current_state == STATE_MAP_SIZE:
            self.menu_renderer.draw_map_size_menu(self.current_map_size)
        elif self.current_state == STATE_SETTINGS:
            self.menu_renderer.draw_settings()
        elif self.current_state == STATE_HIGHSCORE:
            self.menu_renderer.draw_highscores(self.highscore_manager.get_top_scores())
        elif self.current_state == STATE_PLAYING:
            self._draw_game()
        elif self.current_state == STATE_PAUSED:
            self._draw_game()
            self.menu_renderer.draw_pause_overlay()
        elif self.current_state == STATE_GAME_OVER:
            self._draw_game()
            is_high_score = self.highscore_manager.is_high_score(self.score)
            self.menu_renderer.draw_game_over(self.player_health, self.score, is_high_score)
    
    def _draw_game(self):
        """Draw the game screen."""
        if self.walls:
            self.walls.draw()
        if self.coins:
            self.coins.draw()
        if self.enemies:
            self.enemies.draw()
        if self.player_list:
            self.player_list.draw()
        
        # Draw HUD
        arcade.draw_text(
            f"Score: {self.score}",
            10, self.height - 30,
            arcade.color.WHITE,
            24,
            bold=True
        )
        
        # Draw health with color coding
        health_color = arcade.color.GREEN
        if self.player_health < 50:
            health_color = arcade.color.ORANGE
        if self.player_health < 25:
            health_color = arcade.color.RED
        
        arcade.draw_text(
            f"Health: {int(self.player_health)}",
            10, self.height - 60,
            health_color,
            20,
            bold=True
        )
        
        # Draw attack cooldown indicator
        if self.attack_cooldown_timer > 0:
            arcade.draw_text(
                "Cooldown...",
                10, self.height - 90,
                arcade.color.YELLOW,
                16
            )
        
        # Draw enemy health bars
        for enemy in self.enemies:
            if hasattr(enemy, 'health'):
                bar_width = 40
                bar_height = 5
                health_percentage = enemy.health / ENEMY_HEALTH
                
                left = enemy.center_x - bar_width / 2
                right = enemy.center_x + bar_width / 2
                bottom = enemy.center_y + 40 - bar_height / 2
                top = enemy.center_y + 40 + bar_height / 2
                
                # Background (red)
                arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.RED)
                # Health (green)
                right = left + bar_width * health_percentage
                arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.GREEN)
    
    def on_key_press(self, key, modifiers):
        """Handle key presses for menus, movement, and combat."""
        if self.current_state == STATE_MENU:
            if key == arcade.key.ENTER:
                self.setup()
            elif key == arcade.key.M:
                self.current_state = STATE_MAP_SIZE
            elif key == arcade.key.S:
                self.current_state = STATE_SETTINGS
            elif key == arcade.key.H:
                self.current_state = STATE_HIGHSCORE
            elif key == arcade.key.ESCAPE:
                arcade.exit()
        
        elif self.current_state == STATE_MAP_SIZE:
            if key == arcade.key.KEY_1:
                self.current_map_size = 'small'
            elif key == arcade.key.KEY_2:
                self.current_map_size = 'medium'
            elif key == arcade.key.KEY_3:
                self.current_map_size = 'large'
            elif key == arcade.key.KEY_4:
                self.current_map_size = 'huge'
            elif key == arcade.key.ESCAPE:
                self.current_state = STATE_MENU
        
        elif self.current_state in (STATE_SETTINGS, STATE_HIGHSCORE):
            if key == arcade.key.ESCAPE:
                self.current_state = STATE_MENU
        
        elif self.current_state == STATE_PLAYING:
            if key in (arcade.key.P, arcade.key.ESCAPE):
                self.current_state = STATE_PAUSED
            elif key == arcade.key.SPACE:
                self._attack()
            elif key in (arcade.key.UP, arcade.key.W):
                self.up_pressed = True
            elif key in (arcade.key.DOWN, arcade.key.S):
                self.down_pressed = True
            elif key in (arcade.key.LEFT, arcade.key.A):
                self.left_pressed = True
            elif key in (arcade.key.RIGHT, arcade.key.D):
                self.right_pressed = True
            
            self._update_player_speed()
        
        elif self.current_state == STATE_PAUSED:
            if key in (arcade.key.P, arcade.key.ESCAPE):
                self.current_state = STATE_PLAYING
            elif key == arcade.key.Q:
                # Save score before quitting
                self.highscore_manager.add_score(self.score)
                self.current_state = STATE_MENU
        
        elif self.current_state == STATE_GAME_OVER:
            if key == arcade.key.ENTER:
                self.setup()
            elif key == arcade.key.ESCAPE:
                self.current_state = STATE_MENU
    
    def _attack(self):
        """Player attacks nearby enemies."""
        if self.attack_cooldown_timer > 0:
            return
        
        self.attack_cooldown_timer = ATTACK_COOLDOWN
        
        attack_range = TILE_SIZE * 1.5
        enemies_to_remove = []
        
        for enemy in self.enemies:
            distance = math.hypot(
                self.player_sprite.center_x - enemy.center_x,
                self.player_sprite.center_y - enemy.center_y
            )
            
            if distance < attack_range:
                enemy.health -= ATTACK_DAMAGE
                if enemy.health <= 0:
                    enemies_to_remove.append(enemy)
                    self.score += 50
        
        for enemy in enemies_to_remove:
            enemy.remove_from_sprite_lists()
            if enemy in self.enemies:
                idx = list(self.enemies).index(enemy)
                if idx < len(self.enemy_physics_engines):
                    self.enemy_physics_engines.pop(idx)
    
    def on_key_release(self, key, modifiers):
        """Handle key releases."""
        if self.current_state != STATE_PLAYING:
            return
        
        if key in (arcade.key.UP, arcade.key.W):
            self.up_pressed = False
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = False
        elif key in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False
        
        self._update_player_speed()
    
    def _update_player_speed(self):
        """Update player velocity with normalized diagonal speed."""
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        
        if self.up_pressed:
            self.player_sprite.change_y += PLAYER_SPEED
        if self.down_pressed:
            self.player_sprite.change_y -= PLAYER_SPEED
        if self.left_pressed:
            self.player_sprite.change_x -= PLAYER_SPEED
        if self.right_pressed:
            self.player_sprite.change_x += PLAYER_SPEED
        
        # Normalize diagonal movement
        if self.player_sprite.change_x != 0 and self.player_sprite.change_y != 0:
            magnitude = math.sqrt(
                self.player_sprite.change_x ** 2 + 
                self.player_sprite.change_y ** 2
            )
            self.player_sprite.change_x = (self.player_sprite.change_x / magnitude) * PLAYER_SPEED
            self.player_sprite.change_y = (self.player_sprite.change_y / magnitude) * PLAYER_SPEED
    
    def on_update(self, delta_time):
        """Movement and game logic."""
        if self.current_state != STATE_PLAYING:
            return
        
        # Update attack cooldown
        if self.attack_cooldown_timer > 0:
            self.attack_cooldown_timer -= delta_time
        
        # Update physics
        if self.physics_engine:
            self.physics_engine.update()
        
        # Update animations
        if self.player_list:
            self.player_list.update_animation(delta_time)
        if self.enemies:
            self.enemies.update_animation(delta_time)
        
        # Update coins
        if self.coins:
            self.coins.update()
        
        # Enemy AI: chase player
        for i, enemy in enumerate(self.enemies):
            dx = self.player_sprite.center_x - enemy.center_x
            dy = self.player_sprite.center_y - enemy.center_y
            distance = math.hypot(dx, dy)
            
            if distance > 0:
                enemy.change_x = (dx / distance) * ENEMY_SPEED
                enemy.change_y = (dy / distance) * ENEMY_SPEED
            
            if i < len(self.enemy_physics_engines):
                self.enemy_physics_engines[i].update()
        
        self.enemies.update()
        
        # Coin collection
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coins)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10
        
        # Enemy collision damage
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemies)
        if enemy_hit_list:
            self.player_health -= 5 * delta_time * len(enemy_hit_list)
            
            if self.player_health <= 0:
                self.player_health = 0
                self._game_over()
        
        # Win condition
        if len(self.coins) == 0:
            self._game_over(won=True)
    
    def _game_over(self, won=False):
        """Handle game over state."""
        self.highscore_manager.add_score(self.score)
        self.current_state = STATE_GAME_OVER


def main():
    """Main function"""
    window = DungeonCrawler()
    arcade.run()


if __name__ == "__main__":
    main()
