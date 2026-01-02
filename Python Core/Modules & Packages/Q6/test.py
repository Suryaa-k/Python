from Demo import Demo
import random
st = Demo("Peter")
st.display()
st.roll_num = random.randint(1, 1000) # Enter wrong pin
print(st.roll_num)
st.roll_num = random.randint(1, 1000) # Enter Correct pin
print(st.roll_num)