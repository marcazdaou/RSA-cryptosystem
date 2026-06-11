# RSA Cryptosystem

A from-scratch implementation of the **RSA public-key cryptosystem** in Python — key generation, encryption, and decryption — built on the mathematical difficulty of factoring large semiprime numbers.

## Mathematical Foundation

```
Key Generation:
  1. Select two large primes p and q
  2. Compute n = p · q  (the modulus)
  3. Compute φ(n) = (p−1)(q−1)
  4. Choose e coprime to φ(n)       → Public key:  (e, n)
  5. Compute d ≡ e⁻¹ (mod φ(n))    → Private key: (d, n)

Encryption:  c = m^e mod n
Decryption:  m = c^d mod n
```

## Features

- **Key pair generation** with configurable bit length
- **Miller-Rabin primality test** for fast, probabilistic large-prime selection
- **Extended Euclidean Algorithm** for modular inverse computation
- **Fast modular exponentiation** using Python's built-in `pow(base, exp, mod)`
- Encrypt and decrypt arbitrary integer messages
- Cryptographically secure random number generation via `secrets` module

## Algorithms Implemented

| Algorithm | Purpose |
|---|---|
| Miller-Rabin | Probabilistic primality testing |
| Extended Euclidean | Compute modular inverse (private key) |
| Fast modular exponentiation | Efficient `m^e mod n` |
| Sieve of Eratosthenes | Pre-filter small primes before Miller-Rabin |

## Technologies

- **Python**
- Number theory: Miller-Rabin, Extended GCD
- `secrets` module for secure randomness

## Usage

```bash
python rsa.py
```

```
Generated public key  (e, n): (65537, 2734...8901)
Generated private key (d, n): (1823...4471, 2734...8901)

Message:  42
Encrypted: 1947...3820
Decrypted: 42  ✓
```

## Security Notes

This implementation demonstrates core RSA mechanics for educational purposes. For production use, always use a vetted library (e.g., `cryptography`) with proper OAEP padding and constant-time operations.