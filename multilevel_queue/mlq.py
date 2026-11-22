from collections import deque

# MULTILEVEL QUEUE SCHEDULING
# Queue 1: Round Robin; Queue 2: FCFS

processes = [
    {"pid": "P1", "arrival": 0, "burst": 5, "queue": 1},
    {"pid": "P2", "arrival": 1, "burst": 4, "queue": 1},
    {"pid": "P3", "arrival": 0, "burst": 6, "queue": 2},
    {"pid": "P4", "arrival": 2, "burst": 3, "queue": 2},
    {"pid": "P5", "arrival": 3, "burst": 2, "queue": 1},
]

QUANTUM = 2

for process in processes:
    process["remaining"] = process["burst"]
    process["completion"] = None

processes.sort(key=lambda process: (process["arrival"], process["pid"]))

q1 = deque()
q2 = deque()
current_q1 = None
current_q2 = None
quantum_left = 0
time = 0
index = 0
gantt = []


def add_segment(pid, start, end):
    if gantt and gantt[-1][0] == pid and gantt[-1][2] == start:
        gantt[-1] = (pid, gantt[-1][1], end)
    else:
        gantt.append((pid, start, end))


while any(process["remaining"] > 0 for process in processes):
    # Add newly arrived processes to their queues.
    while index < len(processes) and processes[index]["arrival"] <= time:
        process = processes[index]
        if process["queue"] == 1:
            q1.append(process)
        else:
            q2.append(process)
        index += 1

    # Queue 1 has strict priority over Queue 2.
    if current_q1 is None and q1:
        current_q1 = q1.popleft()
        quantum_left = QUANTUM

    if current_q1 is not None:
        running = current_q1
        add_segment(running["pid"], time, time + 1)
        running["remaining"] -= 1
        quantum_left -= 1

        if running["remaining"] == 0:
            running["completion"] = time + 1
            current_q1 = None
            quantum_left = 0
        elif quantum_left == 0:
            q1.append(running)
            current_q1 = None

    else:
        # Queue 2 uses FCFS and is interrupted by Queue 1 arrivals.
        if current_q2 is None and q2:
            current_q2 = q2.popleft()

        if current_q2 is not None:
            running = current_q2
            add_segment(running["pid"], time, time + 1)
            running["remaining"] -= 1

            if running["remaining"] == 0:
                running["completion"] = time + 1
                current_q2 = None
        else:
            add_segment("IDLE", time, time + 1)

    time += 1


print("\nMULTILEVEL QUEUE SCHEDULING")
print("Queue 1: Round Robin (Quantum = 2 ms)")
print("Queue 2: FCFS")

print("\nGANTT CHART")
for pid, start, end in gantt:
    print(f"| {pid} [{start}-{end}] ", end="")
print("|")

total_tat = 0
total_wt = 0

print("\nPROCESS PERFORMANCE")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for process in sorted(processes, key=lambda item: item["pid"]):
    turnaround = process["completion"] - process["arrival"]
    waiting = turnaround - process["burst"]
    total_tat += turnaround
    total_wt += waiting
    print(
        f'{process["pid"]}\t{process["arrival"]}\t{process["burst"]}\t'
        f'{process["completion"]}\t{turnaround}\t{waiting}'
    )

number_of_processes = len(processes)
print("\nAverage Turnaround Time:", round(total_tat / number_of_processes, 2), "ms")
print("Average Waiting Time:", round(total_wt / number_of_processes, 2), "ms")
