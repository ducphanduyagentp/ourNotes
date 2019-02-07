# Trust and Security Models

- What do you need to trust?

## Trust modeling

- Trust anchor
    - Trust is assumed on this entity, not derived
- Models:
    - Monopoly: 1 trust anchor
    - Oligarchy: multiple, independent trust anchors
    - Anarchy: Everyone is a trust anchor
        - Example: GPG
        - Users make decisions
- Objects of trust
    - Theoretical: crypto algos
    - Design and architectures
    - Implementations: Software/System
- Trust but verify
    - Theoretical, algorithms: Verified through formal proofs
    - Design and architecture: audit
    - Implementation: testing and auditing
- Measure of effectiveness/performance
- Trusted Computing Base
- TCSEC - Orange book

## Windows Kernel Security

- DLL
- JIT compiler

### DLLs

- takeown
- cacls
- regsvr32

### Components

- Windows Internals part 1 v7.0 (2018), p610
    - p629, Chapter 7: Security

## Orange book assurance

- Separation Kernels
    - Bell-LaPadula model
    - MILS
- Designing the reference monitor: NEAT
    - Non-bypassable: Can't get around
    - Evaluable: 
    - Always-invoked: Can't be turned off?
    - Tamper-proof: 
- The reference monitor is trustworthy if the design is certified.
- Certified using Common Criteria
    - Target of Evaluation (TOE)
    - Protection Profile (PP): Preconditions and postconditions
    - Security Targets
    - Security Functional Requirements
    - Security Assurance Requirements
    - Evaluation Assurance Level: Rating, how well can detect PP
        - Higher EAL != Higher security
- Common Criteria Process
- Evaluation Assurance Levels
    - 7 levels
- Where to trust
    - TCSEC

## Security and Integrity Models

- Non-interference model: Clark-wilson
- Bell-LaPadula (BLP):
    - No read up: S reads O iff L(O) <= L(S)
    - No write down: S writes O iff L(S) <= L(O)
    - Simple Security Condition
    - *-Property
    - All about confidentiality: Can get information anywhere to include in classified work
- Biba:
    - About Integrity
    - preventing unauthorized writing
    - inverse of BLP
    - Integrity(O) = min(Integrity(O_i))
    - If there is at least 1 thing included but untrusted, the whole this is untrusted
    - No read down: S reads O iff I(O) >= I(S)
    - No write up: S writes O iff I(O) <= I(S)
- Clark-wilson
    - Developed after Biba
    - Components:
        - Subjects
        - Transactions
    - Data items:
        - Constrained: through integrity verification procedure
        - Unconstrained: no IVP
    - Transactions are predefined sequences of operations on data items
    - 9 rules of 2 types:
        - Certification rules
        - Enforcement rules
- Graham-Denning
- Harrison-Ruzzo-Ullman
    - Extend Graham-Denning
    - Add more rules to a protection system
    - Still a finite set of commands

## Multilateral Security (MLS)

- Need-to-know
- Compartments associated with each piece of details

## Aside on US Data Classification

## Chinese Wall Security Policy

- DFC. Brewer and MJ. Nash
- Conflict of Interest

## Formal modeling

- About relational logic, mathematical model
- BLP:
    - Subject(X)
    - Object(X)
    - L(X) = classification level of X
    - has(x, y, z) = X has permission Y on object Z
    - for all s, o