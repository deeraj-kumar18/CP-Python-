# REFER TO QUESTION 5.
def test_check(n,m,c,devices,operations):
    device_states=[False]*n # initially all devices are turned Off.
    current_consumption=0
    max_consumption=0
    fuse_blown=False

    for operation in operations:
        device_index=operation-1  # as the numbers in the list are 1-indexed, we are converting into 0-indexed.
        if device_states[device_index]==True: # if device is on, we turn it off and subtract consumption value.
            current_consumption-=devices[device_index]
        else: # if device is off, we turn it on and add the consumption value
            current_consumption+=devices[device_index]

        device_states[device_index] = not device_states[device_index]

        if current_consumption>c: # checking fuse blow out condition
            fuse_blown=True
            break

        if current_consumption>max_consumption:
            max_consumption=current_consumption
    
    return fuse_blown,max_consumption


testcase=1
# reading input
while True:
    n,m,c=map(int,input().split()) # n=no. of devices, m=no. of operations, c=capacity of device
    if n==m==c==0:
        break
    devices=[]  #adding consumption of devices to a list.
    for i in range(n):
        consumption=int(input())
        devices.append(consumption)

    operations=[]  # adding operations of devices to a list.
    for i in range(m):
        operation=int(input())
        operations.append(operation)
    
    fuse_blown,max_consumption=test_check(n,m,c,devices,operations)
    print(f"Sequence {testcase}")
    if fuse_blown:
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print(f"Maximal power consumption was {max_consumption} amperes.")
    print()
    testcase+=1



