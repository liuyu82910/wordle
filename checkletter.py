

class CheckLetter:
    def __init__(self, character: str):
        self.character: str = character
        self.in_word: bool = False
        self.in_position: bool = False
            
    def __repr__(self):
        return f"{self.character} word: {self.in_word}, position: {self.in_position}"
