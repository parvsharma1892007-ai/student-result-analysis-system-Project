import statistics

scores = [8,7,6,9,5,7,8,6,9,7]

mean_score = statistics.mean(scores)
median_score = statistics.median(scores)
mode_score = statistics.mode(scores)
stdev_score = statistics.stdev(scores)

print("Quiz Performance Statistics\n")

print("Scores:",scores)
print("Average Score:",mean_score)
print("Median Score:",median_score)
print("Mode Score:",mode_score)
print("Standard Deviation:",stdev_score)
scores = {
"Rahul":8,
"Aman":7,
"Priya":6,
"Riya":9,
"Karan":5
}

ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Student Ranking\n")

rank = 1

for student,score in ranking:
    print(rank,student,"Score:",score)
    rank += 1