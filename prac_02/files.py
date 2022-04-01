out_file = open('prac_02/name.txt', 'w')
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

in_file = open('prac_02/name.txt', 'r')
your_name = in_file.read()
print("Your name is", your_name)
in_file.close()

in_file_2 = open('prac_02/numbers.txt', 'r')
first_line = int(in_file_2.readline())
second_line= int(in_file_2.readline())
in_file_2.close()
print(f"{first_line} + {second_line} = {first_line + second_line}")

total = 0
in_file_3 = open('prac_02/numbers.txt', 'r')
for line in in_file_3:
    total += int(line)
in_file_3.close()
print(f"Total is {total}")

