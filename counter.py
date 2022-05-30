
class MyCounter:

    def __init__(self, startValue = 0, incrementalValue, limitValue ):
        self.startValue_ = startValue
        self.incrementalValue_ = incrementalValue
        self.limitValue_ = limitValue
    
    def count(self):
        self.startValue_ += self.incrementalValue_
    
    def getCurrentNumber(self):
        return self.startValue_
