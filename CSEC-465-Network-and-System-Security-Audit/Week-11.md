# Week 11

## Lab 5, vuln scanning

## Windows (cont.)

- svchost.exe, sc query => service info
- sc sdshow fac => WD => world-writeable, A => All
- lanmanworkstation => smb client
- lanmanserver => smb server
- Stopping race condition, DNS reply in SMB
    - Sign the hash
    - SMBClient by default does not require signing: RequireSecuritySignature => 0
- rpcclient

## Linux

- Windows vs. Linux
    - Linux: Varied/Granular network services
    - Windows: More predictable
- SSH configs
- 

## Midterm

- Q4: Risk formula, why it's used: matrix vs formula, difficult to determine the exact number for the formula.
- Q5: to tell where the potential points of attack is and how the attack may happen, who the attackers may be, identifying the most valuable assets in the network that need protection.
- Q6: visual representation of a kill chain, used to model likely attackers behaviors, showing different classes of threat actors.
- Q9: strategic information, possible cost, what's the high level impact, what to do to mitigate these, estimated time to fix.
- Q10: points of contact, schedule, checklist, entrance meeting
- Q12:
    - EISP: 
    - ISSP: Personal devices must be registered on the guest network. Client data must not be moved to personal devices.
    - SSSP: Android devices must be version 8.0 or above. Windows devices must be windows 7 or above. Laptop must have antivirus installed.