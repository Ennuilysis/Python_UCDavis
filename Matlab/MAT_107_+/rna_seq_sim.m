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