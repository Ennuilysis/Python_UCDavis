# Solve for the determinant for the F matrix/ Lamda max

import numpy as np

# Import R1(123), R2(123),R3(123)

R11 = 1
R12 = 2
R13 = 3
R21 = 4
R22 = 5
R23 = 6
R31 = 7
R32 = 8
R33 = 9



# Define matrix element

# Row 1 --> a
a1 = R11 + R22 + R33
a2 = R23 - R32
a3 = R31 - R13
a4 = R12 - R21
# Row 2 --> b
b1 = R23 -R32
b2 = R11 - R22 -R33
b3 = R12 + R21
b4 = R13 + R31
# Row 3 --> c
c1 = R31 - R13
c2 = R12 + R21
c3 = -R11 + R22 - R33
c4 = R23 + R32
# Row 4 --> d
d1 = R12 - R21
d2 = R13 + R31
d3 = R23 + R32
d4 = -R11 - R22 + R33


# Calculate determinant of F matrix

F = np.array([[a1,a2,a3,a4],[b1,b2,b3,b4],[c1,c2,c3,c4],[d1,d2,d3,d4]])
print("F =",F)
det = np.linalg.det(F)
print("\nDeterminant:",np.round(det))


