from checkletter import CheckLetter
class Wordle:
    
    MAX_TRY = 6
    LENGTH = 5
    VOID_LETTER = '*'

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        
    @property    
    def won(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def attempts_balance(self) -> int:
        return self.MAX_TRY - len(self.attempts)
    
    @property
    def check_attempts(self) -> bool:
        return self.attempts_balance > 0 and not self.won
    
    def attempt(self, word: str):
        word = word.upper()
        return self.attempts.append(word)
    
    def compare(self, word: str):
        word = word.upper()
        result = []
        for i in range(self.LENGTH):
            letter = CheckLetter(word[i])
            letter.in_word = word[i] in self.secret
            letter.in_position = word[i] == self.secret[i]
            result.append(letter)
        return result
