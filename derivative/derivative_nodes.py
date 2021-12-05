class SNode1:
    def compute(self):
        return "".join([self.M.compute(), "+", self.S.compute()])

class SNode2:
    def compute(self):
        return self.M.compute()

class MonomNode:
    def compute(self):
        return "".join([str(self.K1.compute() * self.K2.compute()),
                        "x^", str(self.K2.compute() - 1)])

class KNode:
    def compute(self):
        return int(self.text)
