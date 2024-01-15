def is_valid_triangle(angle1, angle2, angle3):
    """
    Check if the given angles can form a valid triangle.

    Args:
    angle1, angle2, angle3 (float): Angles of the triangle.

    Returns:
    bool: True if a valid triangle is possible, False otherwise.
    """
    # Check if the sum of angles is 180 degrees and each angle is greater than 0
    return angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0

def main():
    # Input angles from the user
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))
    angle3 = float(input("Enter the third angle: "))

    # Check if a triangle is possible
    if is_valid_triangle(angle1, angle2, angle3):
        print("A triangle with positive area is possible.")
    else:
        print("A triangle with positive area is not possible.")

if __name__ == "__main__":
    main()
