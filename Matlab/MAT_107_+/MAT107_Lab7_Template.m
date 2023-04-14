
% Name:Gerrik Labra
% Student ID: 914076227 

% Lab 7: Modeling Cancer with Markov Chains
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations can be
% enterred as comments using the '%' symbol or output directly to the
% Command Window.

% Q1:
%Probability would be expected to be zero.

% Q2:
P=xlsread('cancer_model.xls');
col=P(:,2);
% Q3:
figure;
bar(P(23,:));
xticks(1:50);
xlabel('Site')
ylabel('Transition Chance')


% Q4:
PI0=zeros(1,50);
PI0(23)=1;
[V,D]=eig(P');
answers.Q4=V(:,1)./sum(V(:,1))

% Q5:
chain=sim_MC(P,23,100);
organ_count=histcounts(chain,1:50);
organ_count(24)
%state 24 has a high frequency, relative to other organs.

% Q6:
trials=1000;
steps=1000;
fp_heart=NaN(trials,1);
fp_pancreas=NaN(trials,1);
fp_lymph=NaN(trials,1);

for i=1:trials
    chain=sim_MC(P,23,steps);
    fp_heart=find(chain==17,1)-1;
    fp_pancreas=find(chain==28,1)-1;
    fp_lymph=find(chain==24,1)-1;

end
mfpt_heart=mean(fp_heart)
mfpt_pancreas=mean(fp_pancreas)
mfpt_lymph=mean(fp_lymph)
% Yes, lymph nodes had lower MFPT compared to heart and pancrease

% Q7: 
j=28;
i=23;
Q_pancreas=P;
Q_pancreas(j,:)=0;
Q_pancreas(:,j)=0;
T=(eye(50)-Q_pancreas)\ones(50,1);
T_panc=T(i)
%Its close enough to sim. 26.6345

j=24;
Q_RlymphN=P;
Q_RlymphN(j,:)=0;
Q_RlymphN(:,j)=0;
T=(eye(50)-Q_RlymphN)\ones(50,1);
T_RlymphN=T(i)
%Its close enough to sim. 4.6289
