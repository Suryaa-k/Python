# PROBLEM:
# Calculate maximum members that can board a balloon at once.
#
# INPUT (3 lines):
# 1. n = number of members in line
# 2. w = list of n weights (space separated)
# 3. c = balloon weight capacity
#
# STEPS:
# 1. Sort weights in ascending order
# 2. Find maximum k members where sum(weights[0:k]) <= capacity
# 3. Output: k (maximum members count)
#
# EXAMPLE:
# Input:
# 5
# 30 40 50 60 70
# 150
#
# Output: 3
# (30+40+50=120 <=150, 30+40+50+60=180 >150)

n=int(input())
w=

