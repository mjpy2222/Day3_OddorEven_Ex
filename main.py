# Which number do you want to check?

number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
check_remainder = number % 2
if check_remainder >= 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
    
