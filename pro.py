# FCFS Scheduling Simulation

processes = ['Quiz1','Quiz2','Quiz3','Quiz4','Quiz5']
burst_time = [5,3,8,6,2]

waiting_time = [0] * len(processes)
turnaround_time = [0] * len(processes)

# Calculate waiting time
for i in range(1,len(processes)):
    waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

# Calculate turnaround time
for i in range(len(processes)):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

print("Process   Burst Time   Waiting Time   Turnaround Time")

for i in range(len(processes)):
    print(processes[i],"\t",burst_time[i],"\t\t",waiting_time[i],"\t\t",turnaround_time[i])

avg_wait = sum(waiting_time)/len(processes)
avg_turn = sum(turnaround_time)/len(processes)

print("\nAverage Waiting Time =",avg_wait)
print("Average Turnaround Time =",avg_turn)