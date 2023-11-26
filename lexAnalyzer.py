# import sys

# s = sys.stdin.read()
# print(s)

import sys

# inputlist = sys.stdin.readlines()
arr = []
con = True
while con:
    line = sys.stdin.readline().rstrip('\n')
    if line == "kthxbye":
        con = False
        arr.append(line)
        break
    arr.append(line)

print(arr)




# while run:
#         # loop through each line of user input, adding it to buffer
#         for line in sys.stdin.readlines():
#             if line == 'quit\n':
#                 run = False
#             else:
#                 buffer.append(line.replace('\n',''))