"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tel_nums: set[str] = set()

for text in texts:
    incoming, answering, _ = text
    tel_nums |= {incoming, answering}

for call in calls:
    incoming, answering, _, _ = call
    tel_nums |= {incoming, answering}

print(f"There are {len(tel_nums)} different telephone numbers in the records.")
