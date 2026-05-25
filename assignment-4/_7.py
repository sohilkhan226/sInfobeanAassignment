# Assignment 7: Cricket Run Rate

# In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

# Input:
# Total runs = 275
# Overs = 48.3

# Expected Output:
# Total Balls = 291
# Run Rate = 5.67

runs = 275
overs = 48.3

completed_overs = int(overs)
extra_balls = round((overs - completed_overs) * 10)
total_balls = completed_overs * 6 + extra_balls
run_rate = round(runs / (total_balls / 6), 2)

print("Total Balls =", total_balls)
print("Run Rate =", run_rate)



# runs = 275
# overs = 48.3
# runrate=runs/overs       //mostly hum yahi kar rahe h bus ak ya do point me dikat aayi h....
# print(round(runrate,2))




# overs= float(input("enter the over value"))
# runs= int(input("enter the run"))
# over = int(overs)
# extra_ball = round(overs-over)*10

# total_balls=over*6+extra_ball
# run_rate = runs/(total_balls/6)
# print(run_rate)