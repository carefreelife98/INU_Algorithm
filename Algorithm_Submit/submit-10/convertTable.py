def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32:
            a = 0
        else:
            a -= 64
        cipher += k[a]
    return cipher

def decipher(dec, k):
    n = len(dec)
    cipher = ''
    for i in range(n):
        idx = k.index(dec[i])
        if idx == 0:
            idx = 32
        else:
            idx += 64
        cipher += chr(idx)
    return cipher

if __name__ == "__main__":
    plainText = 'SAVE PRIVATE RYAN'
    K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
    print('평  문 : ', plainText)
    cipherText = encipher(plainText, K)
    print('암호문 : ', cipherText)
    decText = decipher(cipherText, K)
    print(f"복호문 : {decText}")
