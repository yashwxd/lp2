n = int(input("Enter modulo(n): "))
g = int(input("Enter primitive root of {}: ".format(n)))
X_a = int(input("Choose first secret number(Alice): X_a "))
X_b = int(input("Choose first secret number(Alice): X_b "))

Y_a, Y_b = pow(g, X_a, n), pow(g, X_b, n)
K_A, K_B = pow(Y_b, X_a, n), pow(Y_a, X_b, n)

print("They share a secret key for User-A is =", K_A)
print("They share a secret key for User-B is =", K_B)

if K_A == K_B:
    print("Alice and Bob can communicate")
    print("They share secret no.:", K_B)
else:
    print("Alice and Bob cannot communicate")

