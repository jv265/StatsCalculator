def calculate_zvalue(confidence_level):
    # Reference: https://www.surveymonkey.com/mp/margin-of-error-calculator/
    if confidence_level == 80:
        z = 1.28
    elif confidence_level == 85:
        z = 1.44
    elif confidence_level == 90:
        z = 1.645
    elif confidence_level == 95:
        z = 1.96
    elif confidence_level == 98:
        z = 2.33
    elif confidence_level == 99:
        z = 2.58
    else:
        raise Exception("No z value found.")
    return z
