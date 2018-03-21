# Linux File System

- Copy-On-Write (CoW) filesystem
- Kernel is the middle layer between the hardware and the software
- Primary partition
  - MBR: usually contains the partition table
    - Limit: < 2TB, 4 Primary partitions (actually 3, 1 is an extended)
    - Logical:
      - SATA: max 32 logical
      - SCSI: max 16 logical
    - Protocols for read-write operations: IDE, SATA, SCSI
  - GPT:
    - max 128 logical partitions
    - Support drives > 2TB, up to ZB
    - Has an automatical copy of the partition table
    - In 2020, the legacy BIOS will not be used by IBM, gone in x64 OSes, replaced by UEFI
  
## Filesystem Hierarchy Standard

* Notes on the finals:
  
  - `stat` command
  - `ls` command
  - `chown`
  - `chmod`
  - Permission in Discretionary Access Control
  - Questions related to output of `ls` command