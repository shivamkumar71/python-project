from random import randint
class train:
    
    def __init__(self,trainno):
        self.trainno=trainno
        
    def book(self,trainno,fro, to):
        print(f"ticket is booked in train no {self.trainno}")
        
    def getstatus(self):
        print(f"train number: {self.trainno} is running on time")
    def getfare(self, trainno,fro, to):
        print(f"ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(222, 5555)}")


t = train(12345)
t.book(12345,"delhi", "mumbai")
t.getstatus()
t.getfare(12345,"delhi", "mumbai")
        