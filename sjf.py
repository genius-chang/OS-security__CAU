import time

# List of processes with their names and durations
processes = [
    ("Process 1", 3),
    ("Process 2", 1),
    ("Process 3", 4),
    ("Process 4", 2)
]

def sjf_scheduling(processes):
    print("SJF Scheduling")
    # Sort processes by duration and run the shortest one first
    sorted_processes = sorted(_______, key=lambda x: x[1])
    for _______, _______ in ______________:
        print(f"{process} is running for {duration} seconds")
        time.sleep(_______)
    print("All processes in SJF completed.\n")

# Execute SJF scheduling
sjf_scheduling(processes)


