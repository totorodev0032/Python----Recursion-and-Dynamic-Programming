# When two or more functions call themselves indirectly from each other , called indirect recursion.
##### Example #####

def func1(str, n):
    if n>0:
        print(str, "called func1 with n = ", n);
        func2("func1", n-1);

def func2(str, n):
    if n > 0:
        print(str, "calling from func2 with n = ", n);
        func1("func2", n-1);

def main():
    func1("main",7);

main();

# Following is the order of the function calls:
# func1 --> func2 --> func1 --> func2