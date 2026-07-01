from nltk import word_tokenize, pos_tag
 
def match_pos(sent1, sent2):
    sent1_tokens, sent2_tokens = word_tokenize(sent1), word_tokenize(sent2)
    sent1_pos, sent2_pos = pos_tag(sent1_tokens), pos_tag(sent2_tokens)
    matches = []
    for i in range(min(len(sent1_pos),len(sent2_pos))):
        if sent1_pos[i][1] == sent2_pos[i][1]:
            matches.append(sent1_pos[i][0] + ':' + sent2_pos[i][0])
    return matches
 
sent1 = 'She is the best player.'
sent2 = 'He is the worst player.'
 
print(match_pos(sent1,sent2))