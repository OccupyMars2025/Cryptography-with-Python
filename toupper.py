filepath_in = input('Enter input filepath:')
filepath_out = input('Enter output filepath')
f_read = open(filepath_in, 'r')
f_write = open(filepath_out, 'w')

for line in f_read.readlines():
    for letter in line:
        if letter.islower():
            letter = letter.upper()
        f_write.write(letter)