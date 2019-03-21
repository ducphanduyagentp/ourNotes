1
Identification is the process of claiming to be someone or something.

2
Authentication is the process of ensuring a party is what/who they claim to be.

3
Authorization is the process of ensuring an authenticated party is allowed to perform the action they request.

4
Accountability is keeping records of all actions performed by the authorized parties.

5
A reference monitor is the component in the access control process that control the interaction between subjects and objects

6
Trust anchor is an entity from which trust is assumed, not derived.

7
A trusted computing base of a computing system is all the hardware, firmware, and software or combinations of these protection mechanisms that is responsible for enforcing computer security policies

8
A HMAC is a message authentication code that involves a hash function and a secret key, used to verify both the integrity and the authenticity of a message.

9
Mutual authentication is the process in which both parties of a communication authenticate itself.

10
Zero-Knowledge Proof is the method by which one proves the knowledge about a piece of information without revealing the information itself.

11
- Discretionary Access Control (DAC)

- Mandatory Access Control (MAC)

- Role-Based Access Control (RBAC)

- Rule-Based Access Control (RBAC)

12
That means a reference monitor is designed to be:

- Non-bypassable: There is no way to get around it

- Evaluable: No hidden aspects, can be proven to be secure if it's deployed and we can make sure that it's working properly while it's deployed.

- Always-invoked

- Tamper-proof

13
- MAC prevents divulging of information that can be resulted from a user that gives worldwide read permission to confidential information

- MAC prevents polution of trusted information that can be resulted from a user writing to trusted information.

- MAC ensures that permissions is assigned by trusted parties and ensure the least privilege principle, in which a party is given only the permissions that it requires to complete its assigned tasks.


14
Higher EAL means higher cost and complexity in an evaluation effor and doesn't measure security.

15
- Similarity: They are both information flow models.

- Bell-LaPadula serves confidentiality while Biba serves integrity

- BLP prevents the divulging of secret information while Biba prevents the polution of trusted information

- The properties of BLP and Biba are the opposite of each other. In BLP, no reading is allowed from objects of higher clearance and no writing is allowed to objects of lower clearance. In Biba, no writing is allowed to objects of higher integrity and no reading is allowed from objects of lower integrity.



16
- CBC-MAC is done with symmetric cryptography and does not involve hashing. CBC-MAC should be used for fixed-length messages because it is based on block ciphers.

- HMAC is usually done using symmetric cryptography and involes hashing. It can be used to verify messages from clients, the key is known to a server.

- Digital signature is done using asymmetric cryptography and may involve hashing. digital signature is used in two-way transactions like email.


17
- Shannon theorem indicates that the entropy of a plaintext doesn't change given the knowledge of the ciphertext.

- This is based on the concept of confusion and diffusion and the AES encryption has stages to apply this: the substitute bytes stage providing confusion and shifting rows and columns providing diffusions.

18
We should use two key pairs to prevent a forgery attack and to provide extra security in case one key pair is compromised.

The forgery attack can be explained as following:

Charlie intercepts a ciphertext encrypted using Bob's public key: C = Enc(M, Pu_B) = M ^ Pu_B (mod n)

Charlie then requests Bob to sign the message C with Bob's private key of the same key pair: S = C ^ Pr_B (mod n) = ( (M ^ Pu_B) ) ^ Pr_B (mod n) = M

Therefore, Charlie successfully retrieves the message M.


19
Key clustering is different keys that can cause the same ciphertext from a plaintext.

This is similar to hashing in the sense that it produces the same output for the same input.

However, since hashing is usually used to serve integrity while encryption is used to serve confidentiality, this result is considered good for hashing but bad for encryption. It is bad for encryption because it reduces the average amount of keys that an attacker needs to try in a bruteforce attack.


20
The file tester itself is a second preimage attack because we give them knowledge to a message (the file) and the hash (which they can compute from the file), finding a different message that results in the same hash is the second preimage attack



21
- The command can be used for a confused deupty attack if the new copy of the files is modified then being used with the permissions of the original files.

- This is different from renaming the inode because it changes the entry in a directory, which consists of a mapping of name to inode and has nothing to do with permissions. the data from an inode remains the same