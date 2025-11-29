# I->1
# V->5
# X->10
# L->50 
# C->100
# D->500
# M->1000

class IntegerToRoman:
    def ConvertRoman(self,num):
        integer= [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        Roman=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        RomanValueResult=""
        for i in range(len(integer)):
            while num>=integer[i]:
                RomanValueResult+=Roman[i]
                num-=integer[i]

        return RomanValueResult


# main()
if __name__=="__main__":
    num=int(input("Enter the integer value to convert to Roman numeral: "))
    obj= IntegerToRoman()
    RomanValue=obj.ConvertRoman(num)
    print(f"The Roman numeral of {num} is: {RomanValue}")