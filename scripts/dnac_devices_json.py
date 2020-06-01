import json

class dnac_devices_json():

    def load_file(self,name):
       with open(name) as json_file:
            self.jsondata = json.load(json_file)
            
    
    def parse_data(self):
        for data in self.jsondata["response"]:
            print(data["id"])
            print(data["type"])
            print(data["family"])
            print(data["softwareType"])
            print(data["managementIpAddress"])
    
    def main(self):
        fname=input("Enter File Name: ")
        self.load_file(self,fname)
        self.parse_data(self)

if __name__ == '__main__':
    dnac_devices_json.main(dnac_devices_json)
