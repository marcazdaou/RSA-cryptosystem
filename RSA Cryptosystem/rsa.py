import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primes = _primes(lo, hi)  # set primes to list of _primes from lo to hi

    i = stdrandom.uniformInt(0, len(primes) - 1)  # Sample two distinct random primes p and q
    j = stdrandom.uniformInt(0, len(primes) - 1)
    while i == j:
        j = stdrandom.uniformInt(0, len(primes) - 1)
    p = primes[i]
    q = primes[j]
    n = p * q  # Set n and m to pq and (p − 1)(q − 1), respectively.
    m = (p - 1) * (q - 1)
    primes2 = _primes(2, m)  # Find a d ∈ [1, m) such that ed mod m = 1.
    e = primes2[stdrandom.uniformInt(0, len(primes2) - 1)]
    # Choose a random prime e such that e does not divide m
    d = 0
    for i in range(1, m):
        if (e * i) % m == 1:
            d = i
            break
    return n, e, d  # Return the tuple1(n, e, d).


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    E = x ** e % n  # Implement the function E(x) = x**e mod n
    return E


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    D = y ** d % n  # implement the function D(y) = y**d mod n
    return D


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    primes = []  # set primes to empty list
    for p in range(lo, hi + 1):  # for p in range lo to hi+1
        j = 2
        while j * j <= p:  # as long as 2j <= p
            if p % j == 0:  # if p is not prime break
                break
            j = j + 1  # increment j by 1
        if p % j != 0:  # if p is prime
            primes += [p]  # append p to list primes
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    b = a[:]
    c = b[0:k]
    stdrandom.shuffle(c)
    return c


# Returns a random item from the list a.
def _choice(a):
    v = len(a)
    r = stdrandom.uniformInt(0, v)
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
