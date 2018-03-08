# RSA Cryptosystem

## Encryption and Decryption

- Public key(n, e) = k_pub
- Private key d = k_priv
- Encryption: y = enc(x, k_pub) = x ** e mod n
- Decryption: x = d(y, k_priv) = y ** d mod n
- In fact, numbers used in RSA may not really be prime numbers. They are randomly chosen and tested agains certain tests.

## Key generation

1. Choose 2 large prime p, q
2. n = p * q
3. phi(n) = (p - 1) * (q - 1)
4. Select the public exponent e in range [1..phi(n) - 1] such that gcd(e, phi(n)) == 1
5. Private key d is the modular inverse of e in the GF(phi(n)), d * e = 1 (mod phi(n))
6. Return pubkey = (n, e), privkey = d

## Implementation aspects

### Fast exponent