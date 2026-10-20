# RSA Cryptosystem

A from-scratch, **educational** implementation of the RSA public-key cryptosystem in Python: key generation,
encryption and decryption of text messages, written for an introductory programming course. It uses small primes so
every step can be followed by hand; it is a learning tool, not secure cryptography.

## How it works (`RSA Cryptosystem/rsa.py`)

```
Key generation  keygen(lo, hi)
  1. List the primes in [lo, hi) by trial division and pick two distinct ones, p and q
  2. n = p·q   and   m = (p − 1)(q − 1)
  3. Pick a random prime e < m                      → public key  (n, e)
  4. Search for d in [1, m) with e·d mod m = 1      → private key (n, d)

Encryption  E(x) = x^e mod n          Decryption  D(y) = y^d mod n
```

Text is encrypted one character at a time: each character's code (`ord`) is encrypted and written as a
fixed-width binary string (width = bit length of `n`), and decryption reverses the process.

## Programs

| File | What it does |
|---|---|
| `rsa.py` | Library: `keygen`, `encrypt`, `decrypt`, `bitLength`, `dec2bin`, `bin2dec` |
| `keygen.py` | Generates and prints a key pair `n e d` from primes in a given range |
| `encrypt.py` | Reads a message from standard input and writes it encrypted as a binary string |
| `decrypt.py` | Reverses `encrypt.py` with the private key |
| `distance.py`, `palindrome.py`, `reverse.py`, `sin.py`, `transpose.py` | Smaller exercises from the same assignment |

## Run

The programs use the course's standard I/O library (`stdio`, `stdrandom`).

```bash
python keygen.py 50 100                      # prints n e d
echo "Hello" | python encrypt.py <n> <e>     # prints the encrypted bits
echo "<bits>" | python decrypt.py <n> <d>    # prints Hello
```

## Concepts

Modular arithmetic · Euler's totient · modular inverse · public-key cryptography · binary encoding
