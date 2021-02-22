# Weight: 160
# (L)bs or (K)g: l
# You are 72.0 kilos

weight = int(input("Weight: "))
scale = input("(L)bs or (K)g: ")

if scale.upper() == "L":
    conversion = weight * 0.45
    print(f"You are: {conversion} kilos")
elif scale.upper() == "K":
    conversion = weight / 0.45
    print(f"Your are: {conversion} pounds")
