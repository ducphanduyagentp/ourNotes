# Sleuthkit

## Midterm

- March 5th
- 50 multiple-choice questions

# Tools

- blkls -o 2048 linux-case.001 | strings -t d | grep "Assignments"
- fsstat => 4096 block size => Divide offset by block size
- ifind: Map block number to an inode number
- time
    - access: block access
    - modify: block change
    - change: inode change
- fls