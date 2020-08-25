# A function call itself multiple times instead of once, called non-linear Recusrion.
# fibonacci problem

def fibonacci_(n):
    if n == 0:
        return 0;
    if n == 1 :
        return 1;
    else:
        return fibonacci_(n-1) + fibonacci_(n-2);

fibonacci_(5);
