#TEAM code_wise

EN-GAME: Pronuncuation correction game which takes in voice input of the pronunciation of words from the user and compares it with the correct pronunciation of the word. User is then given points if the pronunciation is correct. After gaining some points, the user then is taken to the next level.

#HOW TO START
1. Run file record.py and give word inputs from your microphone under the given time frame of 2sec.
2. Run the file b_edit.py to produce spectograms of your pronunciation, the correct pronunciation and the difference in spectograms.
3. Run the file b_edit1.py to produce the spectograms using fourier transforms of the signals same as before.

#USE CASES
1. Preparation for interviews.
2. Teaching assisting teachers in schools.
3. Preparstion for competetive examinations.
4. Helpful for people in rural areas.

#DEPENDENCIES
1. pyaudio
2. scipy
3. matplotlib
4. numpy
5. pydub
6. pyQT5

#HOW THE APPLICATION WORKS
The user pronunciation and the correct pronunciation of a word are stored and spectograms for each signal is produced and compared. Before comparison the spectograms are normalised through the following steps:
1. Input voive signals taken from the user. 
2. Fourier transform of the input and the correct signals.
3. Blob detection algorithm to clip the significant parts the signals for correct comparison.
4. Check the pronunciation and assign points accordingly.

#HOW TO CONTRIBUTE
Just fork and go ahead!



