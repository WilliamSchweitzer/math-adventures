# Modular multiplication

"""
 I AM DEFINING ALL MY OWN FUNCTIONS FOR PRACTICE.

 NOTES:
 Division is held til after modular inverserse are considered
 Example: 14 * 16 = 224
 In modular arithmetic, (14 * 16) mod 19 = 15

 Or: (14 * 16) / 19, then take remainder = 15

 So modular multiplation can be written as:
  (x * y) mod p = result
  or:
  (x * y) then take the remainder, divided by p = result
  
  Basically, any amount of multiplications and modular operations
  may result in the same result as long as the modulus p is the same.
"""

def multiply(x, y):
 result = x * y
 print(str(x) + ' * ' + str(y) + ' = ' + str(result))
 return result

def remainder(x, y):
 result = x % y
 print(str(x) + ' % ' + str(y) + ' = ' + str(result))
 return result


m_res = multiply(14, 16)
remainder(m_res, 19)

# todo: write function to take mod
