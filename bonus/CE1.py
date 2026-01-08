import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

gen_num = random.randint(lower_bound, upper_bound)
print(gen_num)