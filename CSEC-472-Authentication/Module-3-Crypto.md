# Crypto Review

- CIA
- Types of attack
- Kerchoffs principle

## Asymmetric Ciphers

- Trapdoor functions
- Examples
    - Knapsack
    - Prime factoring
    - Discrete Log

## Attacks on cryptosystems

- Ciphertext only
- Chosen plaintext
- Adaptive chosen plaintext
- Forward search
- Downgrade attack

## Hashes

### Criteria

- Preimage
- Second preimage
- Collision

## Authentication

- Mutual authentication
- Use of session key for forward secrecy

## Symmetric Key Authentication

- Disadvantages:
    - Key exchange
    - Introduce a nonce to provide mutual authentication

## Public key authentication

- Signing with the private key
- Don't use the same key pair for encryption and signing

## Perfect forward secrecy

- Crack the key in the future, still don't have access too all the stuff encrypted by that key
- [] => encrypt, {} => sign

## Zero-knowledge proof

- We need to prove someone's claim that they know some secret, without knowing their secret.

## Best authentication protocols

- Series of requirements