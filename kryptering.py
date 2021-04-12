# encoding=utf-8
# för varje tecken i variabel text då plusar key varje gång
def encrypt(text, key):
    outText = []
    cryptText = []

    upper = ['A','B','C','D','E','F','G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Q','Y','Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in text:
        if i in upper:
            index = upper.index(i) #position på tecknet
            newindex = (index + key) % 26
            cryptText.append(newindex)
            newLetter = upper[newindex]
            outText.append(newLetter)
        elif i in lower:
            index = lower.index(i)
            newindex = (index + key) % 26
            cryptText.append(newindex)
            newLetter = lower[newindex]
            outText.append(newLetter)
    return outText

# i varje tecken i variabel text så blir det minus key varje gång
def decrypt(text,key):
    return encrypt(text,-key)

def runtestcode (text, key):
    print('-'*50)
    print("Klartext :",text,"Key :",key)
    krypterat = encrypt(text,key)
    print("Krypterat:",krypterat)
    okrypterat = decrypt(krypterat,key)
    print("Avkodat:", okrypterat)
   
runtestcode("HEJ",2)