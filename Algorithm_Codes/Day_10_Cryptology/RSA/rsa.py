import re


def encipher(plain, n, p):
    cipher = ''
    i = 0
    while i < len(plain):
        m = ''
        for j in range(4):
            m += plain[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(p):
            b = t % n
            t = a * b
        if b < 10:
            cipher += '000' + str(b)
        elif b < 100:
            cipher += '00' + str(b)
        elif b < 1000:
            cipher += '0' + str(b)
        else:
            cipher += str(b)
    return cipher

def decipher(enc, s, n):
    recover = ''
    loop = len(enc) // len(str(n))
    while loop:
        tg = int(enc[:4])
        enc = enc[4:]
        # print(f"tg={tg}, enc={enc}")

        concatstr = str(pow(tg, s) % n)
        match len(concatstr):
            case 1:
                concatstr = '000' + concatstr
            case 2:
                concatstr = '00' + concatstr
            case 3:
                concatstr = '0' + concatstr

        recover += concatstr
        loop -= 1
    return recover

def encode(plain):
    n = len(plain)
    m = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32:
            a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)
    return m

def decode(recov):
    n = len(recov)
    m = ''
    for i in range(0, n, 2):
        temp_d = int(recov[i:i+2]) + 64
        if temp_d == 64:
            temp_d = 32
        m += chr(temp_d)
    return m

if __name__ == "__main__":
    plainText = 'SAVE PRIVATE RYAN '
    N = 3713
    # 비밀 키
    S = 97
    P = 37
    plainMessage = encode(plainText)
    print('평  문 : ', plainMessage)
    cipherMessage = encipher(plainMessage, N, P)
    print('암호문 : ', cipherMessage)
    recov = decipher(cipherMessage, S, N)
    print(f"복호문 : {recov}")
    origin = decode(recov)
    print(f"복호화된 Text : {origin}")
