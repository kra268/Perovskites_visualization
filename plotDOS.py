import numpy as np
import matplotlib.pyplot as plt
'''
data_1 = np.loadtxt('BNH3.dat')
plt.figure(1)
plt.plot(data_1[7930:10000, 0], data_1[7930:10000, 1], label='Sn(p)', c='grey') # Tin (p)
plt.plot(data_1[12925:15000, 0], data_1[12925:15000, 1], label='I(p)', c='violet') # Iodine (p)
plt.plot(data_1[2940:5000, 0], data_1[2940:5000, 1], c='forestgreen') # Total DOS
plt.legend()
plt.xlabel("Energy (eV)",fontstyle='normal', c='black',fontfamily='sans-serif',fontweight='bold')
plt.ylabel("Density (states/eV)",fontstyle='normal', c='black',fontfamily='sans-serif',fontweight='bold')
plt.title("Anilinium",fontweight="bold")

plt.ylim(0)
plt.xlim(-4,5) # Sets a limit
plt.yticks([]) # Removes y axis numbers
plt.xticks(np.arange(-4,5,1))
#plt.savefig('Anilinium_Sn_I_states.png',dpi = 300)
'''
plt.figure(2)
data_2 = np.loadtxt('BF5NH3_C_N_F.dat')
plt.plot(data_2[7930:10000, 0], data_2[7930:10000, 1], label='N(p)', c='skyblue') # C(p) DOS
plt.plot(data_2[12925:15000, 0], data_2[12925:15000, 1], label='C(p)', c='peru') # N(p) DOS
plt.plot(data_2[17925:20000, 0], data_2[17925:20000, 1], label='F(p)', c='royalblue') # F(p) DOS
plt.plot(data_2[2940:5000, 0], data_2[2940:5000, 1], c='forestgreen') # Total DOS
plt.legend()
plt.xlabel("Energy (eV)",fontstyle='normal', c='black',fontfamily='sans-serif',fontweight='bold')
plt.ylabel("Density (states/eV)",fontstyle='normal', c='black',fontfamily='sans-serif',fontweight='bold')
plt.title("2,3,4,5,6-FAn",fontweight="bold")

plt.ylim(0)
plt.xlim(-4,5) # Sets a limit
plt.yticks([]) # Removes y axis numbers
plt.xticks(np.arange(-4,5,1))
plt.savefig('BF5NH3_C_N_F_states.png',dpi=300)
plt.show()
