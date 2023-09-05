print("Input string")
str = input()
result_str = ""
for i in str:
    if i <= 'A' or i >= 'Z':
        result_str = result_str + i
    else:
        result_str = result_str + ""
print(result_str)