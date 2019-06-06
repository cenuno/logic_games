from typing import List

Vector = List[int]


def generate_sequences(x: Vector, p: int) -> List[Vector]:
    """
    For a given list (l), store each sequence of l
    from the ith index to the ith index + p index of l
    as a list of lists.
    """
    output = []
    if p > len(x):
        raise ValueError("p can only be <= to the len(x).")
    for index, element in enumerate(x):
        end_range = index + p
        sequence = x[index:end_range]
        if len(sequence) == p:
            output.append(sequence)
    return output


test = [1, 2, 3, 4]
assert generate_sequences(x=test, p=1) == [[1], [2], [3], [4]]
assert generate_sequences(x=test, p=2) == [[1, 2], [2, 3], [3, 4]]
assert generate_sequences(x=test, p=3) == [[1, 2, 3], [2, 3, 4]]
assert generate_sequences(x=test, p=4) == [[1, 2, 3, 4]]
