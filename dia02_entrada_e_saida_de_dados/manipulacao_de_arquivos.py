persons = open("persons.txt", mode="w")

persons.write("Naruto\n")
persons.write("Sasuke\n")
persons.write("Sakura\n")


persons.close()

persons = open("persons.txt", mode="r")
content = persons.read()
print(content)
for line in content:
    print(f"badass character:{line}")

persons.close()