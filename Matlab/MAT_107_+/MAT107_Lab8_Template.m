
%Name:Gerrik Labra
% Student ID: 914076227 

% Lab 8: Branching Processes
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations should be
% enterred as comments using the '%' symbol.
clear
clc
close all
clearvars
% Q1:
X = sim_branching_poisson(1.88, 10);
figure;
plot(0:10, X);
xlabel('Generation')
title('question 1')
ylabel('Outbreak Size')


% Q2:
Xs = NaN(11, 100);
for i = 1:100
    Xs(:, i) = sim_branching_poisson(1.88, 10);
end
figure;
plot(0:10, Xs);
title('question 2')
xlabel('Generation')
ylabel('Outbreak Size')


% Q3:
mos=mean(Xs(11,:));
answers.q3=mos;

% Q4:
pos=sum(Xs(11,:)==0)/100
answers.q4=pos;

% Q5:
Lamb=1.88;
gens=10;
answers.q5=sum(Lamb.^(0:gens));
% Q6:
Xs_sum=cumsum(Xs);
M_TS=mean(Xs_sum(11,:))
%roughly same as qeustion 5

% Q7:
s=0;
for i=1:10
    s=poisspgf(s,Lamb);
end
p_endGen10=s
%0.239209
%Question 4 was 18 percent. The probability is higher.



% Q8:
syms S;
sol=vpasolve(exp(Lamb*(S-1))==S,[0,0.99])
%0.23926576308781532803558980371729
%Matches well.

% Q9:
load('secondary_infections.mat');
%part a
nbin_Par=nbinfit(counts);
%b
figure
hold on
histogram(counts,'Normalization','probability')
plot(0:35,nbinpdf(0:35,nbin_Par(1),nbin_Par(2)));
title('question 9')
xlabel('2nd Infections')
ylabel('Probability')
%C
plot(0:35,poisspdf(0:35,Lamb));
legend('Data','NB fit','Poiss Fit')
hold off
%The NB fit better, because it matched the beginning generation, while the
%Poiss did not. Both matched the outcome of 35 2nd infections however.

% Q10:
Xs_NB=NaN(11,100);
for i=1:100
   Xs_NB(:,i)=sim_branching_nbin( nbin_Par(1),nbin_Par(2),10);
end
%A
mos_nb=mean(Xs_NB(11,:))

%B
pos_nb=sum(Xs_NB(11,:)==0)/100
%0.9000

%C
XsNBsum=cumsum(Xs_NB);
mean_totalsize_NB=mean(XsNBsum(11,:))
%From 1700 to 500. Lots more variance.

%D
%There is a lot more variance, but by the end there is a chance that the
%outbreak will not be over by generation 10

% Q11:
s=0;
for i=1:10
s= nbinpgf(s,nbin_Par(1),nbin_Par(2));
end
p_end_by_10_NB=s
%agrees within 2% of the pos_nb
%0.8789


% Q12:
syms S;
sol=vpasolve((nbin_Par(2)/(1-(1-nbin_Par(2))*S))^nbin_Par(1)==S,[0,0.99])
%0.87945640312821151217912180776012

% Q13:
%The risk assesed under the poisson model has high uncertainty, while under
%the Negative Binomial model there is mathematical certainty, or at least
%agreement, of what the fallout of the outbreak will be.


function X = sim_branching_poisson(lambda, n_max)
 
X = zeros(1, n_max+1); % Initialize infection counts to zero
X(1) = 1; % Single infection at X0
 
for n = 1:n_max
    
    counts = 0;
 
    for i = 1:X(n)
        counts = counts + poissrnd(lambda);
    end
 
    X(n+1) = counts; % Total number of secondary infections
 
end
end 

function g = poisspgf(s, lambda)
 
g = exp(lambda*(s-1));
 
end

function X = sim_branching_nbin(r, p, n_max)
 
X = zeros(1, n_max+1); % Initialize infection counts to zero
X(1) = 1; % Single infection at X0
 
for n = 1:n_max
    
    counts = 0;
 
    for i = 1:X(n)
        counts = counts + nbinrnd(r, p);
    end
 
    X(n+1) = counts; % Total number of secondary infections
 
end
end 

function g=nbinpgf(s,r,p)
g=(p/(1-(1-p)*s))^r;
end
