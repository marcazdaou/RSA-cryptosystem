import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])  # set n and e as command line argument
    e = int(sys.argv[2])
    message = stdio.readAll()  # accept message from standard input
    width = rsa.bitLength(n)   # write bitLength of n
    for c in str(message):
        x = ord(str(c))   # use ord() to change c to integer
        encrypted = (rsa.encrypt(x, n, e))  # encrypt x
        xBinary = rsa.dec2bin(encrypted, width)  # encrypted value as a width-long binary string
        stdio.write(xBinary)
    stdio.writeln()


if __name__ == '__main__':
    main()
