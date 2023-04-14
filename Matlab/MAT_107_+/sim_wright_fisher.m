function [chains, counts] = sim_wright_fisher(N, N0, N_generations, N_sims)

chains = zeros(N_sims, N_generations+1);
counts = zeros(N+1, N_generations+1);

for i = 1:N_sims
    
    chains(i, :) = wright_fisher_sim_generations(N, N0, N_generations);
    
    for j = 1:N_generations+1
        counts(chains(i,j)+1, j) = counts(chains(i,j)+1, j) + 1;
    end
    
end

chains = chains';
counts = counts';

end

function trajectory = wright_fisher_sim_generations(N, N0, n_generations)

trajectory = N0; % Vector tracking changes in population
population_t = [ones(1, N0) zeros(1, N-N0)];

for t = 2:n_generations+1

    population_t = randsample(population_t, N, true);
    j = sum(population_t);
    
    trajectory(t) = j;

end
end