def Fibo (n):
    if n < 3:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

def main():
    print(Fibo(10))
main()