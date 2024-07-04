def solution(N):
    import string
    alphabet = string.ascii_lowercase 
    # Determine the maximum number of unique letters we can use
    k = min(26, N)
    
    # Calculate how many times each letter will appear
    q = N // k
    r = N % k
    
   
    result = (alphabet[:k] * q) + alphabet[:r]
    
    return result

print(solution(3))   
print(solution(5))  
print(solution(30))  