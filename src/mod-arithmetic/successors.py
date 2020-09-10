"""

1. How to count in mod arithmetic 
2. mod arithmetic is foundational to public key crypto systems

Some names to know:
    Diffie-Hellman Key Exchange
    RSA Authentiation and Signing
    DSS Digital Signaure standard
    ElGamal Encryption
    ECC - Ellipic Curve cryptosystems

In mod arithmetic: There is a last number, that is one less than a number called a modulus.
"""

def count_up_from_zero_on_paper(x):
 for i in range(0, int(x)+1):
  print(i)

print('Count on paper -> limit=10')
print('_________________________')

count_up_from_zero_on_paper(10)

print('All number modulo a number -> mod=6')
print('___________________________')

def count_up_from_zero_modulus(m):
 for i in range(0,  m):
  print(i)

count_up_from_zero_modulus(6)

# Modular addition and subtraction below

def modular_add(x, y, mod):
 result = int(x) + int(y)
 if result > mod:
  print(result-mod)
 elif result < mod:
  print(mod - result)
 else:
  print(0)

print('Modular addition/subtraction test case')
print('x=14, y=16, mod=19, x + y == result == 30/19 == 11, 30 mod 19 == 11')
print('___________________________________________________________________')

modular_add(14,16,19)



