# Linux/Unix

## MBR

- Use only 1 block

## GPT

- GUID

## Disk structure

- View superblock
- `sudo fsstat /dev/sda` => Cannot determine file system type
- `sudo mmls /dev/sda` => offset 2048
- `sudo fsstat -o 2048 /dev/sda`
- `sudo mmls /dev/sda1` => Cannot determine partition type
- offset is in byte
- `istat /dev/sda1 <inode>`: Where to find the data block

## Files deletion

## Lab

- fsstat linux-case.001 => don't know system type
- mmls linux-case.001  => partition Start column, 2048
- fsstat -o 2048 linux-case.001
- ils -o 2048 -m linux-case.001
- mactime