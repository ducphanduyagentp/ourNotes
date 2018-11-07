# Week 10

## Auditing vs Vuln Scanning

- Vuln scanners often ignore misconfigurations
- Huge amount of traffic => DoS
- Often signature matching => False positive. Example: version number in the banner is incorrect
- PoC is run => clients may not want

## Finding Windows hosts on network

- Ports: 138, 139, 445, 3389
- nbtscan
- DC: ports 88, 389, 636, 3268, 3269

## Tasks

- Discover users using kerberos
- Discover users using net command
- Discover firewall rules
- WMI stuffs
    - wmic: https://www.sans.org/security-resources/sec560/windows_command_line_sheet_v1.pdf
    - https://www.andreafortuna.org/dfir/windows-command-line-cheatsheet-part-2-wmic/
    - msbuild: C# interpreter
- Windows Groups
    - Administrators
    - Hyper-V Local
    - Users
    - Remote Management users (WMI)

    - Domain Admins
    - Domain Users
    - Enterprise Admins (privileges across multiple admins)

    - Remote Desktop Users (Domain & Local)