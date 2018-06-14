#文件读取练习
with open(r'data/pi_digits.txt') as file_object:
  #  contents = file_object.read()
  #  print(contents)
   # print(contents.rstrip())
    lines = []
    for line in file_object:
        lines.append(line.rstrip())
for x in lines:
    print(x)
