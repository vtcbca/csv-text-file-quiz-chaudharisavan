bca_info = """BCA Course Information:Bachelor of Computer Applications (BCA) is a 3-year undergraduate program."""
with open('BCA.txt', 'w') as bca_file:
    bca_file.write(bca_info)
    row= {'A': 0, 'B': 0, 'C': 0}
    with open('BCA.txt', 'r') as BCA_file:
        lines = BCA_file.readlines()
        for line in lines:
            f_char = line.strip()[0]
        if f_char in row:
            row[f_char] +=1
    for char, count in row.items():
        print(f"Number of lines starting with '{char}': {count}")
