from scipy import io as spio
import numpy as np
a=np.ones([3,3])

spio.savemat(r'C:\Users\Ranqing\Anaconda3\file.mat',{'first':a})

data = spio.loadmat(r'C:\Users\Ranqing\Anaconda3\file.mat',struct_as_record=True)


