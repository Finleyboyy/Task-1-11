length = float(input("What is the length of the rectangle?:\n"))
width = float(input("What is the width of the rectangle?:\n"))

# Formula for perimeter of a rectangle: P = 2 × (length + width)
perimeter = 2 * (length + width)

# Formula for area of a rectangle: A = length × width
area = length * width

print(f'The perimeter of the rectangle is {perimeter:.3f} and the area is {area:.3f}')
