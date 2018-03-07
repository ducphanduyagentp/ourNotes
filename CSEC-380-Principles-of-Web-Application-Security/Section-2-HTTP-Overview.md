# HTTP Overview

## HTTP RFC

## HTTP Overview

## HTTP Overview cont.

## Character Interpretation

## ASCII

## Unicode

- Unicode Consoritum: characters are more than 1 byte
- There are metadata for each character
- UTF: Unicode Transformation Format
- UTF-7, UTF-8, UTF-16, UTF-32
- Sizes:
  - 1 byte: standard ASCII
  - 2 bytes: Arabic, Hebrew
  - 3 bytes: Basic Multilingual plane
  - 4 bytes: All unicode
- 1 bit is not used in a byte => used to represent if there are more bytes coming
- **Unicode is the collect of all characters**

## Unicode Security

### Programming concerns

- Character and String data types
- Library support
- Counting characters
- Comparing for equality

### Security

- Visual spoofing, **Confusables**
  - IDNA: Internation Domain Name 2003, 2008, _Punycode_ converts Unicode URLs
  - Invisibles
    - Zero Width
    - Spaces
    - RTL
- 
`