import random

def battle():
    random1 = random.randrange(217, 256)
    level = int(input("what level do you want: "))
    print("your levels is", level,"on your pokemon")

    critical = int(input("what critical hits do you want: "))
    print("your critical his is ", critical,"on your pokemon")

    A = int(input("what attack power do you want: "))
    print("your attack power is", A,"on your pokemon")

    D = int(input("what defense level do you want: "))
    print("your defense is" , D ,"on your pokemon")

    type1 = int(input("what type effectiveness do you want: "))
    print("your effectiveness is", type1,"on your pokemon")

    type2 = int(input("what second type of effectiveness do you want: "))
    print("your second type of effectiveness is", type2 ,"on your pokemon")

    power = int(input("what power level do you want: "))
    print("your  power level is", type2 ,"on your pokemon")

    stab = int(input("what stab/bonus attck  do you want: "))
    print("your stab is", stab ,"on your pokemon")

    damage = (((2*level*critical/5 + 2)*power*A/D / 50 +2)*stab*type1*type2*random1)

    print(damage)

while(1):
    battle()
