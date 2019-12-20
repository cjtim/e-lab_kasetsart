def read_hour():
    hour = int(input("Enter hour: "))
    return hour
def read_minute():
    minute = int(input("Enter minute: "))
    return minute
def read_second():
    second = int(input("Enter second: "))
    return second
def to_seconds(hour, minute, second):
    return (hour*3600)+(minute*60)+second
def time_elapsed(start_time, finish_time):
    summ = finish_time - start_time
    hour = summ//3600
    minute = (summ%3600)//60
    second = (summ)%60
    print(end='')
    return "{0} hours {1} minutes {2} seconds.".format(hour,minute,second)

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
