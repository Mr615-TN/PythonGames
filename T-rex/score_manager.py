import json

class ScoreManager:
    def __init__(self):
        self.scores = []
        self.load_scores()

    def load_scores(self):
        try:
            with open('scores.json', 'r') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = []

    def save_scores(self):
        with open('scores.json', 'w') as f:
            json.dump(self.scores, f)

    def add_score(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:10]  # Keep only top 10 scores
        self.save_scores()

    def get_top_scores(self):
        return self.scores[:10]

    def get_last_score(self):
        return self.scores[-1] if self.scores else 0