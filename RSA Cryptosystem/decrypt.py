import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])  # set n and d as command line argument
    d = int(sys.argv[2])
    width = rsa.bitLength(n)  # set width as bitLength of n
    message = stdio.readAll()  # accept message from standard input
    v = len(str(message))  # v is length of message
    for i in range(0, v - 1, width):  # for i ∈ [0, l − 1) and in increments of width
        s = str(message)[i:(i + width)]
        y = (rsa.bin2dec(s))  # set y to decimal value of s
        decrypted = rsa.decrypt(y, n, d)  # decrypt y
        f = chr(decrypted)   # use chr() to change int to character
        stdio.write(str(f))


if __name__ == '__main__':
    main()
