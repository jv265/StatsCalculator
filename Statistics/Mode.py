def mode(data):
    list_number_of_occurrences = {}
    result = 0
    result_value = 1
    mode_found = False

    for num in data:
        if num in list_number_of_occurrences:
            list_number_of_occurrences[num] = list_number_of_occurrences[num] + 1
        else:
            list_number_of_occurrences[num] = 1

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
