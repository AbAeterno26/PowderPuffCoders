class Amino():
    """ 
    This class holds the attributes for an amino acid. The color and text
    differ per amino acid but the location is always initialized at (0, 0). 
    """
    def __init__(self, text, color, amino_id):
        self.color = color
        self.text = text
        self._location = (0, 0)
        self.amino_id = amino_id
        
    def update_loc(self, location):
        self._location = location
        