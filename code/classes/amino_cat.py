class Amino():
    """ 
    This class holds the attributes for an amino acid. The color and text
    differ per amino acid but the location is always initialized at (0, 0). 
    """
    def __init__(self, text, color):
        self.color = color
        self.text = text
        # self.row = 0
        # self.column = 0
        self._location = (0, 0)
        
    def update_loc(self):
        pass