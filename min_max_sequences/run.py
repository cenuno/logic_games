from generate_sequences import generate_sequences
from calculate_min_max_of_means import calculate_min_max_of_means

ages = [4, 4, 4, 9, 10, 11, 12]

sequences = generate_sequences(x=ages, p=3)

print(f"""
{ages} split into sequences of 3 looks like this:
{sequences}
""")

min_max = calculate_min_max_of_means(x=sequences)

print(f"""
After calculating the mean of each sequence,
the min mean value is {min_max["min"]} and
the max mean value is {min_max["max"]}.
""")
