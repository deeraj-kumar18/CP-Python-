# TEX QOUTES
print("Welcome to Tex Qoutes Editor.")
print("Please enter your input:")
all_input=[]
while True:
    try:
        line=input()
        all_input.append(line)
    except EOFError:
        break

answer=""
flag=True
for line in all_input:
    for char in line:
        if char == '"':
            if flag:
                answer+='``'
            else:
                answer+="''"
            flag=not flag
        else:
            answer+=char
    answer+="\n"

print(answer)