import pytch

class Problem(pytch.Sprite):
    @property
    def _x(self):
        raise RuntimeError("oh no")

    @_x.setter
    def _x(self, x):
        pass

    @pytch.when_I_receive("trouble")
    def cause_trouble(self):
        self.show()

class Counter(pytch.Sprite):
    @pytch.when_I_receive("go")
    def init(self):
        self.n = 0;
        while True:
            self.n += 1
