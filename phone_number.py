def create_phone_number(n):
    # phone_number = []
    # phone_number.append("(")
    # phone_number.append(n[0:3])
    # phone_number.append(")")
    # phone_number.append(" ")
    # phone_number.append(n[3:6])
    # phone_number.append("-")
    # phone_number.append(n[6:10])
    digits = ' '.join(str(e) for e in n[0:3])
    print(digits)
    
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])