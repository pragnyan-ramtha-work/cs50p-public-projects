rate = 50
paid = 0



while paid < 50:
    ins = int(input("Insert coin: "))
    if ins == 25:
        paid = paid +25
    elif ins == 10:
        paid = paid +10
    elif ins == 5:
        paid = paid +5
    else:
        pass
    amtd = rate - paid
    if amtd > 0:
        print("Amount Due:",amtd )
    elif amtd <= 0:
        print("Change Owed:",-amtd )
