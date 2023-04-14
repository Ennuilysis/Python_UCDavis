format short

A1 = [2/3 4/3 5/2]
format rat
A1 = [2/3 4/3 5/2]
format short
A1 = [2/3 4/3 5/2]
format long
A1 = [2/3 4/3 5/2]
fix(A1)
help format
A = [1 2 3 4; 4 5 6 5; 6 6 6 5; 2 1 4 7]
B1 = tril(A)
B2 = tril(A, 1)
B3 = tril(A, -1)
B4 = tril(A, -2)
B5 = tril(A, 0)
B6 = tril(A, 2)
C1 = triu(A)
C2 = triu(A, 1)
C3 = triu(A, -1)
C4 = triu(A, -2)
C4 = triu(A, 0)
C5 = triu(A, 1)
C6 = triu(A, 2)
B=[ 2 2 2 2 ; 3 3 4 3; 5 5 1 1 ; 2 -1 2 0 ]
C=ones(4)
A+B
5*C
A^2
A-3*B
U= round( 10 * rand(5))
V= round( 10 * rand(5))
W= round( 10 * rand(5))
L = tril(U)
K = tril(V )
J = triu(V )
L - K
3*L+5*K
L*K
K*L
K^3
J+K
5*J
J^2
% a.) Explain: What type of matrix are you getting? Is it lower triangular, upper triangular, or other type
% that you know?
% a.) L is lower triangular, K is same, and J is upper 
% 1st computation is lower triangular
% 2nd is same
% 3rd is same
% 4th is same
% 5th is same
% 6th is a square matrix
% 7th is a upper triangular
% 8th is same
% b.) No. The elements of the upper triangular matrix of both matrices are
%zero. The sum of the elements would also be zero.
% c.) It is the multiplication of a lower triangular matrix, preceded by an
% if statement to check that the matrix matches the value pattern of a
% lower triangular matrix.
% d.) Yes. It is the direct multiplication of each value of the matrix by
% the corresponding indexed value in the other matrix, will result in a
% lower triangle, since both matrices are lower triangles. 0*0=0, and
% number*number=number.
% e.1)
bab=J*5
J+bab
%e.2)
J*bab
%e.3)
J-bab
%e.4)
J.*bab
%FIN
D=diag(diag(A))
E=diag(diag(B))
% a.)
D+E
% a.1) I am getting a diagonal matrix
% a.2) D+E=diagonal(D+E)
% a.3) 
% b.)
D-E
% c.)
D*E
% d.)
E*D

% 1.) Explain what type of matrix are you getting?
% I am creating diagonal matrices
% 2.) Can you make a statement to generalize this fact?
% a=matrix_class(D+E,D-E,D*E,E*D)
% a=diagonal
% 3.) Is it possible to get a non diagonal matrix from adding or multiplying diagonal matrices?
% If its a diagonal unit matrices, where all values in all matrices are the
% same in each matrix, but different to each matrix, yes. It just requires
% coefficients. Or, an inverse diagonal matrix could work.
% 4.) Can we obtain a diagonal matrix by multiplying two non-diagonal matrices? Give an example
%no
a=[2,3,4;4,5,3;3,2,3]
b=[8,1/3,1/4;1/4,8,1/3;1/3,1/2,9]
c=a*b
% 5.) Can we obtain a diagonal matrix by adding two non-diagonal matrices? Give an example
%Yes
b=[8,-3,-4;-4,6,-3;-3,-2,8]
a+b
M = [1 1 2 5; 1 7 3 -4; 2 3 8 1; 5 -4 1 9]
M'
M==M'
M==-M'
M = [0 1 -2 5; -1 0 3 -4; 2 -3 0 6; -5 4 -6 0]
M'
M==-M'
S=A+A'
T=B+B'
R=A-A'
S+T
S-T
S*T
T*S
% a.) Which one of these matrices are symmetric?
%S+T and S-T are symmetric
% b.) What type of matrix will we get if we add (multiply ) two symmetric matrices?
%If we add 2 symmetric matrices, they will be symmetric. If we multiply, we
%get a non symmetrical array.
% c.) Can we get symmetric matrices by adding two non-symmetric matrices?
% Sometimes, yes. The sum of the matrices must result in symmetry.
X = [ 2 4 -2; 3 5 0 ] \ [0; 1]
AG= [ 2 4 -2 0; 3 5 0 1; 4 8 -4 3]
rref(AG)
AC = [2,4,-2; 3,5,0; 4,8,-4]
b = [0 1 3]'
X = AC\b
%I interpret that Matlab cannot compute a solution to the matrix.
rref([AC,b])
%The ouctomes of using rref and \ are different and do not agree.
A=[1,-1,-2;2,1,3;2,3,0]
B=[3,6,7]'
X=A\B
rref([A,B])
