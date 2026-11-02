#PINS WALA QUESTION 

N, K = map(int, input("Enter number of pins (N) and number of balls (K): ").split())
pins = ["I"] * N

for i in range(1, K + 1):
    s, e = map(int, input(f"Enter start and stop pin positions for ball {i}: ").split())
    for j in range(s - 1, e):
        pins[j] = "."

print("Final pin status:", "".join(pins))