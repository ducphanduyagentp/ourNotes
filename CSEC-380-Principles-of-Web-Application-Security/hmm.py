from base64 import b64encode, b64decode
import getpass
import sys

def xor(s1, s2):
  return b64encode(''.join([chr(ord(a) ^ ord(b)) for (a, b) in zip(s1, s2)]))

def dec(c, k):
  c = b64decode(c)
  c = xor(c, (k * len(c))[:len(c)])
  c = b64decode(c)
  c = b64decode(c)
  return c.decode('hex')

def enc(p, k):
  p = p.encode('hex')
  p = b64encode(p)
  p = b64encode(p)
  p = xor(p, (k * len(p))[:len(p)])
  p = b64encode(p)
  return p

def main():
  if len(sys.argv) != 3:
    exit(1)
  filename = sys.argv[2]
  mode = sys.argv[1]

  data = open(filename).read().strip('\r\n')
  k = getpass.getpass("Password: ")
  if mode == 'enc':
    print enc(data, k)
  elif mode == 'dec':
    print dec(data, k)  

if __name__ == '__main__':
  main()