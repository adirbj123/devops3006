my_file = open("read_this.txt")
print(list(my_file.readlines()))
my_file.seek(0)
for line in my_file.readlines():
    print(line)