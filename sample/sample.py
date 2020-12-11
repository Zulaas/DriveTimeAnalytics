import datetime
import pandas as pd


# Todo what is with idx equals 0 but the value is bigger than the search value ?
def findClosestIndex(search, df):
    idx = (df['Time'] - search).abs().idxmin()
    values = df.loc[idx]
    if values['Time'] > search:
        if idx == 0:
            raise Exception(f'idx:{idx} is zero that causes a '
                            f'IndexOutOfBoundException in further processing check data')
        idx -= 1
    return idx


def relativeDelta(start, end):
    if start > end:
        raise Exception(f'start:{start} can`t be greater than end:{end}')
    timeDelta = end - start
    return timeDelta


def calculateEndTime(endToTest, absolutEnd, absolutStart):
    end = endToTest
    if (endToTest > absolutEnd) or (endToTest < absolutStart):
        end = absolutEnd
    return end


def countTimeDriven(start, rowEnd, df):
    absolut = start
    startIdx = findClosestIndex(start, df)
    values = df.loc[startIdx]
    end = calculateEndTime(values['Time'], rowEnd, start)
    timeDriven = datetime.timedelta(0)
    while start < rowEnd:
        if values['Value'] == 1:
            timeDriven += relativeDelta(start, end)
        start = end
        startIdx += 1
        # Todo idx should not be bigger than the end index in the dataframe
        values = df.loc[startIdx]
        end = calculateEndTime(values['Time'], rowEnd, absolut)
    return timeDriven


def getCycles():
    cycles = pd.read_csv("data/cycle_intervals_complete_2019_11.csv")
    cycles['Begin'] = pd.to_datetime(cycles['Begin'])
    cycles['End'] = pd.to_datetime(cycles['End'])
    return cycles


def getSensorBackward():
    backward = pd.read_csv("data/sensor_FW_Rückwärts_complete_2019_11.csv")
    backward['Time'] = pd.to_datetime(backward['Time'])
    return backward


def getSensorForward():
    forward = pd.read_csv("data/sensor_FW_Vorwärts_complete_2019_11.csv")
    forward['Time'] = pd.to_datetime(forward['Time'])
    return forward


def analyzeCycles(cycles, backward, forward):
    for index, cycle in cycles.iterrows():
        timeDrivenBackward = countTimeDriven(cycle['Begin'], cycle['End'], backward)
        timeDrivenForward = countTimeDriven(cycle['Begin'], cycle['End'], forward)
        # Todo print in csv an repeat for forward
        print(f'timeDrivenBackward: {timeDrivenBackward} timeDrivenForward: {timeDrivenForward}')


def main():
    # import data
    cycles = getCycles()
    backward = getSensorBackward()
    forward = getSensorForward()
    analyzeCycles(cycles, backward, forward)


main()
