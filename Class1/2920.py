input_list = list(input().split())
if input_list == sorted(input_list):
    print("ascending")
elif input_list == sorted(input_list, reverse=True):
    print("descending")
else:
    print("mixed")