
def mode(data):
    list_number_of_occurrences = {}
    result_value = 0
    result = 0
    for num in data:
        if num in list_number_of_occurrences:
            list_number_of_occurrences[num] = list_number_of_occurrences[num] + 1
        else:
            list_number_of_occurrences[num] = 1

    for key in list_number_of_occurrences:
        if result_value < list_number_of_occurrences[key]:
            result_value = list_number_of_occurrences[key]
            result = key
    return result

