import datetime
import pandas as pd


def findClosestIndex(search, df):
    idx = (df['Time'] - search).abs().idxmin()
    values = df.loc[idx]
    if values['Time'] > search:
        idx -= 1
    return idx


def relativeDelta(start, end):
    timeDelta = end - start
    return timeDelta


def calculateEndTime(endToTest, absolutEnd):
    end = endToTest
    if endToTest > absolutEnd:
        end = absolutEnd
    return end


def countTimeDriven(start, rowEnd, df):
    startIdx = findClosestIndex(start, df)
    values = df.loc[startIdx]
    end = calculateEndTime(values['Time'], rowEnd)
    timeDriven = datetime.timedelta(0)
    while start < rowEnd:
        if values['Value'] == 1:
            timeDriven += relativeDelta(start, end)
        start = end
        startIdx += 1
        values = df.loc[startIdx]
        end = calculateEndTime(values['Time'], rowEnd)
    return timeDriven


def main():
    # import data
    cycles = pd.read_csv("data/cycle_intervals_complete_2019_11.csv")
    cycles['Begin'] = pd.to_datetime(cycles['Begin'])
    cycles['End'] = pd.to_datetime(cycles['End'])

    backward = pd.read_csv("data/sensor_FW_Rückwärts_complete_2019_11.csv")
    backward['Time'] = pd.to_datetime(backward['Time'])
    forward = pd.read_csv("data/sensor_FW_Vorwärts_complete_2019_11.csv")
    forward['Time'] = pd.to_datetime(forward['Time'])

    for index, cycle in cycles.head().iterrows():

        timeDrivenBackward = countTimeDriven(cycle['Begin'], cycle['End'], backward)
        timeDrivenForward = countTimeDriven(cycle['Begin'], cycle['End'], forward)
        print(f'{timeDrivenBackward}  {timeDrivenForward}')


            # ist nächster index ausser der ist wieder ein anderer
        # print in csv an repeat for forward

        #Todo: idx ende muss auch definiert sein
        #Todo: idx anfang auch
        print(" ")


main()

# count seconds from row['Begin'] till backwardClosestBeforeIdx += 1 aber nur wenn value von backwardClosestBeforeIdx = 1 ist
# wenn die null ist tu nix weil dann hat sich die maschine nicht bewegt
# same mit row['End']
