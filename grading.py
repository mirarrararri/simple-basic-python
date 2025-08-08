sub1 = float(input("Enter your English Grade: "))
sub2 = float(input("Enter your Math Grade: "))
sub3 = float(input("Enter your Filipino Grae: "))
sub4 = float(input("Enter your Science Grade: "))
sub5 = float(input("Enter your Filipino Grade: "))
sub6 = float(input("Enter your ESP Grade: "))
sub7 = float(input("Enter your TLE Grade: "))
sub8 = float(input("Enter Your MAPEH Grade: "))

add = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8)
avg = (add/8)

if avg >= 95:
    print(f"Average: {avg}, With High Honor")
elif avg >= 90:
    print(f"Average: {avg}, With Honor")
elif avg >= 75:
    print(f"Average: {avg}, Passed")
else:
    print(f"Average: {avg}, Failed")