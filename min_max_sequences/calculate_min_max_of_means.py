from typing import Dict, List

Vector = List[int]


def calculate_min_max_of_means(x: List[Vector]) -> Dict[str, float]:
    """
    Calculate the mean for each sequence in x and
    return the min and max mean values as a dictionary
    """
    output = {}
    means = [sum(sequence) / len(sequence) for sequence in x]
    output["min"] = min(means)
    output["max"] = max(means)
    return output


test = [[1, 2, 3], [2, 3, 4]]
assert calculate_min_max_of_means(x=test) == {"min": 2.0, "max": 3.0}
