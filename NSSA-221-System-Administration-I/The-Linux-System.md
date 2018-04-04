# The Linux System

## System Architecture

- Kernel space:
  - Manages the hardware.
  - Shell acts between the user and the kernel.
  - In windows, drivers tell the OS what a piece of hardware is capable of.
  - In linux, it's kernel modules.
- Libraries:
  - Allow processes to add more features
  - Shared
  - Shell and processes are dependent on libraries
  - Libraries makes signals and syscalls
- Syscalls:
  - Interacts with the kernel

## Kernel

- CPU
- RAM
- Network

## /dev Directory

- /dev/scsi
- /dev/sda:
  - Major number => driver for all the devices.
  - Minor number => different modules for a specific device.

## glibc

## BIOS phase

- Read-only software, firmware on CMOS chip
- Figure out what type of hardware it needs to work with.

## BOOTLOADER phase

- Kernel is where pid=0 starts
- initrd creates pseudo filesystem so that the kernel can mounts itself on that to start building stuffs
- Load the OS from the storage into RAM

## Kernal phase

- Linux run levels
- init 0 to init 1

## Processes

- Program loaded from storage into RAM
- Is running

### Types

- Binary executables, /bin, /sbin
- Internal shell commands (not executable)
- Shell scripts executables run in shell environment.
===========
- 2 types:
  - Shell jobs (user)
  - Daemon (system)
- Swap memory:
  - tl;dr: windows sucks
- Bash and processes opened in the shell: parent-child relation
- Child processes that have the parent killed are called orphaned processes/zombie processes.
- SIGHUP:
  - Tell the process to go back and re-read the config files
- Fork: by kernel
- Exec: by system
- Threads are in brackets, developers' stuffs
- top wait time (wa): IO wait time
- load average should always be under the # of CPU (1 min < 5 min < 15 min usually)
- priority, niceness: rt: real time, 20: standard.