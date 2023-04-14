function [ chain ] = sim_MC( A, X0, N )

chain = [X0 NaN(1, N-1)];
indices = 1:size(A,1);

for i = 2:N
    
    probs = A(chain(i-1),:);
    C = cumsum(probs);
    chain(i) = indices(1+sum(C(end)*rand>C));

end

end