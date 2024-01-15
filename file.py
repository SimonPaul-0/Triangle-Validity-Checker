def is_triangle_possible(angle1, angle2, angle3):
    # Check if the sum of angles is 180 degrees
    total_angle = angle1 + angle2 + angle3
    if total_angle == 180:
        # Check if each angle is greater than 0
        if angle1 > 0 and angle2 > 0 and angle3 > 0:
            return True
        else:
            return False
    else:
        return False

# Input angles from the user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check if a triangle is possible
if is_triangle_possible(angle1, angle2, angle3):
    print("A triangle with positive area is possible.")
else:
    print("A triangle with positive area is not possible.")
