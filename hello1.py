print("hello World")

def generate_ID(x):
    with open("txt/Class.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0].startswith("M"):
                return data