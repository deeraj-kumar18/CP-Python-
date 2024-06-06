# Refer Question text file.
n=int(input()) # taking input of testcases 
for j in range(n): 
    dict={} # dict to store rank as key and website as value.
    for i in range(10): #  in each testcase we have ten entries.
        a=input().split(" ") 
        if int(a[-1]) in dict.keys(): # checking if the number is already as a key, if yes we add to the list.
            dict[int(a[-1])]+=[a[0]]
        else:
            dict[int(a[-1])]=[a[0]]  
        
    keys=dict.keys()  # list of keys.
    print(f"Case #{j+1}:")
    for i in keys:
        if i == max(keys):
            for a in dict[i]:
                print(a)
            