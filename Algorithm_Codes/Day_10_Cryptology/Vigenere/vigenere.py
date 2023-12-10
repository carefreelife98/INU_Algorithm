def encipher(p, k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i % n]) - 64
        t = a + b
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)
    return c

def decipher(c, k):
    p = ''
    n = len(k)
    for i in range(len(c)):
        a = ord(c[i])
        if a == 32:
            a = 64
        b = ord(k[i % n]) - 64
        t = a - b
        if t < 65:
            t += 27
        if t == 91:
            t = 32
        p += chr(t)
    return p

if __name__ == "__main__":
    plainText = 'SAVE PRIVATE RYAN'
    K = 'ABC'
    print('평  문 : ', plainText)
    cipherText = encipher(plainText, K)
    print('암호문 : ', cipherText)
    decText = decipher(cipherText, K)
    print(f"복호문 : {decText}")
