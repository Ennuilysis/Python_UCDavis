clear
clc
% Name:Gerrik Labra
% Student ID: 914076227

% Lab 6: Limiting Behavior of Markov Chains
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations can be
% enterred as comments using the '%' symbor or output directly to
% the Command Window.


% Q1:
P = [0.9, 0.1; 0.44, 0.56];


% Q2:
PI1=P(1,1:2);
answers.Q1=P^30;
%It looks like over a large iteration, the distribution probability of each
%state becoming the landed on the final reaches a constant probability,
%no matter what the initial state condition is.

% Q3:
i_dry=[1,0];
i_wet=[0,1];
answers.Q3a=i_dry*P^30
answers.Q3b=i_wet*P^30
%Right eigen vectors are found.
% Q4:
[V,D]=eig(P');
%Matlab prefers right eigen vectors instead of left eigen vectors, so
%transition matrices need to be transposed before input into the command,
%and produces left eigen values


% Q5:
answers.Q5=V(:,1);

% Q6:
answers.Q6=sum(V(:,1));
%no


% Q7:
answers.Q7=(answers.Q5)/(answers.Q6)
%This is the unit vector.

% Q8:
%No.  They are the average across the whole year, based on conditions, not
%time nor humidity nor temperature nor time of year. Additionally, its
%proven that theres no chance of rain in the middle of a heat wave,
%therefore the static distribution is wrong to say there is given the
%previous day was dry. Rather, it might give how many days of the year
%there is some rain in davis, but even then the average is based off of
%years of data, and does not account for the increasing drought conditions
%of California. It could be improved by binning the probability
%distributions. A different distribution matrix each month of the year
%would increase the accuracy. It cannot be used to predict day to day, but
%it can be used to find how much of the year will have wet days.

% Q9:
T = 365;
X = NaN(1,T);
X(1) = 1;
for i = 2:T 
    probs = P(X(i-1),:);           % Get transition probabilities
    X(i) = binornd(1, probs(2))+1;   % Sample next states probability
end
answers.Q9=X;

% Q10:
CC=V(:,1)./sum(V(:,1));
GG=1;
subplot(3,1,GG)
plot(1:T,cumsum(X-1)./(1:T),[1,T],[CC(2) CC(2)],[1,T],[CC(1) CC(1)])
%creates a line plot of the cumulative probability of there being a wet day
%the next day, as time progresses.
title("Question 10")
xlabel("Days")
ylabel("Percent of time wet")
legend("Davis", "Davis Prediction 1", "Davis prediciton 2")
GG=GG+1;


% Q11:
P = [0.5, 0.5; 0.5, 0.5];
[V,D]=eig(P')
answers.Q11a=(V(:,1))./(sum(V(:,2)));
CC=V(:,2)./sum(V(:,2));
T = 365;
X = NaN(1,T);
X(1) = 1;
for i = 2:T
    probs = P(X(i-1),:);           % Get transition probabilities
    X(i) = binornd(1, probs(2))+1;   % Sample next states probability
end

subplot(3,1,GG)
plot(1:T,cumsum(X-1)./(1:T),[1,T],[CC(2) CC(2)],[1,T],[CC(1) CC(1)])
xlabel("Days")
ylabel("Percent of time wet")
legend("Random Town", "Random Town Prediction 1", "Random Town prediciton 2")
%creates a line plot of the cumulative probability of there being a wet day
%the next day, as time progresses.
title("Question 11")
GG=GG+1;
%This system converges just as fast as Davis. Also I plot better. #flex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% Q12:
file = fastaread('Ecoli-k12-genome.fasta');
seq = file.Sequence;
di_nuc_counts = zeros(4);
for i = 1:length(seq)-1
    di_nuc = seq(i:i+1); % Read dinucleotide
    row = nuc_to_index(di_nuc(1)); % Convert letters to index for matrix
    col = nuc_to_index(di_nuc(2)); % Convert letters to index for matrix
    di_nuc_counts(row, col) = di_nuc_counts(row, col) + 1;
end
transition_matrix = di_nuc_counts./sum(di_nuc_counts, 2);
display(transition_matrix);

%A Favors being followed by A, but despises G.
%T Favors being followed by T, but despises A.
%G Favors being followed by C, but despises no one uniquely.
%C Favors being followed by G, but despises T.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Q13:
P=transition_matrix;
[V,D]=eig(P');
answers.Q13=V(:,1)./sum(V(:,1));
%The nucleotide pairs are distributed somewhat uniformly. Not exactly 1/4
%each, but close enough.

% Q14:
file = fastaread('Organism_A.fasta');
seq = file.Sequence;
di_nuc_counts = zeros(4);
for i = 1:length(seq)-1
    di_nuc = seq(i:i+1); % Read dinucleotide
    row = nuc_to_index(di_nuc(1)); % Convert letters to index for matrix
    col = nuc_to_index(di_nuc(2)); % Convert letters to index for matrix
    di_nuc_counts(row, col) = di_nuc_counts(row, col) + 1;
end
A_matrix = di_nuc_counts./sum(di_nuc_counts, 2);
answers.Q14a=A_matrix
file = fastaread('Organism_B.fasta');
seq = file.Sequence;
di_nuc_counts = zeros(4);
for i = 1:length(seq)-1
    di_nuc = seq(i:i+1); % Read dinucleotide
    row = nuc_to_index(di_nuc(1)); % Convert letters to index for matrix
    col = nuc_to_index(di_nuc(2)); % Convert letters to index for matrix
    di_nuc_counts(row, col) = di_nuc_counts(row, col) + 1;
end
B_matrix = di_nuc_counts./sum(di_nuc_counts, 2);
answers.Q14b=B_matrix;
answers.Q14c=A_matrix-B_matrix;


% Q15:

P=A_matrix;
[V,D]=eig(P');
A_eigen=V(:,1)./sum(V(:,1))

P=B_matrix;
[V,D]=eig(P');
B_eigen=V(:,1)./sum(V(:,1))

%matches text value
% Q16:
%Not really. There are better methods than statistics, like comparing gene
%location, jumping gene numbers, alleles of genes, ect. This method is
%too... inpercise. Its focusing on the wrong values to compare genomes.

%Both have the same eigen values, and are within standard deviation to both
%be a match for. It would be better to check the transition matrix itself
%for sequence favoritism. When looking at transition matrix, its clear that
%organism A favors high A sequeces and T sequences, therefore that organism
% is E. atrepeatium.




function index = nuc_to_index(nuc)
switch nuc
    case {'A', 'a'}
        index = 1;
        return
    case {'T', 't'}
        index = 2;
        return
    case {'G', 'g'}
        index = 3;
        return
    case {'C', 'c'}
        index = 4;
        return
end
end

