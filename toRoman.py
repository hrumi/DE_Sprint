def intToRoman(num) -> str:
        
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        result = ""
        
        roman = []
        for i in range(len(values)):
            while(num >= values[i]):
                num = num - values[i]
                roman.append(romans[i])
                s = ''.join(roman)
        return s

print (intToRoman(1))