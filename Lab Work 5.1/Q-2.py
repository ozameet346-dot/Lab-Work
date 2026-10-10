Number=int(input("how many numbers do you want to enter :"))

Num=[]


for i in range (Number):
    num=int(input(f"enter number {i+1}:"))

    Num.append(num)


maxNumber=min(Num)

minNumber=max(Num)


print("max number", maxNumber)

print("min number", minNumber)