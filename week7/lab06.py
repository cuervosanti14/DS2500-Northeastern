# LAB EXERCISE 06

### SET UP BEGINS Do not modify
section_A = [85, 88, 90, 92, 87, 91, 89, 84, 86, 90]
section_B = [78, 95, 82, 88, 91, 73, 99, 85, 77, 94]
### SET UP ENDS Do not modify

# Problem 1
def find_average(lst):
    """
    Takes a list of numbers in and returns mean of the list

    Parameters: list of numbers
    Returns: mean of list of numbers
    """
    num_total = 0
    num_count = 0

    # Add totals and counts from list
    for num in lst:
        num_total += num
        num_count += 1

    # Formula for returning average
    return num_total / num_count

# Problem 2
def find_median(lst):
    """
    Takes a list of numbers in and returns median of the list

    Parameters: list of numbers
    Returns: median of list of numbers
    """
    # Sort list from least to greatest
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 0:
        # Formula for calculating median if even # of nums
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        # Formula for calculating median if odd # of nums
        median = sorted_lst[n // 2]

    return median

# Problem 3
def find_mode(lst):
    """
    Takes a list of numbers in and returns mode of the list
    If there are multiple modes, return all of them in a list
    If there is no mode, return original list of numbers

    Parameters: list of numbers
    Returns: mode(s) of list of numbers
    """
    # Count frequencies of each number
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find the max frequency
    max_count = max(counts.values())

    # Return original list if there is no mode (every element appears only once)
    if max_count == 1:
        return lst

    # Get all numbers with max frequency
    modes = [num for num, count in counts.items() if count == max_count]

    # Return mode(s)
    if len(modes) == 1:
        return modes[0]
    else:
        return modes

# Problem 4
def find_variance(lst):
    """
    Takes a list of numbers in and returns population variance of the list

    Parameters: list of numbers
    Returns: variance of list of numbers
    """
    pop_variance_numerator = 0
    # Use prior function to get mean of lst to use in for loop
    mean = find_average(lst)

    for num in lst:
        # Sum the total squared differences
        pop_variance_numerator += (num - mean) ** 2

    # Divide by "N" for population variance
    return pop_variance_numerator / len(lst)

def find_sd(variance):
    """
    Takes a list of numbers in and returns standard deviation of the list

    Parameters: list of numbers
    Returns: standard deviation of list of numbers
    """
    std_dev = variance ** 0.5

    return std_dev

# Problem 5
# Calculating section A statistics
sec_A_avg = find_average(section_A)
sec_A_med = find_median(section_A)
sec_A_mode = find_mode(section_A)
sec_A_var = find_variance(section_A)
sec_A_sd = find_sd(sec_A_var)

# Calculating section B statistics
sec_B_avg = find_average(section_B)
sec_B_med = find_median(section_B)
sec_B_mode = find_mode(section_B)
sec_B_var = find_variance(section_B)
sec_B_sd = find_sd(sec_B_var)

def main():
    # Printing section A statistics
    print("Section A's mean =", sec_A_avg)
    print("Section A's median =", sec_A_med)
    print("Section A's mode =", sec_A_mode)
    print("Section A's variance =", sec_A_var)
    print("Section A's standard deviation =", sec_A_sd)

    # Printing section B statistics
    print("Section B's mean =", sec_B_avg)
    print("Section B's median =", sec_B_med)
    print("Section B's mode =", sec_B_mode)
    print("Section B's variance =", sec_B_var)
    print("Section B's standard deviation =", sec_B_sd)

if __name__ == '__main__':
    main()