
% Name:Gerrik Labra
% Student ID: 914076227
% Lab 4: The Poisson Distribution and RNA-Seq
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations should be
% enterred as comments using the '%' symbol.
%% 
% Use MATLAB to draw1000samples of a Poisson random variable with the
% function poissrnd. Assume that lamda=10. What are the mean and variance of
% your 1000 samples?

lamda=10;
n=1000;
% Q1:
random_numbers_1=poissrnd(lamda,1,n);
RN_mean=mean(random_numbers_1);
RN_var=sum((random_numbers_1-RN_mean).^2)/(n-1);

answers.q1={RN_mean,RN_var};


%% 
% Use 𝑛=10,000 and 𝑝=0.001 to plot a Binomial distribution over
% 𝑘∈{0,1,...,20}.Then, plot a Poisson distribution with lambda=𝑛𝑝=10
% over the same interval. Do the two distributions agree?(Hint: Use
% binopdf(k,n,p)and poisspdf(k,lambda)to generate the points of the
% distributions)

n=10000;
p=0.001;
k=0:20;
% Q2:
GG=1;
y_1=binopdf(k,n,p);
y_2=poisspdf(k,n*p);
subplot(3,3,GG)
plot(k,y_1)
title("Question 2 Bino distribution");
GG=2;
subplot(2,2,GG)
plot(k,y_2)
title("Question 2 Poisson distribution");
GG=GG+1;

%They agree
%% 

% Let's assume that the input is a collection of ? ?RNA fragments from 𝐺
% different genes. Suppose that agene𝑖is responsible  for 𝑛$of  the total
% fragments. Further  assume  that all fragments produced by a gene i are
% of identical length ti.
%N=sum(ni*ti) where i=1:G

%Primer length =6, no less. t+1-primer_lenght places where primer can bind.

% Simulatean RNA-Seq experiment with the parameters from the prompt above: 
ti = [200 300 1000 500 450]; %5 genes, with unique lengths
ni = [5 3 5 7 10]; %Copy numbers of each gene/transcript
np= 200; %different primers to simulate
falloff=0.01;%Probability of polymerase falling off
plen = 6;
binding_sites = (ti+1-plen).*ni;
probs = binding_sites./sum(binding_sites);

% Sample transcripts that produce fragments
%binds = 1+sum(repmat(rand(1,np),length(ti),1)>repmat(cumsum(probs'),1,np),1);
%Length of the reverse-transcribedfragment is itself a random variable. We
%will assume that RT has probability 𝑝=0.01 of dropping off at each
%nucleotide, and subsequently that the length of a cDNA fragment is random
%variable 𝐿~Geom(𝑝).We will also need to constrain this length so that if
%the RT reaches the end of the original strand, elongation stops.

% Q3:
binds = 1+sum(repmat(rand(1,np),length(ti),1)>repmat(cumsum(probs'),1,np),1);
frags=zeros(np,3);
for i=1:length(binds)
   frags(i,1)=binds(i);
   t=ti(binds(i));
   nuc = randi(t-5); % Binding position
   frags(i, 2) = nuc;
   len = 6 + geornd(falloff);
   if (nuc+len)>t
       len = t-nuc;
   end
   frags(i,3) = len;
end
detected_frags_raw= frags(frags(:, 3) >=30);
counts_raw = hist(detected_frags_raw, 1:1:length(ti));
[counts, detected_frags]=rna_seq_sim(ti, ni, np);

answers.q3.a=counts
answers.q3.b=detected_frags


%% 
% Suppose that we wanted to compute the relative abundance of each gene.
% Because each gene has a different RNA fragment length, we need to account
% for the fact that longer RNA fragments will be primed more often than
% smaller fragments. Also recall that the entire length of an RNA fragment is
% not available for primer binding –the "effective length" of a gene 𝑖 is
% 𝑡i−5.Thus, the relative proportion of fragments from a particular gene
% 𝑖 is computed as:

%Q4:
p_gene=(counts./(ti-5))/(sum((counts./(ti-5))))
answers.q4=p_gene
%% 

% Q5: %The underlying relative abundance is on the same order of magnitude,
% and has a variance at the hundreths place. Its not exactly correct, but
% its a good estimate.

%% 
% Perform 1000 experiments using the parameters from above. Save the counts
% for the first gene (the gene with length 200) from each experiment and
% plot a histogram of the 1000 observations.
N=1000;
count_A=NaN(N,1);
%Q6:
for i=1:N
    [count_B, ~]=rna_seq_sim(ti, ni, np);
    count_A(i)=count_B(1);
end
subplot(2,2,GG)
hold on
histogram(count_A,'Normalization','pdf')
xlabel('counts')
title('Question 6 and 7')
GG=GG+1;
%% 

% Q7:;
mc=mean(count_A);
k=0:40;
plot(k,poisspdf(k,mc))
hold off
%% 

% Q8:
N=1000;
count_A=NaN(N,1);
for i=1:N
    [count_B, ~]=rna_seq_sim(ti, poissrnd(ni), np);
    count_A(i)=count_B(1);
end
subplot(2,2,GG)
hold on
histogram(count_A,'Normalization','pdf')
xlabel('counts')
title('Question 8,9,10')
GG=GG+1;
%% 

% Q9:
mc=mean(count_A);
k=0:40;
plot(k,poisspdf(k,mc))


%% 

% Q10:
fit_line=nbinfit(count_A); %fit_lined= [R P]
plot(k,nbinpdf(k,fit_line(1),fit_line(2)))
legend("observed values", "poisson fit/line","NB fit/line")
%Yes, it captures the data better.
%% 

% Q11:
%Binomial tells us probability at each trial or instance for success.
%The fit line matches the data better than poisson, and this is due to incorporating variance.
%The effect is a higher matching to the actual abundance.
%counts being random rather than static.
function [counts, detected_frags] = rna_seq_sim(ti, ni, np)

% Primers
plen = 6; % Length

% Enumerate possible binding sites
binding_sites = (ti+1-plen).*ni; % Number of binding sites in pool, per transcript

% Probability that a primer binds to each transcript
probs = binding_sites./sum(binding_sites);

% Sample transcripts that produce fragments
binds = 1+sum(repmat(rand(1, np), length(ti), 1)>repmat(cumsum(probs'), 1, np), 1);

% Initialize fragments stemming from each binding site
frags = zeros(np, 3);
 
p = 0.01; % Probability of RT falling off
 
for i = 1:length(binds) % For each primer...
    
    frags(i, 1) = binds(i); % Save transcript
    t = ti(binds(i)); % Transcript length
    
    nuc = randi(t-5); % Binding position
    frags(i, 2) = nuc; % Save position
    len = 6 + geornd(p); % Length of reverse transcribe (including primer)
    
    % Handle if fragment length goes beyond end of transcript
    if nuc + len > t
        len = t-nuc;
    end
    
    frags(i, 3) = len; % Length of fragment
     
end
   
detected_frags = frags(frags(:, 3) >= 30);

counts = hist(detected_frags, 1:1:length(ti));

end