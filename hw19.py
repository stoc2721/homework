from stack import Stack
def div_by_two(dec_num):
    s = Stack()
    bin_num=''
    while dec_num>0:
        remainder=dec_num%2
        dec_num=dec_num//2
        s.push(remainder)
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num
print(div_by_two(256))



def rev_string(input_str):
    s=Stack()
    index=0
    while index in range(len(input_str)):
        s.push(input_str[index])
        index+=1
    rev_str=''
    while not s.is_empty():
        rev_str+=s.pop()
    return rev_str
print(rev_string('YOB'))




def is_match(p1,p2):
    if p1 =='(' and p2 == ')':
        return true
    elif p1 =='{' and p2 == '}':
        return true
    elif p1 =='[' and p2 == ']':
        return true
    else:
        return False


def is_paren_balanced(p_string):
    index = 0
    is_balanced = True
    s = Stack()
    if p_string == '':
        is_balanced=False
        return False
    elif p_string[-1]in'({[':
        is_balanced=False
        return False
    else:
        while index<len(p_string) and is_balanced==True:
            if p_string[index] in '({[':
                s.push(p_string[index])
            else:
                if s.is_empty():
                    is_balanced=False
                    return False
                elif is_match(s.pop(),p_string[index]):
                    is_balanced=True
                else:
                    is_balanced=False
                    return False
            index+=1
    if s.is_empty() and is_balanced==True:
        return True
print(is_paren_balanced('[]'))
print(is_paren_balanced(''))
print(is_paren_balanced('[('))
