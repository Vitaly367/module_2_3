first = 3090
second = 3092
third = 3091
if (first == second == third):
    print(3)
elif (first == second) or (first == third) or (second == third):
    print(2)
else:
    print(0)