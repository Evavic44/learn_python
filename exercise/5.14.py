# TODO: Complete section exercise
import time

# The time module provides a function also named time, that returns the current Greenwich Mean Time in "the epoch" or
# which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970

# Epoch or Unix Time: Represents the number of seconds that has passed since Jan 1 1970 (Not counting leap seconds)

unix_time = time.time()
# Jan 1 1970, 00:00:00 UTC  - Oct 03 2023, 16:12:10 = 1696345944.2292697 in seconds
# (at the time of writing this line of code)

# Convert Epoch or Unix time
# You can convert the time to days by dividing the number of seconds by the total number of seconds in a day
# There are 86,400 seconds in a day. (24hrs * 60min * 60sec = 86,400)
# To convert unix time to days = Unix seconds / Number of seconds in a day

# Convert Unix Time
unix_to_days = unix_time / 24 * 60 * 60

print(f'{int(unix_to_days / 365)} years, '
      f'{int(unix_to_days / 30)} months, '
      f'{int(unix_to_days / 7)} weeks, '
      f'{int(unix_to_days / 3600)} days since UNIX time')
