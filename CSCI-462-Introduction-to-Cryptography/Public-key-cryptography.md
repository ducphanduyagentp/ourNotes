# Public-key cryptography

## 02/28/2018

### Problems with symmetric key cryptography

- n people => n(n-1)/2 keys needed
- no non-repudiation

### Asymmetric cryptography

- Mailbox idea: anyone can drop a letter, but only the owner can open the mailbox
- Diffie-Hellman
- There is a public key and a private key
- It is slower than symmetric-key cryptography

#### Basic Protocol for Public-Key Encryption

#### Security mechanisms

- Key distribution
- Non-repudiation and digital signature
- Identification
- Encryption (RSA/Elgamal)

#### Basic key transport protocol

1. Diffie-Hellman key-exchange protocol
2. Hybrid protocol
- Bob sends Alice pubkey_B
- Alice sends Bob e(K, pubkey_B)
- K = D(E, privkey_B)
- AES(m, K)

#### Public key algorithms

- Based on one-way functions
- y = f(x) is computationally easy
- x = f_inv(y) is computationally infeasible

1. Factoring integers (RSA)
2. Discrete Logaritm (Diffie-Hellman, Elgamal, DSA)
3. Elliptic curves (EC) (ECDH, ECDSA)

#### Number theory for this cryptomagic

1. Euclidean Algorithm to find the gcd of two integers r_0 and r_1

- gcd(r_0, r_1) = gcd(r_0 - r_1, r_1)

2. Extended Euclidean Algorithm to find the modular inverse of r_1 mod r_0

- Magic table of Z_4

  |x  |0  |1      |2  |3    |
  |-  |-  |-      |-  |-    |
  |0  |0  |0      |0  |0    |
  |1  |0  |**1**  |2  |3    |
  |2  |0  |2      |0  |2    |
  |3  |0  |3      |2  |**1**|

- Look for 1 to find the modular inverse in a ring of number
- **Note**: Inverse of a mod m exists iff gcd(a, m) = 1
- How to do this magic:

  * modular inverse of 12 mod 67

    |-      |q_(i-1)|r_i|s_i|t_i|
    |-      |-      |-  |-  |-  |
    |0      |x      |67 |1  |0  |
    |1      |x      |12 |0  |1  |
    |2      |5      |7  |1  |-5 |
    |3      |1      |5  |-1 |6  |
    |4      |1      |2  |2  |-11|
    |5      |2      |1  |-5 |28 |

  * modular inverse of 43 mod 240

    240 = 5 * **43** + 25
    43  = 1 * **25** + 18
    25  = 1 * **18** + 7
    18  = 2 * **7**  + 4
    7   = 1 * **4**  + 3
    4   = 1 * **3**  + 1
    3   = 3 * **1**  + 0
    
    |-      |q_(i-1)|r_i  |s_i|t_i|
    |-      |-      |-    |-  |-  |
    |0      |x      |240  |1  |0  |
    |1      |x      |43   |0  |1  |
    |2      |5      |25   |  | |
    |3      |1      |18   | |  |
    |4      |1      |7    |  ||
    |5      |2      |4    | | |
    |6      |1      |3    |  ||
    |7      |1      |1    |-12 |67 |

3. Euler Phi function (Toitient function)

- phi(m) = # numbers that is coprime to m in the set {1..m - 1}
- e.g: phi(6) = 2, phi(5) = 4
- Factorize m:
  - phi(m) = pi{i = 1..n}(p_i ** e_i - p_i ** (e_i - 1))
  - ==> phi(p) = p ** 1 - p ** = p - 1
- RSA uses 2 prime numbers
- m = p * q => phi(m) = (p - 1) * (q - 1) if p and q are primes

4. Fermat's Little Theorem

- Given a prime p and an integer a: a**p = a (mod p)
- Same as a ** (p - 1) = 1 (mod p)
- Find modular inverse: if p is a prime:
a * a**(p - 2) = 1 (mod p)
==> a ** (-1) = a ** (p-2) (mod p) is the modular inverse mod p
