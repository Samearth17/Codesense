import datetime

# Voting_System class
class Voting_System:

    # voting_options instance variable
    def __init__(self, voting_options):
        self.voting_options = voting_options

    # Vote function
    def vote(self, user_id, option_id):
        if user_id not in self.voting_options.keys():
            self.voting_options[user_id] = option_id
            return True
        else:
            return False

    # get_all_votes function
    def get_all_votes(self):
        return self.voting_options