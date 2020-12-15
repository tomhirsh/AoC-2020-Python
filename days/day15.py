class queue_age:
    def __init__(self, initial_turn):
        super().__init__()
        self.turns = [-1, initial_turn]
    
    def update_age(self, turn):
        prev_turn = self.turns[-1]
        self.turns = [prev_turn, turn]
    
    def get_age(self):
        return self.turns[1] - self.turns[0]


def get_starting_nums():
    return [0,13,1,8,6,15]


def get_last_spoken_word(last_word_turn, spoken_words, last_word, turn):
    while turn < last_word_turn:
        if last_word in spoken_words:
            spoken_words[last_word].update_age(turn)
            last_word = spoken_words[last_word].get_age()
        else:
            spoken_words[last_word] = queue_age(turn)
            last_word = 0
        turn += 1
    
    return last_word


if __name__ == "__main__":
    starting_nums = get_starting_nums()
    spoken_words = {num:queue_age(i+1) for i,num in enumerate(starting_nums[:-1])}
    last_word = starting_nums[-1]
    turn = len(starting_nums)
    print(get_last_spoken_word(2020, spoken_words, last_word, turn))
    print(get_last_spoken_word(30000000, spoken_words, last_word, turn))