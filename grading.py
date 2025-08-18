#Input
sub1 = float(input("Enter your Grade in Filipino: "))
sub2 = float(input("Enter your  Grade in Math: "))
sub3 = float(input("Enter your  Grade in Filipino: "))
sub4 = float(input("Enter your  Grade in Science: "))
sub5 = float(input("Enter your  Grade in Filipino: "))
sub6 = float(input("Enter your  Grade in ESP: "))
sub7 = float(input("Enter your  Grade in TLE: "))
sub8 = float(input("Enter Your  Grade in MAPEH: "))

#Process
add = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8)
avg = (add/8)

#simplier(Process)
#avg = (sub1 + sub2 +sub3 + sub4 + sub5 + sub6 + sub7 + sub8)/8

#Output
if avg >= 95:
    print(f"Average: {avg}, With High Honor")
elif avg >= 90:
    print(f"Average: {avg}, With Honor")
elif avg >= 75:
    print(f"Average: {avg}, Passed")
else:
    print(f"Average: {avg}, Failed")


