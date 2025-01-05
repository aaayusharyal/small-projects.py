import math as m
print("A quadratic equation is in the form ax^2 + bx + c")
a, b, c = map(int, input("Enter the values of a, b and c: ").split())
if a == 0:
    print("The equation is linear, please enter the value of a > 0!!")
else:
    discriminant = b*b - 4*a*c
    if discriminant > 0:
        dis = m.sqrt(discriminant)  
        root1 = (-b + dis) / (2 * a)
        root2 = (-b - dis) / (2 * a)
        print("The roots of the given quadratic equation are", root1, "and", root2)
    elif discriminant == 0:
        root1 = -b / (2 * a)
        print("There is one real root:", root1)
    else:
        realpart = -b / (2 * a)
        imaginarypart = m.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex: {realpart} + {imaginarypart}i and {realpart} - {imaginarypart}i")
