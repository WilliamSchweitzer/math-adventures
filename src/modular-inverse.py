"""
NOTES
-----
Congruence: 
 - If (a-b)/m "M must be a number"
 - "Say, B is congruent to C with moduus M" - OR [ b "triple bar" c (mod m) ]

Modular Multiplicative Inverse:
 - Equation without both sides modded, a * x + m * y = 1
 - Constraint:  GCD(a,m) = 1
 - GOAL: FIND 'x', the modular multiplictive inverse of 'a'
 - a * x is congruent to 1, and only has 1 modulus m
 - x is simply a^-1

 - Find the modular inverse using the Extended Eucidean algorithm "EEA"
 - EEA is a * x + m * y = 1 , where 1 is the gcd(a,b), 
 or in our case gcd(a,m) = 1. Meaning a and m are relativly prime or coprime. 
 - IMPORTANT ` ***** "gcd(a,m)=1 is also the condition for the modular inverse to exist." *****
 - An equation of the above form is know as a Linear Diophantine Equation "LDA" 
 - LDA is an equation with format -> "ax + by = c"
"""

# This program was not written to be secure. It was written for specific inputs.
# Recursion seems to be an efficient way to solve this problem.
# Program solves for 

if __name__ == '__main__':
 print('This program assumes the given input is two coprime numbers.')
 print('Input first coprime number "a" (then press enter)... ')
 a = int(input())
 print('Input second coprime number "m" (then press enter)... ')
 m = int(input())
 given_a = a

 remainder = -1
 equations = []

# Euclidean Algorithm
 while remainder != 1:
  dividend = a
  divisor = m
  quotient = a // m
  remainder = a % m

  print('dividend <-- divisor(quotient) <-- remainder')
  print(str(dividend) + ' <-- ' + str(divisor) + '(' + str(quotient) + ')' + '<--' + str(remainder))
  input()

  equations.append([divisor, dividend, quotient, remainder])

  m = remainder
  a = divisor 

 print('Nice job! You entered valid input!')
 print(equations)

 eea_result = {}

for equation in reversed(equations):
 try:
  eea_result[equation[0]].append(1)
 except KeyError:
  eea_result[equation[0]] = [] 
  eea_result[equation[0]].append(1) 
 try:
  eea_result[equation[1]].append(1)
 except KeyError:
  eea_result[equation[1]] = []
  eea_result[equation[1]].append(1)
 try:
  eea_result[equation[2]].append(1)
 except KeyError:
  eea_result[equation[2]] = []
  eea_result[equation[2]].append(1)
 try:
  eea_result[equation[3]].append(1)
 except KeyError:
  eea_result[equation[3]] = []
  eea_result[equation[3]].append(1) 

 print(eea_result)

 print('----------')
 print('The Multiplicative Modular inverse is: ' + str(eea_result[given_a]))
