# Elliptic Curve cryptography

## Abelian Group

- Axioms
  - Closure
  - Associative
  - Identity element
  - Inverse element

## Elliptic curves over real numbers

- **NOT** Ellipses
- Weierstrass equation

## Computations on Elliptic Curves

- Elliptic Curve Point addition and doubling formulas
- x_3 = s ** 2 - x_1 - x_2 (mod p)
- y_3 = s(x_1 - x_3) - y_1 (mod p)
- s
  - (y_2 - y_1) / (x_2 - x_1) (mod p) if P != Q (point addition)
  - (3x**2 + a)/(2y_1) (mod p) if P == Q (point doubling)
- Note that in the formula y_3 depends on x_3 and they both depend on s

## Elliptic curves over prime fields

- The elliptic curve over Z_p (p > 3) is the set of all pairs (x, y) in Z_p so that:
  - y ** 2 = x ** 3 + ax + b (mod p)
  - (a, b) in Z_p
  - 4(a ** 3) + 27(b ** 2) != 0 (mod p)
  - And an imaginary point O
- Those points form a finite group

## Elliptic curve DLP

- The operation is adding
- Given a primitive element P and another element Q on an elliptic curve E.
- The ECDL problem is finding the integer d where 1 <= d <= #E such that:
  - dP = Q (adding P d times)
- In some cryptosystem d is considered a private key because it's hard to find.
- Example:
  - E_p(a, b) = y ** 2 = x ** 3  + ax + b (mod p)
  - E_23(9, 17)
  - P is the base

## Point Multiplication

- Double-and-Add algorithm just like Square-and-Multiply

## Elliptic curve DH Protocol

- Given a prime p a suitable elliptic curve E and a point P(x_P, y_P) of high order
- ECDHE:
  - k_priv = a in {2..#E-1}
  - k_pub = A = dP = (x_A, y_A)
  - Common secret = aB = T_ab = (x_T, y_T) (B is Bob's public key)
- Symmetric encryption:
  - k_AES = x_T
  - c = enc(m, x_T)
  - m = dec(c, X_T)

## Implementation
