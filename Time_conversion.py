"""Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. """

import os

def timeConversion(s):
    # Extract the period (AM/PM) and split the time
    period = s[-2:]  # AM or PM
    time_parts = s[:-2].split(":")  # Get HH, MM, SS

    hours = int(time_parts[0])
    minutes = time_parts[1]
    seconds = time_parts[2]

    # Convert hours based on AM/PM rules
    if period == "AM":
        if hours == 12:
            hours = 0  # Midnight case
    else:  # PM case
        if hours != 12:
            hours += 12  # Convert PM times except for 12 PM

    # Format hours to two digits
    military_time = f"{hours:02}:{minutes}:{seconds}"
    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()  # Read input and remove extra spaces
    result = timeConversion(s)

    fptr.write(result + '\n')
    fptr.close()
