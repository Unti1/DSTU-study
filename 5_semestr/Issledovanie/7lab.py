import nashpy as nash
import numpy as np

P1=np.array([[3,0,3],[4,1,1],[4,1,1]])
P2=np.array([[3,4,9],[0,1,3],[4,1,0]])
P3=np.array([[3,2,9],[0,3,3],[4,1,2]])
prisoner_dilemma=nash.Game(P1,P2,P3)
print(prisoner_dilemma)