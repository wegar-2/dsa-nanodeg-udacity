"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_times: dict[str, int] = {}
for call in calls:
    incoming, answering, _, t = call

    if incoming not in call_times:
        call_times[incoming] = 0
    call_times[incoming] += int(t)

    if answering not in call_times:
        call_times[answering] = 0
    call_times[answering] += int(t)

max_time: int = max(call_times.values())
longest_calls = {k: v for k, v in call_times.items() if v == max_time}

tel_num: str = list(longest_calls.keys())[0]
total_time = longest_calls[tel_num]

print(f"{tel_num} spent the longest time, "
      f"{total_time} seconds, on the phone during September 2016.")
