
%%Name: Labra Gerrik Student
%ID: 914076227

% Lab 3: Sanger Sequencing
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations can be
% enterred as comments using the '%' symbol or output directly to the 
% Command Window.
%% 

%%In a test tube, a soupis createdcontaining DNA polymerase, good copies of
%C, T and G, and a mix of good and “defective” copies of A.

%Strand S is added, and complement is building.

%when 𝑆contains a T (so that an A is added to the growing strand) if a
%good A is added, the polymerase continues building up the new strand. But
%if a defectivecopy of A is used, the replication stopsat that point.

% We  now separate  the  two  strands  and  measure  their  lengthsin
% order  to  determine where  a defective nucleotide was incorporated

%Suppose the short string has length four. We can then deduce that there is
%a defective A at position fourof the short strand, and hence there is a T
%at position four of the original DNA strand 𝑆.

%% 

% Q1:
%p is probability Adenosine is good.
p=[0.5,0.7,0.95];
%(1-p)=success, or probability of bad adenosine
k=1:10;
n=1;
for i=p
    pdf=geopdf(k-1,1-i);
    subplot(3,3,n);
    plot(k,pdf,'-.c^');
    ylim([0, 0.2]);
    ylabel('Probability');
    xlim([0.5 10.5]);
    xticks(1:10);
    xlabel('k');
    legend("p="+string(i));
    title('Probability of Ending at k-th T in S');
    n=n+1;
end

%Answer: As probability increase, k gets smaller. Or rather, it becomes
%more likely the first or no T neucleotides match with a bad Adenosine.

% Q2:
%Answer: when p=0.95

% Q3:
%As k gets large, probability decreases. This indicates its most likely
%that a bad A will attach at the beginning, therefore more likely there
%will be a majority of VERY short S sequences when measured after
%sequencing.


% Q4:
p = [0:0.001:1];
k = [1,2,3];
for i=k
n_exp_1 = 1./(geopdf(i-1, 1-p));
subplot(3,3,n)
plot(p, n_exp_1)
xlim([0 1])
xlabel('Proportion of Good Nucleotides')
ylabel('Expected Number of Experiments')
ylim([0 10])
legend("k="+string(i))
n=n+1;
end
% Q5:
%For k=1, first T position, the expected number of experiments to detect
%a bad adenosine increases as the ratio of good nucleotides increases.

%For k=2, the expected number of experiments increases exponentially to
%dect a bad adenosine, both when good nucelotide ratio is low and high. It
%appears theres a relation between experimental trials and not just ratio,
%but also the likelyhood of finding a bad adenosine requires twice the
%number of experiments of the previous position, but has half the range of
%nucleotide concentration to have the lowest number of experiments to find
%a bad adenosine at that location.

%For k=3 The above situation is seen again, but now the range is the upper
%half of k=2. So it takes a geometrically decreasing ration range as
%position or k increases.

% Q6:

syms k p
solve(diff(1/((p^(k-1))*(1-p)))==0, p)
%(k-1)/k=p
k=[1,2,3]
a=(k-1)./k
%answer provided by function is correct.

% Q7:
p =[0.8,0.9];
for i=p
    Nk = 30;
    N_experiments = 10000;
    outcomes = NaN(N_experiments, 1);
    for ii = 1:N_experiments
        outcomes(ii) = min([geornd(1-i)+1, Nk+1]);
    end
    subplot(3,3,n)
    histogram(outcomes)
    title("Count of bad adenosines at kth T position");
    n=n+1;
end
% when p is 0.8 expectation is better and follows a normal trend. 0.9 has
% weird bit where probability shoots up at the final position.

% Q8:
Nk = 30;
p=(Nk-1)/Nk
N_experiments = 10000;
outcomes = NaN(N_experiments, 1);
for ii = 1:N_experiments
    outcomes(ii) = min([geornd(1-p)+1, Nk+1]);
end
subplot(3,3,n)
histogram(outcomes)
title("Count of bad adenosines at kth T position");
n=n+1;
%Distribution is clearly biased. I ran the code multiple times. The derived
%formula is wrong.

% Q9:
%In my biased graphs, yes. All fragment lengths can be detected. As the
%length gets longer, relatively less and less fragments are detectable as
%length increases.
