
import time

number = 7

print("Multiplication Table of", number)
print("-" * 30)

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    time.sleep(0.5)

print("\nTask completed successfully!")
