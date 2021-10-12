import pandas as pd
import insight


def main():

    # reading in the data
    data = pd.read_csv("./data.csv")

    # defining the ai function
    def ai(data):
        return insight(data)

    # what is the insight?
    y = ai(data=data)

    # print the insight
    print(y)

    # create a plot
    y.plot()

    # exit message
    print("INSIGHT PRODUCED. GOODBYE")


if __name__ == "__main__":
    main()
