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

### Chinese Remainder Theorem

* Proof: By induction

* Theorem: Let n_1, n_2, ..., n_r be integers greater than 1. If n_i are pairwise coprime and a_1, a_2, ..., a_r are integers such that 0 <= a_i < n_i, then the system
  
  * x = a_1 (mod n_1)
  * x = a_2 (mod n_2)
  * ...
  * x = a_r (mod n_r)

  has a unique solution x.

* Example
  
  * x = 2 mod 3
  * x = 3 mod 5
  * x = 2 mod 7

  * N = n_1 * n_2 * n_3 = 3 * 5 * 7 = 105
  * N_1 = 35, N_2 = 21, N_3 = 15
  * b_1 * 35 = 1 mod 3 => b_1 = 2
  * b_2 * 21 = 1 mod 5 => b_2 = 1
  * b_3 * 15 = 1 mod 7 => b_3 = 1
  * x = (a_1 * b_1 * N_1 + a_2 * b_2 * N_2 + a_3 * b_3 * N_3) mod N = (2 * 2 * 35 + 3 * 1 * 21 + 2 * 1 * 15) mod 105 = 233 mod 105 = 23

## Fast decryption with CRT

### CRT-based exponentiation

* 3 steps:

  * Transformation
  * Exponentiation
  * Inverse transformation

* x_p => (x_p ** (d mod (p - 1))) mod p
* x_q => (x_q ** (d mod (q - 1))) mod q
* Example

  * (90 ** 547) mod 899, d = 547, n = 899
  * n = 29 * 31, p = 29, q = 31
  * Step 1: Transformation
    
    * x_p = x mod p = 90 mod 29 = 3
    * x_q = x mod q = 90 mod 31 = 28

  * Step 2: Exponentiation

    * d_p = d mod (p - 1) = 547 mod (29 - 1) = 15
    * d_q = d mod (q - 1) = 547 mod (31 - 1) = 7
    * y_p = x_p ** d_p mod p = 3 ** 15 mod 29 = 26
    * y_q = x_q ** d_q mod q = 28 ** 7 mod 31  = 14
    * In practice, p and q are chosen to have half the bit-length of n.

  * Step 3: Inverse transformation

    * c_p = inv(q) mod p
      31 ** (-1) mod 29 = 2 ** (-1) mod 29 = 15
    * c_q = inv(p) mod q
      29 ** (-1) mod 31 = 15s
    * Result: y = [(q * c_p) * y_p + (p * c_q) * y_q] mod n                                   * The primes p and q are not frequently changed

## Complexity of CRT

## Finding large primes

### Primality Tests

* Outputs are probabilistic:
   
   * N is composite => Always true
   * N is prime => Not always true

#### Fermat Primality Test

  * If a number p' is prime and a ** (p' - 1) = 1 (mod p') for a in {2, 3, ..., p' - 2}
  ```python
    for _ in range(s):
        a = rand(2, p_prime - 1)
        if (a ** (p_prime - 1)) % p_prime != 1:
          return "p_prime is composite"
    return "p_prime is likely a prime"
  ```
  * `a` is a Fermat witness <= p' is composite
  * `a`is a Fermat liar <= False result

#### Miller-Rabin's test

  * Given the decomposition of an odd prime candidate p':
    `p' - 1 = (2 ** u) * r`
    where r is odd
  * If we can find an integer `a` such that:
    `a**r != 1 mod p'`
  * and `a**` //TODO

## Attacks on RSA

### Secure RSA

1. Don't use primes too close to each other
2. the public exponent `e` is usually small for fast public operation. Make sure m ** e is greater than n so that `D(m**e) != m ** (1/e)`
3. Don't send the same message M with different public key with the same publick exponent `e`.
  
    - <code>C<sub>1</sub> = M<sup>3</sup>(mod n<sub>1</sub>)
    - <code>C<sub>2</sub> = M<sup>3</sup>(mod n<sub>2</sub>)
    - <code>C<sub>3</sub> = M<sup>3</sup>(mod n<sub>3</sub>)

    Using CRT we can solve for `M**3` and to obtain M, calculate `(M**3)**(1/3)`
4. Homomorphic property of RSA
    
    - Sign M_1: s_1 = M_1 ** d (mod n)
    - Sign M_2: s_2 = M_2 ** d (mod n)
    - If there is a M_3 = M_1 * M_2, the signature is s_1 * s_2 (mod n). This can be calculated without using the private key

5. Shared factor attack

### Math attacks on RSA

#### Factoring problem

- Factoring n. This enables the calculation of the private key.
- General number field sieve (GNFS): Most efficient classical algorithm for factoring integers larger than 10<sup>100</sup>
- Special number field sieve (SNFS)

### Others

- Chosen ciphertext
- Hardware fault-based
- Bruteforce
- Math
- Timing attack

## Optimal Asymmetric encryption padding (OAEP)

## Diffie-Hellman Key Exchange

### Setup

1. Choose large prime q
2. Chose an integer alpha in range [2, q - 2] such that alpha is a primitive root of q
3. Publish q and alpha

* Primitive root: alpha is a primitive root modulo q if for every integer a coprime to p, there is an integer k such that alpha<sup>k</sup> = a (mod q)

### Key Exchange

1. Generate a private key X_A, X_B
2. Public key: Y_A = alpha ** X_A (mod q), Y_B = alpha ** X_B (mod q)
3. Shared secret. Y_A ** X_B (mod q) == Y_B ** X_A (mod q)

## The Discrete Log problem

## MITM attack

### A generator of the group Z(*, pp)

* Primitive root: alpha is a primitive root modulo q if for every integer a coprime to p, there is an integer k such that alpha<sup>k</sup> = a (mod q)
* alpha is a generator of the multiplicative group of integers modulo Z(*. p)

### Subgroup of the group Z(*, p)

* Example: subgroups of Z(*, 7)

    * ({1}, .) order 1
    * ({1, 6}, .) order 2
    * ({1, 2, 4} .) order 3
    * Z(*, 7) order 6

### Prevention

* Digital signature
* Safe domain parameters:

## El Gamal encryption

