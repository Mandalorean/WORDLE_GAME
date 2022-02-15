class alpha_pos:
    #flags for words in wrong position and correct position
    def __init__(self, character: str):
        self.character: str = character
        self.wrong_pos: bool = False
        self.correct_position: bool = False

    def __repr__(self):
        return f"[{self.character} wrong_pos: {self.wrong_pos} correct_position: {self.correct_position}]"
