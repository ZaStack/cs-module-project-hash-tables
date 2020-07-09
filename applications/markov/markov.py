import random
import sys
from collections import defaultdict, Counter

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    model = defaultdict(Counter)
    end_chars = '.!?'
    STATE_LEN = 4
    for i in range(len(words) - STATE_LEN):
        state = words[i:i + STATE_LEN]
        next = words[i + STATE_LEN]
        model[state][next] += 1

    state = random.choice(list(model))
    out = list(state)
    # sentences = 0
    # while sentences < 5:
    for i in range (len(model)):
        # for word in words:
        #     if word.__contains__(end_chars):
        #         sentences += 1
        out.extend(random.choices(list(model[state]), model[state].values()))
        state = state[1:] + out[-1]
    print(''.join(out))

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

