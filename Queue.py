from sq_parent_class import *

class queue(SorQ):
    def __init__(self):
        super().__init__(50, "Queue")

    def pop(self):
        x = self.check()
        if x == 1:
            return self._list.pop(0)
        else:
            pass
        
