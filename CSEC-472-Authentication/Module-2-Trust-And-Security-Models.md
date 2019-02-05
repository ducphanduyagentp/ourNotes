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
- Security and Integrity Models
    - Non-interference model: Clark-wilson
    - Bell-LaPadula:
        - No read up: S reads O iff L(O) <= L(S)
        - No write down: S writes O iff L(S) <= L(O)