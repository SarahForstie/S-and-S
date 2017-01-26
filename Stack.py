from sq_parent_class import *

class stack(SorQ):
    def __init__(self):
        super().__init__(50, "Stack")

    def push(self, val):
        x = self.check()
        if x == 1:
            return self._list.append(val)
        else:
            pass
