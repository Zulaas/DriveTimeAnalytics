import datetime
import pandas as pd


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
    startIdx = findClosestIndex(start, df)
    values = df.loc[startIdx]
    end = calculateEndTime(values['Time'], rowEnd, start)
    timeDriven = datetime.timedelta(0)
    maxIdx = len(df.index)
    while start < rowEnd:
        if values['Value'] == 1:
            timeDriven += relativeDelta(start, end)
        start = end
        startIdx += 1
        if startIdx > maxIdx:
            raise Exception(f'IndexOutOf BoundException startIdx:{startIdx} than the max index of the df:{maxIdx}')
        values = df.loc[startIdx]
        end = calculateEndTime(values['Time'], rowEnd, start)
    return timeDriven


def getCycles():
    cycles = pd.read_csv("data/input/cycle_intervals_complete_2019_11.csv")
    cycles['Begin'] = pd.to_datetime(cycles['Begin'])
    cycles['End'] = pd.to_datetime(cycles['End'])
    return cycles


def getSensorBackward():
    backward = pd.read_csv("data/input/sensor_FW_Rückwärts_complete_2019_11.csv")
    backward['Time'] = pd.to_datetime(backward['Time'])
    return backward


def getSensorForward():
    forward = pd.read_csv("data/input/sensor_FW_Vorwärts_complete_2019_11.csv")
    forward['Time'] = pd.to_datetime(forward['Time'])
    return forward


def analyzeCycles(cycles, backward, forward):
    df = pd.DataFrame(columns=['timeDrivenBackward', 'timeDrivenForward'])
    for index, cycle in cycles.iterrows():
        timeDrivenBackward = countTimeDriven(cycle['Begin'], cycle['End'], backward)
        timeDrivenForward = countTimeDriven(cycle['Begin'], cycle['End'], forward)
        df = df.append({'timeDrivenBackward': timeDrivenBackward, 'timeDrivenForward': timeDrivenForward}, ignore_index=True)
    return df


def calculateAverageAndWriteFiles(df, cycles):
    result = pd.concat([cycles, df], axis=1)
    result.to_csv('data/output/DriveTimePerCycle.csv', sep=',', index=False)
    averagePerMonth = df.mean()
    dict = {'AveragePerMonthBackwards': averagePerMonth['timeDrivenBackward'],
            'AveragePerMonthForward': averagePerMonth['timeDrivenForward']}
    df2 = pd.DataFrame(dict, index=[1])
    df2.to_csv('data/output/AveragePerMonth.csv', sep=',', index=False)
    # Todo pro Schicht / Tag / Stunde
    # Todo Zeit pro Cycle ab dem gefahren wird (wenn dort ein Zusammenhang besteht)


def main():
    cycles = getCycles()
    backward = getSensorBackward()
    forward = getSensorForward()
    df = analyzeCycles(cycles, backward, forward)
    calculateAverageAndWriteFiles(df, cycles)


main()
