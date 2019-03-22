import copy
def memory_addr(var):
    return hex(id(var))
dict1={'Jack':{'Python':'Proficient','C++':'Fair'},'Mike':'C++'}
dict2=copy.deepcopy(dict1)
print(dict1)
print(memory_addr(dict1))
print(dict2)
print(memory_addr(dict2))
dict2['Jack']['C++']='Proficient'
print(dict1)
print(memory_addr(dict1))
print(dict2)
print(memory_addr(dict2))

