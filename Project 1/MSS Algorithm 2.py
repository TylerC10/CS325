import random
import time

my_list = random.sample(range(-5000, 5000), 10000)

start_time = time.time()


def subArrayCheck(numbers):
    total = 0
    max_total = 0    

    for i in range(0, len(numbers)):
        total = 0
        for j in range(i, len(numbers)):
            total += numbers[j]
            if total > max_total:
                max_total = total
                start_index = i
                stop_index = j

    return (numbers[start_index:stop_index], max_total)



    
subArrayCheck(my_list)
print(time.time() - start_time)
