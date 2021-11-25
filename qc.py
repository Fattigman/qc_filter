import pandas as pd
import sys


def read_file(filename, **readKwargs):
    #reads file
    try:
        return pd.read_csv(filename, **readKwargs)
    except FileNotFoundError as e:
        print(e)
        raise Exception
    else:
        print('unexpected error')
      
    
def transform_df(df, originLen):
    try:
        origins = [x[1:1+originLen] for x in df['sample']]
        df['origin'] = origins
        return df
    except FileNotFoundError as e:
        print(e)
        raise Exception("I know python!")
    else:
        print('unexpected error')
        
        
def q_c(df):
    try:
        ans = {}
        for origin in df['origin'].unique():

            tempDf = df[df['origin'] == origin]['qc_pass'].value_counts()
            if tempDf.index[0] == True and len(tempDf) == 1:
                continue
            elif (fraction:= 1-tempDf[0] / tempDf.sum()) < 0.9:
                ans[origin] = fraction
        return ans
    
    except KeyError as e:
        print('The csv file is probably wrongly formatted!')
        raise Exception()

def main(fName = 'samples.txt', originLen = 1, **readKwargs):
    try:
        nl = '\n'    
        df = read_file(fName, **readKwargs)
        df = transform_df(df, originLen)
        ans = (q_c(df))
        if len(ans) > 0:
            print(f"Following origins did not pass the qc:{nl}{nl.join([f'{origin} with a fraction of {int(ans[origin]*100)}%' for origin in ans])} ")
        else:
            print('All origins passed the qc')
    except:
        print('Fix issues and rerun')
    finally:
        print('Test is done')

main(*sys.argv[1:])
