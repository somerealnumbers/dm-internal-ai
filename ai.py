import pandas as pd
import os
import insight

def main():

    data = pd.read_csv("./data.csv")

    def ai(data):
        return insight(data)

    print("INSIGHT PRODUCED")


if __name__ == "__main__":
    main()
