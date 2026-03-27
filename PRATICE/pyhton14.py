#sip formulae 
class sip:
    def __init__(self,p,r,y):
        self.p = p
        self.r =r
        self.y = y
        self.no_of_payments = y*12
        self.preodic_rate = self.r/1200
    def sip_cal(self):
        fv = self.p*(((1+self.preodic_rate)**self.no_of_payments)/self.preodic_rate)*(1+self.preodic_rate)
        return fv
try:
    principle = float(input("enter the principal: "))
    rate_of_return = float(input("enter the rate of return(annualised): "))
    y = int(input("enter the no. of years of investment: "))
    if (principle<=0 or rate_of_return<=0 or y<=0):
        print("\n[!] cannot proceed futher...\n")
        print("[!] please chech once again the entries...\n")
        exit()
    r = sip(principle,rate_of_return,y)
    print(round(r.sip_cal(),2))
except ValueError:
    print("[!] value error please enter only the number!!")
    