import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def dataframe_clean(dataframe,column,snr=8.0,conf=0.9):
	dataframe.drop_duplicates(str(column),inplace=True)
	dataframe.sort_values(by=str(column),inplace=True)
	dataframe = dataframe[dataframe.confidence>=conf]
	dataframe = dataframe[dataframe.snr>=snr]
	dataframe = dataframe.reset_index(drop=True)
	
	return dataframe

def plotampsnr(dataframe,f1,snr1):
    
    
    plt.figure(figsize=(12,8))
    dataframe[(dataframe['peakFreq']>f1) & (dataframe.snr>snr1)].plot(x='snr',
                                y='amplitude',kind='scatter',fontsize=12,label='O3a',figsize=(12,8))
    
    plt.yscale('log')
    plt.xscale('log')
    plt.yticks(fontsize=18)
    plt.xticks(fontsize=18)
    plt.ylabel('Amplitude [strain \ $\sqrt{Hz}$]',fontsize=14)
    plt.xlabel('SNR',fontsize=14)
    #plt.xlim(snr1,1e5)
    plt.ylim(1e-24,1e-17)
    plt.title('O3a triggers frequency > {0} Hz'.format(f1),fontsize=16)
    plt.show()
    
    return
