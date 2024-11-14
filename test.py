import pandas as pd

Data = [
    {"Name":"Anant", "age":28, "city":"Saharsa"},
    {"Name":"Mohan", "age":29, "city":"Patna"},
    {"Name":"Somnath", "age":30, "city":"Dhabauli"},
    {"Name":"Prabhat", "age":31, "city":"Samastipur"},
]

Data = pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)