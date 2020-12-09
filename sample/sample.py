import pandas as pd


def main():
    cycles = pd.read_csv("data/cycle_intervals_complete_2019_11.csv")
    backward = pd.read_csv("data/sensor_FW_Rückwärts_complete_2019_11.csv")
    forward = pd.read_csv("data/sensor_FW_Vorwärts_complete_2019_11.csv")
    print(cycles.head())
    print(backward.head())
    print(forward.head())



main()

# parse given parameters
# time as from and to
# test or real

# get all Cycles in given time
# here from data future versions from database
# unterscheidung dort nach test and real für den gewählten treiber
