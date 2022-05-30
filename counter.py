
class MyCounter:

    def __init__(self, startValue = None, incrementalValue = None, limitValue = None ):
        if startValue is None:
            self.startValue_ = 0;
        else:
            self.startValue_ = startValue


        if incrementalValue is None:
            self.incrementalValue_ = 1
        else:
            self.incrementalValue_ = incrementalValue


        if limitValue is None:
            print ("cannot be empty")
        else: 
            self.limitValue_ = limitValue
    
    def count(self):
        if(self.startValue_< self.limitValue_):
            self.startValue_ += self.incrementalValue_
        else:
            print(" the current value is bigger than the limit value ")
    def getCurrentNumber(self):
        return self.startValue_
