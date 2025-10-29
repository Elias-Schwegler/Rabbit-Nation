"""Highscore Management with Persistence"""
import json
import os


class HighscoreManager:
    """Manages highscores with file persistence."""
    
    def __init__(self, filename="highscores.json"):
        self.filename = filename
        self.highscores = []
        self.load()
    
    def load(self):
        """Load highscores from file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.highscores = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.highscores = [100, 80, 50, 30, 10]  # Default scores
        else:
            self.highscores = [100, 80, 50, 30, 10]  # Default scores
    
    def save(self):
        """Save highscores to file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.highscores, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save highscores: {e}")
    
    def add_score(self, score):
        """Add a new score and save."""
        if score > 0:
            self.highscores.append(score)
            self.highscores.sort(reverse=True)
            self.highscores = self.highscores[:10]  # Keep top 10
            self.save()
    
    def get_top_scores(self, n=10):
        """Get top N scores."""
        return self.highscores[:n]
    
    def is_high_score(self, score):
        """Check if score qualifies as a highscore."""
        return len(self.highscores) < 10 or score > min(self.highscores)
