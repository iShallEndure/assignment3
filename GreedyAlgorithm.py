# Define a list of job durations
job_durations = [2, 3, 1, 4, 6, 5]

# Sort job durations in ascending order
job_durations.sort()

# Calculate the total completion time
total_completion_time = 0
current_time = 0

for duration in job_durations:
    current_time += duration
    total_completion_time += current_time

print(f"Total completion time: {total_completion_time}")