class SorQ():
    def __init__(self, maxlen, sorq):
        self._list = []
        self._maximum = maxlen
        self._type = sorq

    def push(self, val):
        x = self.check()
        if x == 1:
            return self._list.append(val)
        else:
            pass

    def getList(self):
        return self._list

    def pop(self):
        x = self.check()
        if x == 1:
            return self._list.pop()
        else:
            pass

    def check(self):
        if len(self._list) > 0 or len(self._list) < self._maximum:
            return 1
        else:
            return 0
