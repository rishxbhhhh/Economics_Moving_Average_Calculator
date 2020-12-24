print("SOLN:----------------------------------------------------------------------------------------------")
# input values
t = [100,150,200,300,400]
A = [20,18,15,12,5]
# predicted n quarter moving average
F = []
diffA_F = []
diffA_Fsq = []
n = 3
sum_t = sum_A = mean_t = mean_A = 0.0
for i in range(0,len(t)):
    sum_A = sum_A + A[i]
    sum_t = sum_t + t[i]
mean_A = sum_A / len(t)
mean_t = sum_t / len(t)
avgSum = 0.0
avg_round_sum = 0.0
for i in range(n,len(t)+1):
    avgSum = ( A[i-3] + A[i-1] + A[i-2] ) / n
    avg_round_sum = round(avgSum, 2)
    F.append(avg_round_sum) 
for i in range(n):
    F.insert(0,0.0)
k = 0.0
for i in range(0,len(F)-1):
    k = A[i] - F[i]
    diffA_F.append(round(k,2))
    diffA_Fsq.append(round(k*k,2))
rmse = 0.0
for i in range(n):
    diffA_F[i] = 0.0
    diffA_Fsq[i] = 0.0
sumdiffA_Fsq = 0.0
for i in range(len(F)-1):
    sumdiffA_Fsq = sumdiffA_Fsq + diffA_Fsq[i]
rmse = ( sumdiffA_Fsq / (len(t) - n) ) ** 0.5

print("T > ",end="        ")
print(t)
print("A  > ",end="       ")
print(A)
print("F  > ",end="       ")
print(F)
print("(A-F)  > ",end="   ")
print(diffA_F)
print("(A-F)^2  > ",end=" ")
print(diffA_Fsq)
print("Sum of sq of error > ",end=" ")
print(round(sumdiffA_Fsq, 2))
print("RMSE > ",end=" ")
print(round(rmse, 2))
print("Mean of A = %.2f" % round(mean_A, 2))
print("Mean of t = %.2f" % round(mean_t, 2))