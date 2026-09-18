from math import sqrt

def mean(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    return sum(values)/len(values) 

def median(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    sorted_values = sorted(values)
    middle = len(values)//2

    if len(values) % 2 == 0:
        return (sorted_values[middle-1] + sorted_values[middle])/2
    else:
        return sorted_values[middle]

def mode(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    """Currently shows the first mode when there is a tie"""

    sorted_values = sorted(values)
    selected_value = None
    selected_value_count = 0
    current_value = None
    current_value_count = 0

    for value in sorted_values:
        if value != current_value:
            current_value = value
            current_value_count = 1 
        else:
            current_value_count += 1
            if current_value == selected_value:
                selected_value_count += 1

        if current_value_count > selected_value_count:
            selected_value = current_value
            selected_value_count = current_value_count

    return selected_value

def data_range(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    sorted_values = sorted(values)

    return sorted_values[-1] - sorted_values[0]

def std_variance(*values) -> float:
    if not values:
        raise ValueError("No value provided")
    
    mean_value = mean(*values)
    squared_differences = 0

    for value in values:
        squared_differences += (value - mean_value) ** 2

    return squared_differences / len(values)

def sample_variance(*values) -> float:
    if len(values) < 2:
        raise ValueError("No value provided")
    
    mean_value = mean(*values)
    squared_differences = 0

    for value in values:
        squared_differences += (value - mean_value) ** 2

    return squared_differences / (len(values) - 1)

def std_deviation(*values) -> float:
    if len(values) < 2:
        raise ValueError("No value provided")

    return sqrt(std_variance(*values))
    
def sample_deviation(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    return sqrt(sample_variance(*values))
 
def percentile(indicator, *values) -> float:    

    if indicator < 0 or indicator > 100:
       raise ValueError("Value must be between 0 and 100")

    sorted_values = sorted(values)
    value_quantity = len(values)
    ivalue = ((indicator / 100) * (value_quantity - 1))

    lower_index = int(ivalue)
    fraction = ivalue - lower_index
    lower_value = sorted_values[lower_index]
    if indicator == 100:
        upper_value = sorted_values[value_quantity - 1]
    else:
        upper_value = sorted_values[lower_index + 1]

    return lower_value + fraction * (upper_value - lower_value)


    
def quartiles(indicator, *values) -> float:

    if indicator not in (1, 2, 3):
        raise ValueError("Quartile indicator must be 1, 2 or 3")

    return percentile((indicator * 25), *values)

def coefficient_of_variation(*values) -> float:
    if mean(*values) == 0:
        raise ValueError("Coefficient of variation is undefined when the mean is 0")


    return (std_deviation(*values) / mean(*values)) * 100

def covariance(x, y) -> float:
    if len(x) == 0 or len(y) == 0:
        raise ValueError("Both collections should be non-empty")
    elif len(x) != len(y):
        raise ValueError("Both collections must have the same number of elements")

    mean_x = mean(*x)
    mean_y = mean(*y)
    multiplied_difference = 0

    for x_value, y_value in zip(x, y):
        multiplied_difference += (x_value - mean_x) * (y_value - mean_y)

    return multiplied_difference / len(x)

def sample_covariance(x, y) -> float:
    
    if len(x) == 0 or len(y) == 0:
        raise ValueError("Both collections should be non-empty")
    elif len(x) != len(y):
        raise ValueError("Both collections must have the same number of elements")

    mean_x = mean(*x)
    mean_y = mean(*y)
    multiplied_difference = 0

    for x_value, y_value in zip(x, y):
        multiplied_difference += (x_value - mean_x) * (y_value - mean_y)

    return multiplied_difference / (len(x) - 1)

def pearson_correlation(x, y) -> float: 
    if len(x) == 0 or len(y) == 0:
        raise ValueError("Both collections should be non-empty")
    elif len(x) != len(y):
        raise ValueError("Both collections must have the same number of elements")
    elif std_deviation(*x) == 0 or std_deviation(*y) == 0:
        raise ValueError("Correlation is undefined for constant values")

    return covariance(x, y) / (std_deviation(*x) * std_deviation(*y))

def iqr(*values) -> float:
    if not values:
        raise ValueError("No value provided")

    return quartiles(3, *values) - quartiles(1, *values)

def get_outliers(*values) -> dict[str, float | list[float]]:
    if not values:
        raise ValueError("No value provided")

    iqr_value = iqr(*values)
    lower_fence = quartiles(1, *values) - (1.5 * iqr_value)
    upper_fence = quartiles(3, *values) + (1.5 * iqr_values)
    lower_outliers: list[float] = []
    upper_outliers: list[float] = []

    for value in values:
        if value < lower_fence:
            lower_outliers.append(value)
        elif value > upper_fence:
            upper_outliers.append(value)

    return {
        "lower_fence": lower_fence,
        "upper_fence": upper_fence,
        "lower_outliers": lower_outliers,
        "upper_outliers": upper_outliers,
    }









