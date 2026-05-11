# Assignment 1: Time Converter
# ========================================

# An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

# Write a Python program that:
# - Accepts the total event duration in seconds as input.
# - Calculates how many hours, minutes, and seconds it corresponds to.
# - Displays the output in the format:
#   Hours: x, Minutes: y, Seconds: z

# Sample Input:
# Total event duration in seconds: 3672

total_seconds = int(input("Total event duration in seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")


'''
event = int(input("enter the event in seconds"))

hours = event//3600
event = event%3600
minutes = event//60
seconds = event%60

print(f"Hours: {hours}, Minutes: {minutes},Seconds:{seconds}")
'''

'''
event = int(input("enter the event in seconds"))

hours = event//3600
event = event-3600*hours
minutes = event//60
seconds = event-60*minutes

print(f"Hours: {hours}, Minutes: {minutes},Seconds:{seconds}")
'''