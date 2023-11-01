def CPFchecker(cpf):
    cpf = str(cpf)
    regressive_counter1 = 10
    regressive_counter2 = 11
    list1 = []
    result_1 = 0
    result_2 = 0
    
    for digit in cpf:
        list1.append(int(digit))
        if regressive_counter1 > 1:
            result_1 += int(digit) * regressive_counter1
            regressive_counter1 -= 1
    
    digit1 = (result_1 * 10) % 11
    digit1 = digit1 if digit1 < 10 else 0
    list1 = []

    for digit in cpf:
        
        list1.append(int(digit))
        if regressive_counter2 > 1:
            result_2 += int(digit) * regressive_counter2
            regressive_counter2 -= 1
    
    digit2 = (result_2 * 10) % 11
    digit2 = digit2 if digit2 < 10 else 0
    
    if digit1 == list1[9] and digit2 == list1[10]:
        return False
    else:
        return True



