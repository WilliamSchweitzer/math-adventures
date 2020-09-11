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

print('Modular addition/subtraction test case, subtraction works the same way -> works for any amount of additions/subtractions & any amount of mods')
print('Example (((a+b+c) mod m) + d) mod m)') 
print('x=14, y=16, mod=19, x + y == result == 30/19 == 11, 30 mod 19 == 11')
print('___________________________________________________________________')

modular_add(14,16,19)

print('Test case: result < mod, 1+7 mod 19 = 11')

modular_add(1,7,19)

# Given a number m outside of our range we divide by mod p -> m mod p
# IMPORTANT -> Congruence operator denotes equivalence in mod arithmetic, if difference is multiple of 3

def check_congruence(x1, m1, x2, m2):
 try:
  if m1 != m2:
   print('Mod values are not equal!')

  first_value = modular_add(int(x1),0,int(m1))
  second_value = modular_add(int(x2),0,int(m2))
  print('Always true if mod is the same')
 except:
  print('Mod value may not have been the same?')

print('Test case: x1=7, x2=10 m1,m2=3')
check_congruence(7, 3, 10, 3)

print('Test case: m1,m2 are different')
check_congruence(7, 3, 10, 4)
