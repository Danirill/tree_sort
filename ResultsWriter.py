
def print(n, iterations):
    with open("output.csv", "a") as csv_file:
        line = f"{n},{iterations}"
        csv_file.write(line + "\n")


