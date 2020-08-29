"""
Congruence: 
 - If (a-b)/m "M must be a number"
 - "Say, B is congruent to C with moduus M" - OR [ b "triple bar" c (mod m) ]
"""

"""
Modular Multiplicative Inverse:
 - a * x is congruent to 1, and only has 1 modulus m
 - x is simply a^-1
"""

"""
 - Find the modular inverse using the Extended Eucidean algorithm "EEA"
 - EEA is a * x + m * y = 1 , where 1 is the gcd(a,b), 
 or in our case gcd(a,m) = 1. Meaning a and m are relativly prime or coprime. 
 - IMPORTANT ` ***** "gcd(a,m)=1 is also the condition for the modular inverse to exist." *****
 - An equation of the above form is know as a Linear Diophantine Equation "LDA" 
 - LDA is an equation with format -> "ax + by = c"

"""
 

if __name__ == '__main__':
 print('working')
