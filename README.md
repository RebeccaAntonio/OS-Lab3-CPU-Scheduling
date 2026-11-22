<div align="center">

# BCA151 - OS Laboratory Activity 3
## Multilevel Queue and Real-Time CPU Scheduling

<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Rebecca Lyn Antonio</td>
  </tr>
  <tr>
    <td><strong>Course and Section</strong></td>
    <td>Bachelor of Science in Computer Applications | B186</td>
  </tr>
  <tr>
    <td><strong>Instructor</strong></td>
    <td>Prof. Maria Fe Bahinting</td>
  </tr>
  <tr>
    <td><strong>Date Submitted</strong></td>
    <td>11/22/2026</td>
  </tr>
</table>

</div>

### I. Introduction
This laboratory activity implements and compares Multilevel Queue (MLQ), Rate Monotonic Scheduling (RMS), and Earliest Deadline First (EDF). Python simulations show how processes and periodic task instances are selected for the CPU. Gantt charts and program results are used to examine execution order, waiting and turnaround times, CPU utilization, and deadline compliance.

### II. Objectives
- Explain how MLQ, RMS, and EDF schedule work.
- Implement MLQ using Round Robin and FCFS.
- Simulate preemptive RMS and EDF scheduling in Python.
- Generate and interpret Gantt charts.
- Calculate performance metrics and check deadline compliance.
- Organize program code, output, and documentation in a GitHub repository.

### III. Scheduling Algorithms

1. **Multilevel Queue (MLQ):** Processes are assigned to fixed queues by category. Queue 1 contains interactive processes and uses Round Robin with a 2 ms quantum. Queue 2 contains batch processes and uses FCFS. Queue 1 has strict priority over Queue 2.
2. **Rate Monotonic Scheduling (RMS):** A fixed-priority preemptive algorithm for periodic tasks. The task with the shortest period receives the highest priority.
3. **Earliest Deadline First (EDF):** A preemptive algorithm that dynamically selects the ready task instance with the earliest absolute deadline.

### IV. Program Implementation
- `multilevel_queue/mlq.py` simulates Queue 1 with Round Robin and Queue 2 with FCFS. It prints a Gantt chart, completion times, turnaround times, waiting times, and averages.
- `real_time_scheduling/rms.py` creates separate jobs for periodic task releases, assigns fixed priorities by period, and reports the Gantt chart, utilization, and deadline status.
- `real_time_scheduling/edf.py` creates separate periodic jobs and selects the ready job with the earliest absolute deadline. Ties are resolved by release time and then task ID.

All simulations use 1 ms time steps. Context-switching overhead is ignored.

### V. Test Data

#### MLQ processes
  
| Process | Arrival (ms) | Burst (ms) | Queue |
|---|---:|---:|---:|
| P1 | 0 | 5 | 1 |
| P2 | 1 | 4 | 1 |
| P3 | 0 | 6 | 2 |
| P4 | 2 | 3 | 2 |
| P5 | 3 | 2 | 1 |

Queue 1 uses Round Robin with a 2 ms quantum. Queue 2 uses FCFS.

#### RMS and EDF periodic tasks

| Task | Execution time C (ms) | Period T (ms) | Relative deadline D (ms) |
|---|---:|---:|---:|
| T1 | 1 | 4 | 4 |
| T2 | 1 | 5 | 5 |
| T3 | 2 | 10 | 10 |

All tasks release their first job at time 0. The simulation duration is 20 ms, and each relative deadline equals its period.

### VI. Results and Discussion

## Multilevel Queue (MLQ)

**Gantt chart**

`P1 [0–2] → P2 [2–4] → P1 [4–6] → P5 [6–8] → P2 [8–10] → P1 [10–11] → P3 [11–17] → P4 [17–20]`

| Process | Completion (ms) | Turnaround (ms) | Waiting (ms) |
|---|---:|---:|---:|
| P1 | 11 | 11 | 6 |
| P2 | 10 | 9 | 5 |
| P3 | 17 | 17 | 11 |
| P4 | 20 | 18 | 15 |
| P5 | 8 | 5 | 3 |

Average turnaround time is **12.0 ms**. Average waiting time is **8.0 ms**. Queue 1 processes run before Queue 2 while they are ready; the batch processes run afterward.

### Evidence
MLQ program execution showing the Gantt chart and process performance results.
<img width="1917" height="1017" alt="mlq_execution png" src="https://github.com/user-attachments/assets/eafaaec3-2037-46d4-bf4b-3ff9b0450bac" />
<div align="center">
Figure 1. MLQ program execution]

</div>

## Rate Monotonic Scheduling (RMS)

**Gantt chart**

`T1 [0–1] → T2 [1–2] → T3 [2–4] → T1 [4–5] → T2 [5–6] → IDLE [6–8] → T1 [8–9] → IDLE [9–10] → T2 [10–11] → T3 [11–12] → T1 [12–13] → T3 [13–14] → IDLE [14–15] → T2 [15–16] → T1 [16–17] → IDLE [17–20]`

CPU utilization is **65%**. The RMS sufficient utilization bound for three tasks is **77.98%**, so the task set passes the sufficient-bound test. All task instances with deadlines in the simulation are marked **MET**; there are **0 deadline misses**.

### Evidence
RMS program execution showing the Gantt chart, CPU utilization, and task deadline results.
<img width="1917" height="992" alt="rms_execution png" src="https://github.com/user-attachments/assets/aad84127-bcea-470e-9355-5c4d746184f4" />
<div align="center">
Figure 2. RMS program execution

</div>

## Earliest Deadline First (EDF)

**Gantt chart**

`T1 [0–1] → T2 [1–2] → T3 [2–4] → T1 [4–5] → T2 [5–6] → IDLE [6–8] → T1 [8–9] → IDLE [9–10] → T2 [10–11] → T3 [11–12] → T1 [12–13] → T3 [13–14] → IDLE [14–15] → T2 [15–16] → T1 [16–17] → IDLE [17–20]`

CPU utilization is **65%**. The task set passes the classical EDF utilization test because utilization is at most 100%. All task instances with deadlines in the simulation are marked **MET**; there are **0 deadline misses**.

### Evidence
EDF program execution showing the Gantt chart, CPU utilization, and task deadline results.
<img width="1917" height="1020" alt="edf_execution png" src="https://github.com/user-attachments/assets/fe41927f-2315-461e-b788-77ffa3f9ca6a" />
<div align="center">
Figure 3. EDF program execution

</div>


### VII. Algorithm Comparison

| Criterion | MLQ | RMS | EDF |
|---|---|---|---|
| Scheduling basis | Fixed queue priority | Task period | Absolute deadline |
| Priority assignment | Fixed by queue | Fixed; shorter period means higher priority | Dynamic; earliest deadline means higher priority |
| Scheduling type | Depends on queue policy; Queue 1 RR and Queue 2 FCFS | Preemptive | Preemptive |
| Main application | Different process categories | Periodic real-time tasks | Deadline-based real-time tasks |
| Deadline monitoring | Not inherent | Yes | Yes |

### VIII. Guide Questions

1. **What is the main difference between Multilevel Queue and Multilevel Feedback Queue scheduling?**  
   In MLQ, processes stay in their assigned queues. In Multilevel Feedback Queue scheduling, processes can move between queues based on their behavior or CPU usage.

2. **Why does MLQ use different scheduling algorithms for different process queues?**  
   Different process categories have different needs. Interactive processes benefit from short, responsive time slices, while batch processes can be handled in arrival order.

3. **How does RMS determine which task receives the CPU first?**  
   RMS gives the highest priority to the task with the shortest period among the ready tasks.

4. **Why is RMS considered a fixed-priority scheduling algorithm?**  
   Each task's priority is assigned based on its period and does not change while the task runs.

5. **How does EDF determine which task should execute next?**  
   EDF selects the ready task instance with the earliest absolute deadline.

6. **Why is EDF considered a dynamic-priority scheduling algorithm?**  
   The priority can change as new task instances are released and their absolute deadlines are compared.

7. **What happens when a newly released task has an earlier deadline than the currently running task under EDF?**  
   The newly released task preempts the running task and executes first.

8. **Why is CPU utilization important in real-time scheduling?**  
   Utilization estimates how much processor time tasks require. It helps assess whether the processor has enough capacity to complete work on time.

9. **Can a task set with CPU utilization below 100% still miss a deadline? Explain the conditions under which this may happen.**  
   Yes. Under fixed-priority scheduling, utilization below 100% alone does not guarantee that every deadline will be met. Task periods, execution times, deadlines, release patterns, and scheduling overhead can cause a task to miss its deadline. For RMS, the sufficient utilization bound is a stronger test: passing it guarantees schedulability under the stated assumptions, while failing it does not by itself prove a miss.

10. **Which algorithm would you recommend for periodic real-time tasks, RMS or EDF? Justify your answer.**  
    For this task set, both algorithms meet all deadlines. RMS is straightforward when priorities should remain fixed. EDF can use processor capacity more flexibly because it always selects the ready job with the closest deadline. The best choice depends on system requirements and assumptions.

### IX. Conclusion
This activity demonstrated how MLQ uses fixed process queues with different scheduling policies, how RMS assigns fixed priorities based on task periods, and how EDF dynamically prioritizes absolute deadlines. The Python simulations produced Gantt charts and performance results. For the periodic task set, both RMS and EDF used 65% CPU and reported no deadline misses.

<div align="center">

## End of BCA151 - OS Laboratory Activity 3
