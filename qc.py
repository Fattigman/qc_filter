import pandas as pd
import sys


def readFile(filename, **readKwargs):
    #reads file, takes unlimited amount of keyword arguments into read_csv file
    try:
        return pd.read_csv(filename, **readKwargs)
    except FileNotFoundError as e:
        print(e)
        raise Exception()
    else:
        print('unexpected error')
        raise Exception()
      
    
def addOriginColumn(df):
    #Creates a column of the origin to corresponding sample
    try:
        origins = [x.split('-')[0][1:] for x in df['sample']]
        df['origin'] = origins
        return df
    except KeyError as e:
        print(f'Could not find Key in csv file: {e}. Make sure it is included')
        raise Exception()
    else:
        print('unexpected error')
        raise Exception()
        
        
def filterQC(df):
    #Filter a dataframe based qc of each origin specified in the origin column
    #returns the origins that didn't pass the the qc filter (falls below a threshold of 90%)
    try:
        notPass = {}
        for origin in df['origin'].unique():

            tempDf = df[df['origin'] == origin]['qc_pass'].value_counts()
            if tempDf.index[0] == True and len(tempDf) == 1:
                continue
            elif (fraction:= 1-tempDf[0] / tempDf.sum()) < 0.9:
                notPass[origin] = fraction
        return notPass
    
    except KeyError as e:
        print(f'Could not find Key in csv file: {e}. Make sure it is included')
        raise Exception()
    else:
        raise Exception()

def main(fName = 'samples.txt', **readKwargs):
    try:
        nl = '\n'    
        df = readFile(fName, **readKwargs)
        df = addOriginColumn(df)
        notPass = (filterQC(df))
        if len(notPass) > 0:
            print(f"Following origins did not pass the qc:{nl}{nl.join([f'{origin} with a fraction of {int(notPass[origin]*100)}% that passed qc' for origin in notPass])} ")
        else:
            print('All origins passed the qc')
    except:
        print('Fix issues and rerun')
    finally:
        print('Test is done')

main(*sys.argv[1:])
