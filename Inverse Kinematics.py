import math
print("The {0} coordinates are assumed to be at origin")
x2 = float(input("Please enter the x-coordinate of end-effecto : "))
y2 = float(input("Please enter the y-coordinate of end-effector : "))
a1 = float(input("Please enter the length of the first link : "))
a2 = float(input("Please enter the length of the first link : "))
theta2 = math.acos(
    (pow(x2, 2) + pow(y2, 2) - pow(a1, 2) - pow(a2, 2)) / (2 * a1 * a2))
phi1 = math.atan2(y2, x2)
phi2 = math.atan2(a2 * math.sin(theta2), a1 + a2 * math.cos(theta2))
theta1 = phi1 - phi2
print("In Radians : ")
print("The first joint angle is {:.4f}".format(theta1))
print("The second joint angle is {:.4f}".format(theta2))
print("In Degrees : ")
print("The first joint angle is {:.4f}".format(math.degrees(theta1)))
print("The second joint angle is {:.4f}".format(math.degrees(theta2)))
