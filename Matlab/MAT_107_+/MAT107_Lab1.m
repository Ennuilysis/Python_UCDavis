
% Name: Gerrik Labra
% Student ID: 914076227

% Lab 1: Counting Problems
% MAT/BIS 107, Spring 2021
% University of California, Davis

%% Instructions: Enter your answers below each corresponding question header.
% Your code should produce the necessary outputs and/or plots, depending
% on what each question requests. Wordy answers or explanations should be
% enterred as comments using the '%' symbol.

% Q1: How many unique DNA sequences can be constructed with a length of 12?
answer1=4^12

% Q2: Suppose that an experiment informs you that a protein is comprised by one 
% methionine, one alanine, one glycine, and one leucine. You don’t know the order of amino acids 
% in the protein, however. How many ways can these four amino acids be arranged into a protein 
% sequence?
% Methionine  (ATG); alanine(GCT, GCC, GCA, GCG); 
% glycine(GGT, GGC, GGC, GGG); leucine (TTA, TTG,CTT, CTC, CTA, CTG).
answer2=factorial(4)

% Q3:In reality, proteins always start with methionine. How many ways can the protein sequence be formed,
% given that methionine is at the beginning?
answer3=factorial(3)

% Q4:Given your answer to Question 3, how many DNA sequences exist that could 
% produce the protein?
answer4=factorial(3)*4*4*6

% Q5: In Question 1, we computed the total number of unique DNA sequences with length 
% 12. Our protein with four amino acids also corresponds to a DNA sequence with length 12, 
% because each codon is a triplet. What percentage of DNA sequences with length 12 would 
% produce our protein?
answer5_percentage=(answer4/answer1)*100

% Q6:  
answer6=0;

for x=0:1:4
    answer6=answer6+nchoosek(5,x)*nchoosek(4,x);
end
answer6
% Q7:
answer7=0;

for x=0:1:15
    answer7=answer7+nchoosek(15,x)*nchoosek(15,x);
end
answer7
