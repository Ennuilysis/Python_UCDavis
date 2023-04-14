function result = mark_recapture_prob(N, B, n, k)
 
result = nchoosek(N-B, n-k)*nchoosek(B, k)/nchoosek(N, n);
 
end
