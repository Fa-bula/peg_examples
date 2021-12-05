class ENode:
    def compute(self):
        self.isa = 0
        self.isb = 0
        self.nab = 0
        self.nba = 0

class SNode:
    def compute(self):
        self.A1.compute()
        self.A2.compute()
        self.res = self.A1.nab - self.A2.nba

class ANodea:
    def compute(self):
        self.A.compute()
        self.isa = 1
        self.isb = 0
        self.nba = self.A.nba
        if self.A.isb == 1:
            self.nab = self.A.nab + 1
        else:
            self.nab = self.A.nab

class ANodeb:
    def compute(self):
        self.A.compute()
        self.isa = 0
        self.isb = 1
        self.nab = self.A.nab
        if self.A.isa == 1:
            self.nba = self.A.nba + 1
        else:
            self.nba = self.A.nba
