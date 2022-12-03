testString1 = "helloolleh"
testString2 = "hello 1"

def stringCheck(s):
    s1 = str(s)
    s1 = s1.replace(" ","")
    return s1 == s1[::-1]

print (stringCheck(testString1))
print (stringCheck(testString2))

