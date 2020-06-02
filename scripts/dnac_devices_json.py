import json
import UnitTester as UT
import requests
import base64
class dnac_devices_json():

    def load_file(self,name):
       with open(name) as json_file:
            self.jsondata = json.load(json_file)

    def get_token(self,LoginCreds):
        EncodedCreds = base64.b64encode(bytes(LoginCreds['Username'] + ':' + LoginCreds['Password'], "utf-8")).decode("ascii")
        headers = { 'Authorization' : 'Basic '+EncodedCreds }
        payload = {}
        r = requests.post('https://sandboxdnac2.cisco.com/api/system/v1/auth/token', 
                                    headers=headers, 
                                    data = payload)
        d=r.json()
        print(d)
        return d['Token']                           

    def get_devices_data(self):
        headers={'x-auth-token': self.authtoken}
        r=requests.get("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device",
                        headers=headers,
                        data={})
        d=r.json()
        print(d)
        return d
    
    def parse_data(self):
        for data in self.devdata["response"]:
            print(data["id"])
            print(data["type"])
            print(data["family"])
            print(data["softwareType"])
            print(data["managementIpAddress"])
            self.devlist.append([data["id"],data["type"],
                data["family"],
                data["softwareType"],
                data["managementIpAddress"]])
    
    def main(self,creds):
        self.devlist=[]
        self.authtoken=self.get_token(self,creds)
        self.devdata=self.get_devices_data(self)
        self.parse_data(self)
        self.tester=UT.test_data()
        self.tester.test_dnac_devices(self.devlist)


if __name__ == '__main__':
    devclass=dnac_devices_json.main(dnac_devices_json,{'Username':'dnacdev', 'Password':'D3v93T@wK!'})
