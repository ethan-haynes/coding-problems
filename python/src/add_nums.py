def add(a,b):
    if a == b: return int('{_bin}0'.format(_bin=format(a,'b')),2)

    l_a, l_b = len(format(a,'b')), len(format(b,'b')) 
    bin_a, bin_b = f'{a:0{l_b}b}', f'{b:0{l_a}b}' # to make them equal length
    
    out, carry = '', {'should_carry': None}

    for i in range(len(bin_a), -1, -1): # starting from the back
        if i == len(bin_a): continue # since we can't use - operator
        
        if bin_a[i] == '1':
            if bin_b[i] == '1':
                if carry['should_carry'] == False: carry['should_carry'] = True
                num = '0'
                if carry['should_carry'] == None:
                    carry['should_carry'] = True
            else: num = '0' if carry['should_carry'] else '1'
        else:
            if bin_b[i] == '1': num = '0' if carry['should_carry'] else '1'
            else: 
                if carry['should_carry']:
                    num = '1'
                    carry['should_carry'] = False
                else:
                    num = '0'
        
        out = f'{num}{out}'

    return int(f'1{out}',2) if carry['should_carry'] else int(out,2)

print(add(3,4))
print(add(24,12))
print(add(1,9))
print(add(15,1))
