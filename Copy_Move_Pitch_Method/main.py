import numpy as np
from ders import cevir as cev 
from ders import Spectral as spec
import wave
from scipy.signal import butter, lfilter
import scipy
from scipy.linalg import dft
from matplotlib import pyplot as plt

parametre = {'frame_length': 15.0, 'tda_frame_length': 35.0, 'frame_space': 5.0, 'f0_min': 60.0, 'f0_max': 400.0,
             'fft_length': 8192, 'bp_order': 150, 'bp_low': 50.0, 'bp_high': 1500.0, 'nlfer_thresh1': 0.75,
             'nlfer_thresh2': 0.1, 'shc_numharms': 3, 'shc_window': 40.0, 'shc_maxpeaks': 4, 'shc_pwidth': 50.0,
             'shc_thresh1': 5.0, 'shc_thresh2': 1.25, 'f0_double': 150.0, 'f0_half': 150.0, 'dp5_k1': 11.0,
             'dec_factor': 1, 'nccf_thresh1': 0.3, 'nccf_thresh2': 0.9, 'nccf_maxcands': 3, 'nccf_pwidth': 5,
             'merit_boost': 0.20, 'merit_pivot': 0.99, 'merit_extra': 0.4, 'median_value': 7, 'dp_w1': 0.15,
             'dp_w2': 0.5, 'dp_w3': 0.1, 'dp_w4': 0.9, 'spec_pitch_min_std': 0.05}

sinyal = cev.Sinyal("sample.wav")



kareSinyal = cev.Sinyal("sample.wav")
cev.Sinyal.karaliSinyal(kareSinyal, kareSinyal.data ** 2)



"""class BandPassFilter(object):
    def __init__(self,fs,param):
     fs_min = 1000.0

     filter_order=param['bp_forder']
     highcut=param['bp_low']
     lowcut=param['bp_high']

     if (fs > fs_min):
         dec_factor = param['dec_factor']
     else:
        dec_factor = 1


     nyq = fs/2

     f1 = highcut / nyq
     f2 = lowcut / nyq


     b=scipy.signal.firwin(filter_order+1,[f1,f2],pass_zero=False)
     self.b=b
     a=1
     self.a=a
     self.dec_factor=dec_factor
     self.fs=fs
"""




def BandPassFilter(data, fs, param):


    filter_order = param['bp_order']
    highcut = param['bp_low']
    lowcut = param['bp_high']


    nyq = fs / 2
    low = highcut / nyq
    high = lowcut / nyq

    b= scipy.signal.firwin(filter_order + 1, [low, high], pass_zero='bandpass')
    a = 1
    temp = lfilter(b, a, data)
    return (temp)


"""filtre=BandPassFilter(filKareSinyal.fs,parametre)
temp=lfilter(filtre.b,filtre.a,filKareSinyal.data)
filKareSinyal.data=temp[0:filKareSinyal.uzunluk:filtre.dec_factor]
filKareSinyal.fs=filtre.fs/filtre.dec_factor
"""

filSinyal = cev.Sinyal("sample.wav")
filKareSinyal = cev.Sinyal("sample.wav")
cev.Sinyal.karaliSinyal(filKareSinyal, filKareSinyal.data ** 2)

filKareSinyal.data = BandPassFilter(filKareSinyal.data, filKareSinyal.fs, parametre)
filSinyal.data = BandPassFilter(filSinyal.data, filSinyal.fs, parametre)

enerji=spec.energy(filKareSinyal.data,filKareSinyal.fs,parametre)
np.set_printoptions(precision=5, suppress=True)
dftt=np.array(enerji)
m=dft(178)
m.dot(dftt)
print("el")
def bandPassFilter(signal):
    fs = 16000
    lowcut = 50.0
    highcut = 1500.0

    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    order = 2
    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.lfilter(b, a, signal, axis=-1)

    return (y)


sinyal.data = bandPassFilter(sinyal.data)
kareSinyal.data = bandPassFilter(kareSinyal.data)

plot_a = plt.subplot(211)
plot_a.plot(kareSinyal.data)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plt.show()

plot_a = plt.subplot(211)
plot_a.plot(sinyal.data)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plt.show()

plot_a = plt.subplot(211)
plot_a.plot(filKareSinyal.data)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plt.show()

plot_a = plt.subplot(211)
plot_a.plot(filSinyal.data)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plt.show()






plot_a = plt.subplot(211)
plot_a.plot(kareSinyal.data)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

plot_b = plt.subplot(212)
plot_b.specgram(kareSinyal.data, NFFT=1024, Fs=sinyal.fs, noverlap=900)
plot_b.set_xlabel('Time')
plot_b.set_ylabel('Frequency')

plt.show()



