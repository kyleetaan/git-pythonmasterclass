import time 
from time import monotonic as my_timer
import random

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0])
# print("Month", time_here[1])
# print("Day", time_here[2])
# print("Hour", time_here[3])
# print("Minutes", time_here[4])
# print("Seconds", time_here[5])

input("Press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time-start_time))
