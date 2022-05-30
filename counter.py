
class Counter:

    def __init__(self, startValue, incrementalValue, limitValue ):
        self.startValue_ = startValue
        self.incrementalValue_ = incrementalValue
        self.limitValue_ = limitValue
        self.currentValue = self.startValue_
    
    def count(self):
        self.startValue_ += self.incrementalValue_
    
    def getCurrentNumber(self):
        return self.startValue_
