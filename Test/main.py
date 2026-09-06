decoded = []
tempStr = ""
counter = 0
s = "10#HELLOWORLD5#HELLO"
for i in range(len(s)):
    if(s[i] == '#'):
        counter = int(s[0:i])
    s = s[i+1:]
    for j in range(counter):
        tempStr += s[j]
    decoded.append(tempStr)
    tempStr = ""
    s = s[i+counter:]

print (decoded)