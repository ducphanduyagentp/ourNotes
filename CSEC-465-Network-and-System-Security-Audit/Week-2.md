# Week 2

## Types of audit

- Checking policies against practice

- Technical
    - Pentesting: Not really effective. Companies are aware of some problems and just not fix it immediately, or it's an easy fix.
    - Vuln Assessment: one-shot exploits, often false positives, interesting vulns may require chaining exploits.
    - Source code analysis:  
- Non-technical
    - Policy
    - Procedural
    - Physicals
- Others

- Internals
- Externals

## Technical Models

- Blackbox
    - Simulate adversarial behaviors.
    - No knowledge of the system.
    - TTP: tools, tactics, procedures.
- Greybox
    - Some knowledge
- Whitebox
    - Complete knowledge

## Non-technical models - Lab 1

- Policy/Procedure Review
    - Evaluate company's standards
        - Make sense? w.r.t the followers
        - Follow industry expectations?
        - Clear?
- Policy/Procedure Compliance
    - Are they being followed?
    - Employee behaviors
    - System configurations

## Important steps

- Pre-engagement discussion
    - Way before the audit
    - To discuss types, goals, duration, scope (like Rules of Engagement), depth
    - statements of work, NDAs, contracts
    - Scope:
        - Exceeded authorization
        - (Usually) Scope out: known vulns, production servers, physical damages.
- Initial audit meeting
    - Stakeholders
    - Onsite
- Audit
- Audit report
    - Quantifiable metrics
    - Realistic recommendations and timelines

## Lab 1

- Building a threat model
- Deliverables:
    - Report:
        - Potential threats
        - Graphs
    - Dates: not before it dues
    - Pay attention to risks
    - High-level plan summary for actions: patch => patch program
    - 4 5 6 non-technical
    - 8: potential vulns, not actual vulns