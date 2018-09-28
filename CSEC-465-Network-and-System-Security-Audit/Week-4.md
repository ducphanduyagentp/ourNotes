# Week 4

## Risk

### Calculating Risk

- Risk = Probability x Cost
    - Risk acceptance: Explicit written.
- Risk Matrix
    - Should be used consistently to make decisions

### Concepts in Evaluating Risks

- Security Perimeter
    - Boundary between systems: Host vs network, between networks
- Attack surface
    - All the potential points of attack
        - Not limited to application in OSI model
        - OS
        - Network stack
        - Physical
        - anything the systems rely on.

## Auditing
- Repeatable: needs to compare audit results at 2 different times.
- Methodical examination and review of measuring something against a standard
- Metrics:
    - \# Physical Attack surfaces
    - \# Security exploitability: CVSS score
    - \# Administrative control: \# people do/don't security training, \# admins in the infrastructure
- Example:
    - Conformance
    - Security
    - Financial

### Auditing vs. Assessing
- Auditing:
    - Objective measurement
    - Typically includes assessing
- Assessing:
    - Subjective measurement

### Levels of Auditing
- Policy: Does it do what the organization wants to do? Does it make sense/make the organization more secure?
- Procedure: 
- System/Application: 

## Policy
- Influences actions    
    - Administrative control
- Policies efficiency
    - Disseminated
    - Read
    - Understood
    - Agrred-to
    - Uniformly enforced
        - Exception process
- Constant modification and maintenance

### Policy vs. Procedure
- Policy: What and why users can/can't do/have.
- Procedure: Who does what when and where, mechanism making sure policies are enforced

### Policy Example
- All user passwords must be changed every 6 months
- Password must be x-character long, y types of character.

### Procedure
- The admin will block people that don't change password after 6 months
- The admin use technology X to verify strength of passwords

### Types of policices
- Enterprise Infosec program policies
    - Strategic
    - High-level
    - Example: Resnet is managed separatedly from campus network
    - Starting point, general but have impacts on low-level policies
    - Elements
        - Overview of security philosophy
        - Information about security orgs and roles
            - Responsibilities of shared roles
            - Responsibilities of special roles: admins
    - Examples:
        - Statement of purpose: pretty much like the policies
        - Elements:
            - Security relative to policies
                - People need to understand it.
            - Content of Policies:
                - What is admin credentials?
        - Justification
            - Why need these policies?
            - Non-technical
        - Identify responsibilities and roles
            - 1 group of Stakeholders
            - Not the only group who enforcing these policies
            - Who impacted, affected, enforce?
        - Strategic goals
- Issues-specific
    - Detailed, specific guidance
        - How to encrypt data? What software? What algorithm?
    - Directive control, telling people to do something
    - Justification
        - Why use this but not that? Both technical and high-level explanation
    - Often protects the organization from **liability**
        - Documenting the investigation processes
    - Typically not technical enforced
    - Elaborate on EISP
- System-specific
    - Highly technical
    - Implementations
        - ACL
            - Harder if there is overlapping groups of users
            - Prevent potential conflicts of interests
        - Configuration rules
    - Talk about specific technology, really technical.
    - Where on the system?
        - Example: MySQL
            - MySQL ==> SELinux ==> fp

## Lab 2

- Stakeholders: Identify stakeholders in particular parts
- Policy Statement: **very high level** policy statements
- Auditing: Plan auditing based on the written policy: who will audit this policy
- Maintenance process: who update it
- Amount: each group member => 6 policies
- Network is the same as lab 1
- Appendix may be used for assumptions