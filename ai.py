import pandas as pd
import insight


def main():

    # reading in the data
    data = pd.read_csv("./data.csv")

    # defining the ai function
    def ai(data):
        return insight(data)

    # exit message
    print("INSIGHT PRODUCED")


if __name__ == "__main__":
    main()
