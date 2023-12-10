def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32:
            a = 64
        t = a + k
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        cipher += chr(t)
    return cipher

def decipher(ct, k):
    n = len(ct)
    dec = ''
    for i in range(n):
        a = ord(ct[i])
        if a == 64:
            a = 32
        t = a - k
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        dec += chr(t)
    return dec

if __name__ == "__main__":
    plainText = 'SAVE PRIVATE RYAN'
    K = 1
    print('평 문 : ', plainText)
    cipherText = encipher(plainText, K)
    print('암호문 : ', cipherText)
    decText = decipher(cipherText, K)
    print(f"복호화 : {decText}")
