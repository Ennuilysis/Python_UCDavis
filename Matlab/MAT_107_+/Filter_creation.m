%HW7 Question 3c
clc
P = zeros(11,11);
for i = 1:11
    for j = 1:11
        if j < 11
            lam = 1.5*(i-1);
            val = (exp(-lam)*(lam^(j-1))/factorial(j-1)); %PMF for poisson
            P(i,j) = val;
        elseif j == 11 %pik
            S = 1 - sum(P(i,:));
            P(i,j)= S; 
        end
           %sum(P(11, :)) checking  
    end
end
P
I=eye(10)
Q=P(2:end,2:end)
D=I-Q
BB=inv(D)
C=ones(10,1)
expectation_vector=BB*C
