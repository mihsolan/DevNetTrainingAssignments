import xml.etree.ElementTree as ET
import UnitTester as UT

class load_data_xml():

    def load_file(self,name):
        self.xmlfile = ET.parse(name)
        return self.xmlfile.getroot()
    
    def parse_data(self,root):
        for child in root:
            print("Account Name:" + child.tag)
            print("Account Attributes(if any):")
            print(child.attrib)
            self.parents.append(child.tag)
            print("Paid Amount:"+child[0].text)
            print("Due Amount:" +child[1].text)
            self.paidlist.append(child[0].text)
            self.duelist.append(child[1].text)
    
    def main(self):
        self.parents=[]
        self.duelist=[]
        self.paidlist=[]
        fname=input("Enter File Name: ")
        self.xmlroot= self.load_file(self,fname)
        self.parse_data(self,self.xmlroot)
        self.tester=UT.test_data()
        self.tester.test_data_children(self.parents)
        self.tester.test_data_paid(self.paidlist)
        self.tester.test_data_due(self.duelist)

if __name__ == '__main__':
    load_data_xml.main(load_data_xml)
