# pdb is inbuilt python debugger
# What is Debugging?
# Finding the error
a = input()
b = input()
breakpoint()
def sumation_of_numbers(a,b):
    print("We are inside the function")
    print(int(a)+int(b))

sumation_of_numbers(a,b)

# PDB interactive console will appear whenever it sees 
# a breakpoint()
# c(continue) -> continues all the leftover code whereever we are
# n(next) -> It runs the next piece of code
# s(step inside) -> to step inside the function such that enter will
# work like showing us the next line executing
# WE CAN ALSO USE PRINT IN PDB COSOLE
# WE CAN KNOW THE DATA TYPE OF THE VARIABLE AS WELL
# INSIDE THE PDB CONSOLE