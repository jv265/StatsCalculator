def calculate_zvalue(confidence_interval):
    if confidence_interval == 90:
        z = 1.645
    elif confidence_interval == 95:
        z = 1.96
    elif confidence_interval == 98:
        z = 2.33
    elif confidence_interval == 99:
        z = 2.575
    else:
        raise Exception("No z value found.")
    return z
