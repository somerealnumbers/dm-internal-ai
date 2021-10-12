import pandas as pd
import insight
import numpy as np


def main():

    # CHANGE

    # reading in the data
    dat = pd.read_csv("./data.csv")

    # defining the ai function
    def ai(data):
        """ the genius ai function """
        return insight(data)

    # what is the insight?
    y = ai(data=dat)

    # print the insight
    print(y)

    # create a plot
    y.plot()

    # exit message
    print("INSIGHT PRODUCED. GOODBYE")
    
    # CHANGE


if __name__ == "__main__":
    main()
