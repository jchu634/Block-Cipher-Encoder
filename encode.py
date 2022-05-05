from os import path
def output(cipherText):
    print(hex(cipherText)[2:].upper(),end=" ")
def ECB(plainText,key):
    print("ECB = ",end="")
    for text in plainText:
        output(text^key)
    print()

def CBC(plainText,key,iv):
    print("CBC = ",end="")
    for text in plainText:
        cipherText = (text^iv)^key
        output(cipherText)
        iv = cipherText
    print()

def PCBC(plainText,key,iv):
    print("PCBC = ",end="")
    for text in plainText:
        midText = (text^iv)
        cipherText = midText^key
        output(cipherText)
        iv = cipherText^text
    print()

def CFB(plainText,key,iv):
    print("CFB = ",end="")
    for text in plainText:
        cipherText = (iv^key)^text
        output(cipherText)
        iv = cipherText
    print()

def OFB(plainText,key,iv):
    print("OFB = ",end="")
    for text in plainText:
        midText = (iv^key)
        cipherText = midText^text
        output(cipherText)
        iv = midText
    print()

def main():
    with open("input.txt") as f:
        plainText = [int(a,16) for a in f.read().splitlines()]

    if path.exists("keys.txt"):
        keys = open("Keys.txt")
        key = int(keys.readline(),16)
        initialisationVector = int(keys.readline(),16)
        keys.close()
    else:
        key = int(input('Key: '),16)
        initialisationVector = int(input('I.V.: '),16)

    print("Key: " + hex(key)[2:].upper())
    print("I.V.: " + hex(initialisationVector)[2:].upper())

    ECB(plainText,key)
    CBC(plainText,key,initialisationVector)
    PCBC(plainText,key,initialisationVector)
    CFB(plainText,key,initialisationVector)
    OFB(plainText,key,initialisationVector)

if __name__ == '__main__':
    main()


    

# print(plainText)

