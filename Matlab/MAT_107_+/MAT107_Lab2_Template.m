clear
%Name: Labra Gerrik Student
%ID: 914076227

% Lab 2: Probabilities, Bayes' Formula, Estimating Population Size MAT/BIS
% 107, Spring 2021 University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
%
% This lab includes a number of questions with answers that require yes/no
% as well as some explanation. In particular, several questions (Q2,Q3) ask
% if a computation "agrees" with a prior probability calculation while
% (Q5,Q8,Q10,Q11) all require some further explanations. Please respond to
% these questions with comments under the appropriate question in addition
% to doing the required numerical calculations.

% part1 Consider the possible outcomes of the following scenario. You have
% two jars – one jar contains 2 red balls and 3 green balls, and the other
% jar contains 2 red balls and 2 green balls. One ball from Jar 1 is
% selected at random and moved to Jar 2, but its color is not known. One
% ball from Jar 2 is then selected at random.

% % Q1:What is the probability of a red ball having been transferred from
% Jar 1 to Jar 2 if the color of the ball drawn from Jar 2 is red?
prob_green_trans=3/5;
prob_red_trans=2/5;
prob_red_g_red_trans=3/5;
prob_red_g_red_trans=2/5;
prob_green_g_green_trans=3/5;
prob_red_g_green_trans=2/5;
prob_green_jar2=13/25;
prob_green_trans_g_green=9/13;

ans.q1=(3/5)*(2/5)/(1-(13/25));

% Q2:
N_simulations = 10000;
transferred_balls = NaN(N_simulations, 1);
sampled_balls = NaN(N_simulations, 1);

for i = 1:N_simulations
    jar1 = [1, 1, 1, 0, 0];
    jar2 = [1, 1, 0, 0];
    
    transferred_balls(i) = randsample(jar1, 1);
    jar2 = [jar2, transferred_balls(i)];
    sampled_balls(i) = randsample(jar2, 1);
end

ans.q2_green=(sum(sampled_balls)/N_simulations);
ans.q2_red=1-ans.q2_green;
ans.q2_write="Yes";
% Q3:
prob_green_transferred_given_green_draw = sum(sampled_balls(transferred_balls == 1))/sum(sampled_balls);
prob_red_transferred_given_green_draw = sum(sampled_balls(transferred_balls == 0))/sum(sampled_balls);
prob_red_transferred_given_green_draw = sum(sampled_balls(transferred_balls == 0))/sum(sampled_balls(sampled_balls==0));
ans.q3_write="Yes"


% Q4:
ans.q4=10/(2/10);


% Q5:
%assume ten recaptured
ans.q5="The population is so large that tags were recaptured. So BIGish.";

% Q6:
%relative tagged and captured, relative tagged uncaptured, tagged in
%population
ans.q6=nchoosek(20,4)*nchoosek(80,11)/nchoosek(100,15);

% Q7:
ans.q7=nchoosek(20,0)*nchoosek(80,15)/nchoosek(100,15);


% Q8:
N = [50, 100, 150, 200, 300, 400];
B = [5, 10, 15, 20, 25];
p0 = zeros(length(N), length(B));
k = 0;
for i=1:length(N)
    for j=1:length(B)
        p0(i,j) = mark_recapture_prob(N(i), B(j), B(j), k);
    end
end
figure()
bar(p0(:, 2))
xlabel('Population Size')
xticklabels(cellstr(num2str(N(:))))
ylabel('Probability of Sampling 0 Tagged Animals')
ans.q8="The probability should increase as population size increases. The problem is recapturig zero tagged fish gives no good info, the probability doesnt tell us WHAT size it could really be. Instead, it tells us to prefer a smaller population to get accurate estimates of populations.";

% Q9a:
N= 20;
B= 5;
n= 4;
% k=[0, 1, 2];

ans.q9a_wor=sum(hygepdf(0:2,N,B,n)); %without replacement
ans.q9a_wr=sum(binopdf(0:2,n,B/N));

N= 100;
B= 50;
n= 40;
% k=[1, 2, 3];
ans.q9b_wor=sum(hygepdf(1:3,N,B,n)); %without replacement
ans.q9b_wr=sum(binopdf(1:3,n,B/N));

N= 1000;
B= 200;
n= 40;
% k=[7, 8, 9];
ans.q9c_wor=sum(hygepdf(7:9,N,B,n)); %without replacement
ans.q9c_wr=sum(binopdf(7:9,n,B/N));

% Q10:
ans.q10="It cannot be discrened from the calculations alone which ever one is more  accurate to representing event possibility, but they both agree on order of magnitude, and to a certain degree of digits. I would assume with replacement, as the enviormental conditions of observanece match those of nature, rather than the proxy of a sub-population.";

% Q11:
figure("Position",[0, 0, 600, 500])
N = 300;
B = 20;
n = 15;
population = zeros(N, 1);
tags = randsample(1:N, B, false); % Randomly sample animals to tag
population(tags) = 1; % Mark tagged animals
N_sims = 100; % Number of simulations
r_estimated_wr_i = NaN(N_sims, 1); % Estimates for ratio of tagged animals with replacement
r_estimated_wor_i = NaN(N_sims, 1); % Estimates for ratio without replacement
for i = 1:N_sims
    samples = randsample(1:N, n, true);
    k_tagged = sum(population(samples));
    r_estimated_wr_i(i) = k_tagged/n;
    samples = randsample(1:N, n, false);
    k_tagged = sum(population(samples));
    r_estimated_wor_i(i) = k_tagged/n;
end
N_estimated_wr = B./r_estimated_wr_i; % Population size estimates with replacement
N_estimated_wor = B./r_estimated_wor_i; % Population size estimates without replacement
figure()
histogram(N_estimated_wr, 0:5:5*N)
hold on
histogram(N_estimated_wor, 0:5:5*N)
plot([100, 100],[0, N_sims/2], '--r')
xlabel('Estimated Population Size')
ylabel('Number of Simulations')
legend('Sampling With Replacement','Sampling Without Replacement')
axis tight

ans.q11="Sampling without replacement seems to have the greatest prediction of population size.";

ans

function result = mark_recapture_prob(N, B, n, k)

result = nchoosek(N-B, n-k)*nchoosek(B, k)/nchoosek(N, n);

end