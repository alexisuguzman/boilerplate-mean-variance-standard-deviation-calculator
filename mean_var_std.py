import numpy as np

def create_matrix(list):
    matrix = np.array(list).reshape(3,3)
    return matrix

def calculate(list):

    #Check corrrect lenght of list
    if not len(list) == 9:
        raise ValueError("List must contain nine numbers.") 
    
    calculations = {}

    #Convert list to matrix
    matrix = create_matrix(list)

    mean_axis_1 = matrix.mean(axis=0).tolist()
    mean_axis_2 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()
    calculations["mean"] = [mean_axis_1, mean_axis_2, mean_flattened]

    variance_axis_1 = matrix.var(axis=0).tolist()
    variance_axis_2 = matrix.var(axis=1).tolist()
    variance_flattened = matrix.var().tolist()
    calculations["variance"] = [variance_axis_1, variance_axis_2, variance_flattened]

    std_axis_1 = matrix.std(axis=0).tolist()
    std_axis_2 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std()
    calculations["standard deviation"] = [std_axis_1, std_axis_2, std_flattened]

    max_axis_1 = matrix.max(axis=0).tolist()
    max_axis_2 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()
    calculations["max"] = [max_axis_1, max_axis_2, max_flattened]

    min_axis_1 = matrix.min(axis=0).tolist()
    min_axis_2 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()
    calculations["min"] = [min_axis_1, min_axis_2, min_flattened]

    sum_axis_1 = matrix.sum(axis=0).tolist()
    sum_axis_2 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()
    calculations["sum"] = [sum_axis_1, sum_axis_2, sum_flattened]

    return calculations