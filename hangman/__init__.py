
# coding: utf-8

# In[21]:


class Hangman:
    def __init__(self, word_set):
        from random import choice
        self.word_set = word_set
        word = choice(self.word_set)
        self.word = word
        
    def build_word(self, guess_set):
        word = ''
        for s in self.word:
            if s not in guess_set:
                s = '*'
            word += s
        return word
    
    def guess_a_letter(self):
        mistake_counter = 0
        mistake_limit = 5
        guess_set = set()
        while (mistake_counter != mistake_limit) and (guess_set != set(self.word)):
            print('Guess a letter:\n')
            letter = input()
            if letter in self.word:
                guess_set.add(letter)
                
                print('Hit!\n\nThe word: {}'.format(self.build_word(guess_set)))
            else:
                mistake_counter += 1
                print('Missed, mistake {} out of ' 
                      '{}.\n\nThe word: {}\n'.format(mistake_counter, mistake_limit, self.build_word(guess_set)))
        if mistake_counter == mistake_limit:
            print('You lost!')
        if guess_set == set(self.word):
            print('You won!')


# In[24]:


def main():
    words = ['shark', 'date', 'boss', 'aginity', 'world', 'triangular', 
             'mistake', 'rush', 'landscape', 'groove', 'fireworks']
    player_1 = Hangman(words)
    player_1.guess_a_letter()


# In[ ]:

if __name__ == '__main__':
    main()
