class Grid_Square(object):
    def __init__(self):
        self.dirty = False
    
    def change_dirt_status(self, dirty):
        """:param dirty: Boolean """
        self.dirty = dirty

    def print_dirty(self):
        print(self.dirty)

