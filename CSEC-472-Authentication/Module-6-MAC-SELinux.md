# MAC and SELinux

## Lab

- `yum install -y policycoreutils-gui`
- `yum install -y setools setools-gui`
- `system-config-selinux`
- `checkmodule -M -m -o sample.mod sample.te`
- `semodule_package -o sample.pp -m sample.mod`

### Solution

- To be able to prevent some of the exploit, it is required that we write our own SELinux policies/rules/modules.
- Overwriting existing rules is really difficult. Uninstalling or disabling the apache selinux modules is not possible because of dependencies
- The high-level solution is to create a whole new domain with new types and label httpd as this new type. This new policy will be very strict and will block a lot of actions
- What are the important files of an SELinux policy
    - `.te`: Type enforcement file, contains type definitions and rules
    - `.fc`: File contexts, contains definitions of file types and directories
    - `.pp`: The compiled format of an SELinux policy, not human-readable. This is used to install the policy to the machine
- This make sense because SELinux doesn’t have explicit block rules and only have allow rules. In this way, we can gradually work out the whitelist that only allow DVWA to access resources that it needs and prevent the exploits.
    - Generate new SELinux policies: `sepolgen -n sometype --init /usr/sbin/httpd`
    - Modify the `.fc` to remove existing file contexts that have been defined in httpd
    - Modify the `.te` file to do the following
        - Add the file contexts that have been removed in .fc file that refer to existing httpd file contexts
        - Remove redundant rules so we can work out the whitelist from scratch
    - Install the new policy
- We can set SELinux to permissive mode so it logs blocked actions but won’t actually block it.
    - Turn on httpd, use DVWA as usual so it generate logs for normal activities that we want to allow httpd to perform.
    - Use `audit2allow` to generate allow rules to permit those actions

### SELinux command reference

- Audit log is in `/var/log/audit/audit.log`
- List modules: `semodule -l`
- Remove module: `semodule -r <module-name>`
- Disable module: `semodule -d <module-name>`
- Install module: `semodule -i <module-name>.pp`
- List booleans: `semanage boolean -l`
- Generate policy: `sepolgen`
- Compile .te to .pp
    - `checkmodule -M -m -o file.mod file.te`
    - `semodule_package -o file.pp -m file.mod`
- Create allow rules from audit log, for example httpd
    - `ausearch -c ‘httpd’ --raw | audit2allow -M allowmeplease`
- Search for allow rules that allow subject of type1 to act on object of type 2
    - `sesearch -A -s type1 -t type 2`
    - `sesearch -A -s type1 -t type2 -C`
- SELinux tools but in GUI
    - `system-config-selinux`
