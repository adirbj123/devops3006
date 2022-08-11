import ast
my_file = open("config.json")
c =  dict(ast.literal_eval(my_file.read()))
if c["name"] == "adir":
print("i love devops experts")


with open("names.txt", "a+") as my_file:
    for name in my_file.readlines():
        print(names.strip())