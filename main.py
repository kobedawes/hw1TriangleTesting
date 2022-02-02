def classify_triangle(a, b, c):

    if round((a ** 2), 0) + round((b ** 2), 0) == round((c ** 2), 0):
        return print('right')

    elif a == b == c == a:
        return print("equilateral")

    elif a != b != c != a:
        return print('scalene')

    else:
        return print('isosceles')


