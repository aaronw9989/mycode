#!/usr/bin/env python3

proto = ["ssh", "http", "https"]

protoa = ["ssh", "http", "https"]

print(proto)

proto.append("dns") # this line will add "dns" to the end of our list

protoa.append("dns") # this line will add "dns" to the end of our list

print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

proto.extend(proto2) # pass proto2 as an argument to the extend method

print(proto)

protoa.append(proto2) # pass proto2 as an argument to the append method

print(protoa)

############ CHALLENGE SECTION ##################
#################################################
print() # print a blank line
print("Challenge Section\n")

# reverse the protoa list in place
protoa.reverse()

# print protoa
print(f'Reverse the list {protoa}')

# sort the nested list of numbers in protoa
protoa[0].sort()

# print protao and show sorted numbers
print(f'Sort the nested list {protoa}')

# reverse sort the nested list 
protoa[0].sort(reverse=True)

# display the reversed list
print(f'Reverse sort of nested list {protoa}')

# pop off the last item in our list and place in list2
list2 = protoa.pop()

print(f'Pop of an item {list2}')

print(f'List after using pop {protoa}')





