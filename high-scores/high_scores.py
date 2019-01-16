class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.latest_score = scores[-1]
        self.personal_best_score = max(scores)
        self.top_scores = sorted(scores, reverse=True)[0:3]

    def scores(self):
        return self.scores

    def latest(self):
        return self.latest_score
    
    def personal_best(self):
        return self.personal_best_score
    
    def personal_top(self):
        return self.top_scores
    
    def report(self):
        if self.latest_score >= self.personal_best_score: message = "That's your personal best!"
        else: message = "That's {} short of your personal best!".format(self.personal_best_score - self.latest_score)
        return "Your latest score was {}. {}".format(self.latest_score, message)
