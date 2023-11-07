class RBI:
    def Intrest(self):
        pass
class SBI(RBI):
    def Intrest(self):
        print("SBI Intrest is 5%")
class HDFC(RBI):
    def Intrest(self):
        print("HDFC Intrest is 2%")
s2=SBI()
h1=HDFC()
s2.Intrest()
h1.Intrest()