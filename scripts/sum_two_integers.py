import UnitTester as UT
class sum_two_integers():

    def main(self,arr,sum):
        sublist={}
        i=0
        for ele in arr:
            sub=sum-ele
            if(sublist.__contains__(sub)):
                return [sublist[sub],i]
            sublist[ele]=i 
            i+=1

if __name__ == '__main__':
    result=sum_two_integers.main(sum_two_integers,[2,7,11,15],26)
    print(result)
    tester=UT.test_data()
    tester.test_sum_integers(result)