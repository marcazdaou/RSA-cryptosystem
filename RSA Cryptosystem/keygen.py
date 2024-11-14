import rsa
import stdio
import sys


# Entry point.
def main():
    lo = int(sys.argv[1])  # set lo and hi as command line argument
    hi = int(sys.argv[2])
    n, e, d = rsa.keygen(lo, hi)  # use the rsa.keygen to get values of n, e, d
    stdio.write(str(n) + " " + str(e) + " " + str(d))   # write str(n) , str(e), str(d)


if __name__ == '__main__':
    main()
