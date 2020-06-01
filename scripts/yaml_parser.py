import yaml
import UnitTester as UT
class load_data_yaml():

    def load_file(self,name):
       with open(name) as yaml_file:
            self.yamldata = yaml.load(yaml_file,Loader=yaml.FullLoader)

            
    def parse_data(self):
        for account in self.yamldata:
            print("Account Number: "+account)
            print("Paid: "+ str(self.yamldata[account]["paid"]))
            print("Due: "+ str(self.yamldata[account]["due"]))
            self.parents.append(account)
            self.duelist.append(self.yamldata[account]["due"])
            self.paidlist.append(self.yamldata[account]["paid"])

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
    load_data_yaml.main(load_data_yaml)
