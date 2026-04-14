import os
import mysql.connector
import statistics

# ================= DATABASE CONNECTION =================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root3306",
    database="parv_project"   # make sure this matches your DB
)

cursor = db.cursor()

# ================= LOGIN SYSTEM =================
def login():
    print("\n===== LOGIN SYSTEM =====")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:
        print("\nLogin Successful! Welcome", user[1])
        return True
    else:
        print("\nInvalid Email or Password")
        return False


# ================= DBMS MODULE =================
def dbms_analysis():

    print("\n===== DBMS DATA FROM DATABASE =====")

    cursor.execute("SELECT score FROM results")
    data = cursor.fetchall()

    scores = [x[0] for x in data]

    print("Scores:", scores)

    if len(scores) > 0:
        print("Average Score:", statistics.mean(scores))
        print("Highest Score:", max(scores))
        print("Lowest Score:", min(scores))


# ================= COA MODULE (FCFS) =================
def coa_module():

    print("\n===== COA CPU Scheduling (FCFS) =====")

    processes = ['Quiz1','Quiz2','Quiz3','Quiz4','Quiz5']
    burst_time = [5,3,8,6,2]

    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)

    # Waiting Time
    for i in range(1,len(processes)):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

    # Turnaround Time
    for i in range(len(processes)):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("Process   Burst   Waiting   Turnaround")

    for i in range(len(processes)):
        print(processes[i],"\t",burst_time[i],"\t",waiting_time[i],"\t",turnaround_time[i])

    print("\nAverage Waiting Time =", sum(waiting_time)/len(processes))
    print("Average Turnaround Time =", sum(turnaround_time)/len(processes))


# ================= STATISTICS MODULE =================
def statistics_module():

    print("\n===== STATISTICS ANALYSIS =====")

    scores = [8,7,6,9,5,7,8,6,9,7]

    print("Scores:", scores)
    print("Mean:", statistics.mean(scores))
    print("Median:", statistics.median(scores))
    print("Mode:", statistics.mode(scores))
    print("Standard Deviation:", statistics.stdev(scores))

    # Ranking
    students = {
        "Rahul":8,
        "Aman":7,
        "Priya":6,
        "Riya":9,
        "Karan":5
    }

    ranking = sorted(students.items(), key=lambda x: x[1], reverse=True)

    print("\n===== STUDENT RANKING =====")

    rank = 1
    for name, score in ranking:
        print(rank, name, "Score:", score)
        rank += 1


# ================= MAIN PROGRAM =================

# Login attempts
for i in range(3):
    if login():
        break
else:
    print("Too many failed attempts!")
    exit()

# Menu
while True:

    print("\n===== STUDENT RESULT ANALYSIS SYSTEM =====")
    print("1. View Database Statistics (DBMS)")
    print("2. Run COA Simulation")
    print("3. Run Statistics Analysis")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        dbms_analysis()

    elif choice == 2:
        coa_module()

    elif choice == 3:
        statistics_module()

    elif choice == 4:
        print("Project Finished")
        break

    else:
        print("Invalid Choice")




        # python main_project.py