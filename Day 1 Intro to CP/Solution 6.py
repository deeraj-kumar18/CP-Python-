# Refer to Q6
while True:
    num=input().strip()
    if num=="END":
        break

    count=0
    while True:
        next_num=str(len(num))  # Calculate number of digits and convert to string
        count+=1
        if next_num==num:
            break
        num=next_num
        
    print(count)
