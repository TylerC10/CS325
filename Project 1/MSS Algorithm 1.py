import random
import time

my_list = random.sample(range(-550, 550), 1100)

start_time = time.time()

def subArrayCheck(numbers):
    max_total = 0
    for i in range(0, len(numbers)):
        for j in range(1, len(numbers)):
            place_total = 0
            for k in range(i, j):
                place_total += numbers[k]
                if place_total > max_total:
                    max_total = place_total
                    start_index = i
                    stop_index = j
    return (numbers[start_index:stop_index], max_total)
    



subArrayCheck(my_list)
print(time.time() - start_time)
