from scipy import io as spio

spio.savemat(r'C:\Users\Ranqing\Anaconda3\file.mat',{'first':a})

data = spio.loadmat(r'C:\Users\Ranqing\Anaconda3\file.mat',struct_as_record=True)
