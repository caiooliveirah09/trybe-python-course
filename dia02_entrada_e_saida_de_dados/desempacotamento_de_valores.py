a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = (1, 2, 3) # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]

name, email, age, *rest = ("caio", "email@email.com", 19, "test 1", "test 2", "test 3")
print(name)
print(email)
print(age)
print(rest)