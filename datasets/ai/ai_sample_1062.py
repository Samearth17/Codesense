class HighScores:
    
    def __init__(self, num_scores):
        self.scores = [0] * num_scores
        self.curr_index = 0 # stores index of last score filled 
        self.num_scores = num_scores
        
    def add_score(self, score):
        if self.curr_index < self.num_scores:
            self.scores[self.curr_index] = score
            self.curr_index += 1
        else:
            # update the minimum score in the list
            min_score_index = 0
            for i in range(1, self.num_scores):
                if self.scores[i] < self.scores[i-1]:
                    min_score_index = i
            if self.scores[min_score_index] < score:
                self.scores[min_score_index] = score
    
    def get_scores(self):
        return self.scores