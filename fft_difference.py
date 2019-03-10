#With fourier transform anf then 



from scipy.io import wavfile
#from scipy.fft import fft
import matplotlib.pyplot as plt
import numpy as np

path=input("Enter directory : ")

l=[]

def fft_plot(Input):
		fs, data= wavfile.read(Input)
		print(fs, data)
		a= data.T 
		b= [(ele/2**16.)*2-1 for ele in a ]
		c=np.fft.fft(b)
		d= len(c)//2

		return c,d



for i in range(2):

	plt.subplot(2, 1,1)
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, borderaxespad=0.)

	Input_file= "./"+ path+"/file"+str(i)+".wav"
	A, B= fft_plot(Input_file)
	plt.plot(A , label='test'+str(i))	

	plt.title('Fourier Tranform')
	plt.ylabel('Frequencies together')
	l.append(A)


	plt.plot(abs(A[:(B-1)]))
	print(l)




	

plt.subplot(2, 1,2)


l2=np.append(l[0], [0]*9727)

#print(len(l[0]) , len(l2), len(l[1]))

plt.plot(l2-l[1][:(B-1)], 'g')

plt.plot()
plt.xlabel('time')
plt.ylabel('Seperated')

plt.show()


