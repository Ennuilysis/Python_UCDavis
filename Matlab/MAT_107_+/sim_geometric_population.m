function N = sim_geometric_population(N0, R, probs, T)

C = cumsum(probs);
N = NaN(T, 1);
N(1) = N0;

for i = 1:T-1
    Rn = R(1+sum(C(end)*rand>C));
    N(i+1) = Rn*N(i);
end

end