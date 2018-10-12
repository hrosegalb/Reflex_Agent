class Grid_Square(object):
    def __init__(self):
        self.dirty = False
    
    def change_dirt_status(self, dirty):
        """:param dirty: Boolean """
        self.dirty = dirty

    def get_dirty_status(self):
        return self.dirty

