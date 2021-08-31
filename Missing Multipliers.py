num = int(input("Times table: "))
step = int(input("Step: "))

for a in range(1, 13, step):
    answer = a * num
    print(f"{num} x [] = {answer}")

#Shows your time tables