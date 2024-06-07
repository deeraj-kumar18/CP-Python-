def process_testcase(B,N,reserves,debentures):
    for debtor,creditor,value in debentures:
        reserves[debtor-1] -= value # deducting from debtor bank
        reserves[creditor-1] += value # adding to creditor bank
    
    for reserve in reserves:
        if reserve<0:  # if any reserve is negative, we cannot go forward with the plan.
            return "N"
    return "S"


results=[]
# processing input.
while True:
    B,N = map(int,input().split())

    reserves=list(map(int,input().split()))

    debentures=[]
    for i in range(N):
        D,C,V=map(int,input().split())
        debentures.append((D,C,V))

    result = process_testcase(B,N,reserves,debentures)
    results.append(result)
    print(results)

for res in results:
    print(result)



