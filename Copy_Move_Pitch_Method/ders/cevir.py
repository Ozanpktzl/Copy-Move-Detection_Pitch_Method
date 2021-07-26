import numpy as np
import scipy


class Sinyal(object):
  def __init__(self,name):
      from scipy.io import wavfile

      self.fs,self.data=wavfile.read(name)
      self.name = name
      fs=self.fs
      data=self.data
      output_dtype="f"

      data=flotingPoint(data, output_dtype)

      self.data = data
      uzunluk = len(self.data)
      self.uzunluk = uzunluk
      self.enerji=0
      self.kontrol=1
  def karaliSinyal(self,veri):
     self.data=veri

 

def flotingPoint(veri,output_dtype):

    veri = np.asarray(veri)
    out_dtype = np.dtype(output_dtype)

    return veri.astype(out_dtype) / out_dtype.type(-np.iinfo(veri.dtype).min)











