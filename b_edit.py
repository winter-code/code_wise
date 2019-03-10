from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
path=input("Enter directory : ")

l=[]

for i in range(2):
	Input_file= "./"+ path+"/file"+str(i)+".wav"

	fs, data= wavfile.read(Input_file)
	l.append(data)
	print(fs)

	print(data)
	


	plt.subplot(2, 1, 1)

	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, borderaxespad=0.)

	plt.plot(data , label='test'+str(i))	
	plt.title('DIfference in spectrograms')
	plt.ylabel('Frequencies together')

plt.subplot(2, 1, 2)


l2=np.append(l[0], [0]*33280)

print(len(l[0]) , len(l2), len(l[1]))

plt.plot(l2-l[1], 'g')
plt.xlabel('time')
plt.ylabel('Seperated')

plt.show()


