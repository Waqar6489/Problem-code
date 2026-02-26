# file handling 

with open("Students.txt", "w") as file:                      # w for write in students.txt file
    file.write(" Waqar Ali\n Muhammad Ali\n Ahsan Ali\n Ali Raza\n Ali Hassan\n")
with open("Students.txt", "r") as file:                   # r for read the students.txt file
    content = file.read()
    print(f"Your Sample Names here:\n{content.upper()}")