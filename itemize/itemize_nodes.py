class SNode:
    def compute(self):
        return self.A.compute()

class INode:
    def compute(self):
        return self.text

class ANode:
    def compute(self):
        return "* " + self.I.compute() + "\n" + self.A.compute()

class ENode:
    def compute(self):
        return ""

class ASNode:
    def compute(self):
        return "  " + self.S.compute() + self.A.compute()
