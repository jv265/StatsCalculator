def mode(data):
    list_number_of_occurrences = {}
    result = 0
    result_value = 1
    mode_found = False

    # Goes through sample data and creates a dictionary of numbers with associated number of occurrences
    for num in data:
        if num in list_number_of_occurrences:
            list_number_of_occurrences[num] = list_number_of_occurrences[num] + 1
        else:
            list_number_of_occurrences[num] = 1

    # For each number in the dictionary, checks if it's at least greater and adds.
    # Otherwise we skip. We periodically check if we have a mode found during this process.
    for key in list_number_of_occurrences:
        if result_value < list_number_of_occurrences[key]:
            result_value = list_number_of_occurrences[key]
            result = key
            mode_found = True
            continue

        if list_number_of_occurrences[key] == result_value:
            mode_found = False

    if not mode_found:
        raise Exception("No mode found.")

    return result
