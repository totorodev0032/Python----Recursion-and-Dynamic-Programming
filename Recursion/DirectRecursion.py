# Recursion is a process of repeating a procedure.
# In computer science, recursion refers to a function calling itself directly or indirectly.


## DIRECT RECURSION
# Direct Recursion occurs when a func calls itself directly in its body or definition.

###### Example #########

def func(str, n):
    if n > 0:
        print(str, "called funct with n = ", n);
        func("func", n-1);

def main():
    func("main",7);

main();

# condition in 11th line is called the base case which controls the loop.
# if it will not there, program will know when to stop and Python will throw an error saying:
# RecursionError: maximum recursion depth exceeded while calling a Python object.

