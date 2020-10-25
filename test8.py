in_line = input("Enter data: ")
data = in_line.split()
sum1 = 0
sum2 = 0
for x in range(len(data)+1):
    sum1 += x
avg = sum1/len(data)
for x in range(1,len(data)+1,1):
    sum2 += (x-avg)**2
sd = (sum2/len(data))**0.5
print("avg =", avg, "sd =", sd)



