clear
clc
% Name:Gerrik Labra
% Student ID: 914076227

% Lab 5: Genetic Drift and the Wright-Fisher Model
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations can be
% enterred as comments using the '%' symbol or output directly to
% the Command Window.

%% Part 1, Genetic Drift
N=10 %Population of humans
copies=2*N; %twenty copies of a gene in population, GENE POOL
A=8; %8 copies are allele A
B=copies-A; %B

% Q1: P(X0=A), or sample of gene pool

answers.q1=A/copies

% Q2:
answers.q2=(12/20)^2

% Q3:
k=8
NCK=nchoosek(copies,k);
p=A/copies;
pc=1-p;
prob_8A_nextgen=NCK*((p)^A)*((pc)^(copies-B));
answers.q3=binopdf(k,copies,p) %N=copies is gene pool, so what from gene pool will pass on.

% Q4:
answers.q4=1-answers.q3

% Q5:
%binopdf~=binocdf bino cumulative distribution function
answers.q5=1-binocdf(8,20,p)%probability of increase is 1-probability 8 - probability decrease=1-probability decrease from 8

% Q6:
chains=sim_wright_fisher(20,10,15,100);
GG=1;
subplot(3,3,GG)
plot(chains)
title("Question 6 Genetic Drift A");
xlabel('Generations')
ylabel('Copies allel A within population')
GG=GG+1;
%15 generations, 10 individuals at start, 50% of gene pool is allele A, 20
%individuals by end of 15 gnerations, then 20 simulations.


% Q7:
subplot(3,3,GG)
histogram(chains(2,:))
title("Question 7 1st Generation");
xlabel('Count A')
ylabel('Simulations with count')
GG=GG+1;

% Q8:
subplot(3,3,GG)
y=histogram(chains(end,:))
title("Question 8 15th Generation");
xlabel('Count A')
ylabel('Simulations with count A')
GG=GG+1;
something=histcounts(chains(end,:))
answers.q8=something(1)+something(end)
%% Part 3 Wright Fisher Model of Genetic Drift
%binopdf(k,n,p)
N = 4;
P= zeros(2*N+1, 2*N+1);
for i = 0:2*N
    P(i+1,:) = binopdf(0:2*N,2*N, i/(2*N));
end
pi0=zeros(1,2*N+1);
pi0(N+1)=1;
pi1=pi0*P;
subplot(3,3,GG)
bar(pi1)
GG=GG+1;


% Q9a:
N = 10;
P= zeros(2*N+1, 2*N+1);

for i = 0:2*N
    P(i+1,:) = binopdf(0:2*N,2*N, i/(2*N));
end
answers.q9a=P
% Q9b:
pi0=zeros(1, 2*N+1);
pi0(11)=1; %the 11th element corresponds to 10 alleles in gene pool
answers.q9b=pi0
% Q9c:
pi1=pi0*P;
subplot(3,3,GG)
bar(pi1)
title("Question 9c 1st Generation");
GG=GG+1;
% Q9d:
pi1=pi0*P^15;
subplot(3,3,GG)
bar(pi1)
title("Question 9d 15th Generation");
GG=GG+1;
% Q9e:
%The simulations do and dont exactly match. The simulations of question 6
%are almost unreadable, but theres heavy concentration of the final
%saturation around the center. Question 7 matches the results of the
%equation, in general shape. High density at the center. Question 8 also
%has similar characteristics to the eqaution, high counts on the edges.
%However, both have less uniformity, and higher variability in relation to
%the equation. This is detectable when the file is ran multiple times.

% Q10:
subplot(3,3,GG)
buri_data = csvread('buri_data.csv');
bar3(buri_data(2:end,:), 'w')
xlabel('Copies of Allele')
yticks(1:length(buri_data(:,1))-1)
xticks(1:33)
xticklabels(cellstr(num2str((0:32)')))
ylabel('Generation')
zlabel('Number of Observations')
GG=GG+1;

%Yes. Centerd at 50/50 at the start, or rather gene pool is centered around
%the initial ration at the first generation, then ends with completely
%with allele A or without allele A the most.

% Q11:

[chains,counts]=sim_wright_fisher(32,16,19,107)

chains=histcounts(chains)
subplot(3,3,GG)
bar3(counts(2:end,:),'w')
title("Question 11");
xlabel('Copies of Allele')
yticks(1:length(buri_data(:,1))-1)
xticks(1:33)
xticklabels(cellstr(num2str((0:32)')))
ylabel('Generation')
zlabel('Number of Observations')
GG=GG+1;

%Data is really similar. Its only difference is exact counts, but the
%patterns of the data match.
%% 

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