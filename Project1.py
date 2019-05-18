#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
import time
import winsound

def fibseq(N):
    a =1
    b =1

    for a in range (N):
        yield a
        a, b = b, a+b

def countdown(t):
    while t:
        for s in range (t):
            print(f"Faltan {t} segundos...\r", end="")
            t -= 1
            time.sleep(1)
    print("\nTime!!!")
    winsound.Beep(350,1000)



N = int(input("Enter number of fibonacci terms desired: "))

for a in fibseq(N):
    print(a)
    print(".")

countdown(N)

