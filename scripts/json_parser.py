import json
import UnitTester as UT
class load_data_json():

    def load_file(self,name):
       with open(name) as json_file:
            self.jsondata = json.load(json_file)
            
    
    def parse_data(self):
        self.parents.append("ACCT100")
        self.paidlist.append(self.jsondata["ACCT100"]["paid"])
        self.duelist.append(self.jsondata["ACCT100"]["due"])
        self.parents.append("ACCT200")
        self.paidlist.append(self.jsondata["ACCT200"]["paid"])
        self.duelist.append(self.jsondata["ACCT200"]["due"])
        self.parents.append("ACCT300")
        self.paidlist.append(self.jsondata["ACCT300"]["paid"])
        self.duelist.append(self.jsondata["ACCT300"]["due"])
        print("ACCT100")
        print(self.jsondata["ACCT100"]["paid"])
        print(self.jsondata["ACCT100"]["due"])
        print("ACCT200")
        print(self.jsondata["ACCT200"]["paid"])
        print(self.jsondata["ACCT200"]["due"])
        print("ACCT300")
        print(self.jsondata["ACCT300"]["paid"])
        print(self.jsondata["ACCT300"]["due"])
        
    
    def main(self):
        self.parents=[]
        self.duelist=[]
        self.paidlist=[]
        fname=input("Enter File Name: ")
        self.load_file(self,fname)
        self.parse_data(self)
        self.tester=UT.test_data()
        self.tester.test_data_children(self.parents)
        self.tester.test_data_paid(self.paidlist)
        self.tester.test_data_due(self.duelist)

if __name__ == '__main__':
    load_data_json.main(load_data_json)
