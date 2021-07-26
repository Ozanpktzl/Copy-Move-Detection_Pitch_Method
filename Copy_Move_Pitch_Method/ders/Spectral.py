import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import mlab as ml

class energy(object):
    def __init__(self,veri,fs,param):
        nfft = param['fft_length']
        n_fo_min = np.around((param['f0_min'] * 2 / fs) * nfft)
        n_fo_max = np.around((param['f0_max']  / fs) * nfft)

        frame_size=int (np.fix(param['frame_length']*fs/1000))
        frame_jump=int(np.fix(param['frame_space']*fs/1000))
        noverlap=frame_size-frame_jump
        nlfer_thersh1=param['nlfer_thresh1']

        window= signal.windows.hann(frame_size+2)[1:-1]
        self.frame_size=frame_size
        self.frame_jump=frame_jump
        self.noverlap=noverlap
       
        sp=signal.spectrogram(veri,fs,nfft=nfft, noverlap=noverlap,scaling='spectrum',mode='magnitude',window=window)


        temp=sum(np.abs(sp[2][int(n_fo_min):int(n_fo_max)]))
       
        ortalamaEnerji=np.mean(temp)
       
        self.enerji=temp/ortalamaEnerji
       
        self.frameKontrol = (self.enerji > nlfer_thersh1);

     

