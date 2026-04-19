# LAB EXERCISE 03

# SET UP BEGINS - Do Not Modify
employees = [
{"name": "Alice", "department": "Engineering", "years_experience": 5},
{"name": "Ann", "department": "Marketing", "years_experience": 4},
{"name": "Ben", "department": "Engineering", "years_experience": 2},
{"name": "Bob", "department": "Engineering", "years_experience": 6},
{"name": "Eve", "department": "HR", "years_experience": 3},
]

pairs = [(5, 2), (1, 4), (3, 1), (2, 9)]
# SET UP ENDS - Do Not Modify

# PROBLEM 01
def count_ints(lst, target):
    """
    Takes a 2D list of integers & a single integer & returns
    number of times that integer appears in the list

    parameter: list of integers, target integer
    returns: # of occurrences of that integer in the list
    """
    count = 0

    # Filter list to get count of target integer
    for row in lst:
        count += len(list(filter(lambda x: x == target, row)))
    return count

# PROBLEM 02
def remove_duplicates(lst):
    """
    Takes a list of numbers & returns new list after removing duplicates

    parameter: list of #s
    returns: new list after removing duplicates
    """
    nums = []

    # Loop through list to get individual (no duplicates) numbers
    for item in lst:
        if item not in nums:
            nums.append(item)
    return nums

# PROBLEM 03
def filter_employees(lst):
    """
    Takes a list of dictionaries representing employees & returns list of
    employee's in Engineering with > 3 years of experience

    parameter: list of employees
    returns: list of qualified employee's names
    """
    # Filter employees by department & experience
    # And get name of valid employees
    return [emp["name"] for emp in lst
            if emp["department"] == "Engineering"
            and emp["years_experience"] > 3]

# PROBLEM 04
def function_p4(lst):
    """
    Takes a list of tuples, where each tuple contains 2 numbers, and
    returns a list of tuples containing the 2 original numbers & their product

    parameter: list of tuples, where each tuple only contains 2 numbers
    returns: list of tuples containing original 2 numbers & their product
    """
    # Get list of tuples w/ pair & their product
    return [(a, b, a * b) for a, b in pairs]

# PROBLEM 05
def function_p5(lst):
    """
    Takes a list of tuples & returns list sorted in ascending order
    by second element of each tuple

    parameter: list of tuples
    returns: list sorted in ascending order by second element of each tuple
    """
    # Sort list by increasing order of 2nd element
    return sorted(lst, key = lambda x: x[1])

# PROBLEM 06
def function_p6(lst):
    """
    Takes a list of tuples containing #s & returns the list sorted
    in descending order by sum of each tuple

    parameter: list of tuples containing #s
    returns: list sorted in descending order by sum of each tuple
    """
    # Sort list by descending order of sums
    return sorted(lst, key = lambda x: x[0] + x[1], reverse = True)

def main():
    print(filter_employees(employees))
    print(function_p4(pairs))
    print(function_p5(pairs))
    print(function_p6(pairs))

if __name__ == "__main__":
    main()