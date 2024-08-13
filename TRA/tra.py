#II.Verstärkung der Emitterschaltung
#5.5kHz 

#1. Messung mit C_E und ohne R_L

U_E = 20.4 #mV
Widerstand_mitCE_ohne_RL = np.array([1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6, 7, 8, 9, 10])
#in kiloohm
U_A_mitCE_ohne_RL = np.array([0.456, 0.644, 0.856, 1.07, 1.27, 1.46, 1.66, 1.84, 2.10, 2.46, 2.88, 3.28, 3.64, 4.08])

# 2. Messung ohne C_E und ohne R_L 
#U_E = 20.4 #mV, also gleich wie davor
Widerstand_ohneCE_ohne_RL = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
U_A_mitCE_mit_RL = np.array([24.4, 43.6,  63.2, 84, 102, 141, 162, 180, 198]) # In mV !!!

#3. Messung mit C_E und mit R_L = 10kOhm

#U_E = 20.4 #mV, also gleich wie davor
Widerstand_mitCE_mit_RL = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
U_A_mitCE_ohne_RL = np.array([0.404, 0.7, 0.960, 1.18, 1.38, 1.56, 1.68, 1.84, 1.94, 2.06]) #V