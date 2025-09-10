def caesar(p, key):
    c = ""
    for i in p:
        if i.isupper():
            c += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
        elif i.islower():
            c += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
        else:
            c += i
    return c

p = "Vo Thi Thanh Kieu"
key = 7
print(caesar(p,key))
