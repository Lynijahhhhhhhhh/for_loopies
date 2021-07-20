# -------------------- Section 3 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 3\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   Create a function that will calculate and print the first n numbers of the fibonacci sequence.
#       n is specified by the user.
#
#   NOTE: You can assume that the user will enter a number larger than 2
#
# Example Output
#
#   >> size... 6
#
#   1, 1, 2, 3, 5, 8
#
# Write Code Below #
user=int(input("Enter a term higher than 2: "))
def fibonacci(n):
    sequence = [0,1]
    for i in range(2,n+1):
        next_num = sequence[-1] + sequence[-2]
        
        sequence.append(next_num)
    return sequence



sequence = fibonacci(user)
print(sequence)