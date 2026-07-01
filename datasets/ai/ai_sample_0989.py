import numpy as np

def predict_match_score(probabilities):
    p_serve_win = probabilities[0]
    p_opp_serve_win = probabilities[1]
    p_serve_game_win = probabilities[2]
    p_opp_serve_game_win = probabilities[3]

    expected_score_serve = p_serve_game_win * (4*p_serve_win + 3*p_opp_serve_win)
    expected_score_opp_serve = p_opp_serve_game_win*(4*p_opp_serve_win + 3*p_serve_win)

    total_expected_score = expected_score_serve + expected_score_opp_serve
    return total_expected_score

probabilities = np.random.random(4)
print(predict_match_score(probabilities))