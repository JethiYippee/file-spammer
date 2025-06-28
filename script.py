num_files = 1000  # Change this number to however many files you want

for i in range(1, num_files + 1):
    filename = str(i)
    open(filename, 'w').close()
