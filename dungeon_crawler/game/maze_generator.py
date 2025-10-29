"""Maze Generation using Recursive Backtracker Algorithm"""
import random
from .constants import TILE_SIZE


class MazeGenerator:
    """Generates maze obstacles for the game."""
    
    @staticmethod
    def generate_maze(screen_width, screen_height, player_start_x, player_start_y):
        """
        Generate a maze using recursive backtracker algorithm.
        
        Args:
            screen_width: Width of the play area in pixels
            screen_height: Height of the play area in pixels
            player_start_x: Player starting X position
            player_start_y: Player starting Y position
            
        Returns:
            List of (x, y) tuples representing wall positions
        """
        # Calculate maze dimensions
        max_cells_x = (screen_width - 2 * TILE_SIZE) // TILE_SIZE
        max_cells_y = (screen_height - 2 * TILE_SIZE) // TILE_SIZE

        # Maze cell dimensions (must be odd for proper maze generation)
        cols = max((max_cells_x - 1) // 2, 3)
        rows = max((max_cells_y - 1) // 2, 3)

        maze_w = cols * 2 + 1
        maze_h = rows * 2 + 1

        # Initialize maze grid (False = wall, True = passage)
        maze = [[False for _ in range(maze_w)] for _ in range(maze_h)]

        # Recursive backtracker maze generation
        start_x, start_y = 1, 1
        maze[start_y][start_x] = True
        stack = [(start_x, start_y)]
        
        while stack:
            x, y = stack[-1]
            neighbors = []
            
            # Check all 4 directions (2 cells away for proper maze structure)
            for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):
                nx, ny = x + dx, y + dy
                if 1 <= nx < maze_w - 1 and 1 <= ny < maze_h - 1 and not maze[ny][nx]:
                    neighbors.append((nx, ny))
            
            if neighbors:
                nx, ny = random.choice(neighbors)
                # Carve passage between current cell and chosen neighbor
                maze[ny][nx] = True
                maze[y + (ny - y) // 2][x + (nx - x) // 2] = True
                stack.append((nx, ny))
            else:
                stack.pop()

        # Convert maze grid to wall positions
        wall_positions = []
        offset_x = TILE_SIZE
        offset_y = TILE_SIZE
        
        for row in range(maze_h):
            for col in range(maze_w):
                if not maze[row][col]:
                    cx = offset_x + col * TILE_SIZE
                    cy = offset_y + row * TILE_SIZE
                    
                    # Skip if wall would overlap player start position
                    if abs(cx - player_start_x) < TILE_SIZE and \
                       abs(cy - player_start_y) < TILE_SIZE:
                        continue
                    
                    wall_positions.append((cx, cy))
        
        return wall_positions
