# Week 3

## Risk, Threat Modeling

### Breaches

- Reasons to be a target:
    - 

### Threat Actors

- Threat Taxonomy
    - access: Who has access? Outsiders, Insiders
    - intent: malicious/non-malicious, what resources are being targeted
    - objectives: tactical, particular goals
    - skills:
    - resources: Given enough resources, anyone may get in.
    - motivation: why do this?
    - limits: things that attackers can't do
    - impacts: what damage can the attacker cause?
    - visibility: how visible is the threat actor?
    - ...
- Even security researchers are threat actors, but with non-malicious intents.
- Motivation: CIA's MICE and RASCLS
    - Ideologically motivated: Hacktivist, Whistle-blowers, nation-state attackers, terrosists
    - Cognitive dissonance
- External Threat Actors
    - Organized crime: syndicates, mafias; as-a-Service model (ransomwares, DDoS) is unique to the cyber crime
    - Terrorists: shutdown critical systems, destroy systems, cause life-threatening problems
        - Example: WannaCry vs. hospitals
    - Gov: involved in all of the above more or less.
    - The competition
    - Hired guns
    - Hacktivists
- Internal Threat Actors:
    - Disgruntled employees
    - Clueless employees: Ignorance, clicks on every links
    - Customers: Obtain information about other customers, alter prices
    - Suppliers: Customer requirements put product at risks
    - Vendors
    - Business partners
    - Contractors, consultants:
        - disclose informations at security conferences that violates NDAs.
        - Need a lot of policies to manage.
        - become a target, entrypoint, pivot point to interesting targets

### Sophistication

- Relative to sophistication of defenders
- Tiers: Basic, Intermediate, Advanced
    - Technical or Security Maturity: 2FA
- Defensive products towards basic defenders
- Risks vs. Rewards

### Attack (Opportunity + Motivation) Vectors

- Social Engineering
- DoS
- Injection
- Session theft
- Phreaking
- Misconfig
- Physical

There are points of exposure that allow these attack vectors to take place.

- Who do what depends on the threat actors.

- Example: Weak ciphers, TLS 1.0
    - Enable MITM attack: sysadmins, ISP, nation-state...
    - Need high-privileged access in the network.

### STRIDE threat model

- To ID malicious actions in the environment => Plan to defend accordingly
- Threats != Goals
- Ransomware as DoS? not really clear

#### STRIDE

- Repudiation: Voting for example, needs both non-repudiation and anonimity.
- DoS: Non-malicious intent also (stripping on cable, too many people access a website for free stuffs, )

### Detection

- Logs
- Patch level
- Tripwire
- Categorization of controls: Administrative, Technical, Physical
    - Directive
    - Deterrent
    - Preventive
    - Detective
    - Compensating:
    - Recovery: Bring to original operational state
    - Corrective: Bring to a safe state
- New categorization: NIST framework

## Security Controls and Risk

- Risk(Event, Asset) = P(Event) * Cost(A)
- Security controls => reduce / elimiate risks
- Risk management: Develop policies to reduce, eliminate, transfer, accept risks

## Lab 1

### Data collection