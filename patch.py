def solution(S):
    N = len(S)
    patches = 0
    i = 0
    
    while i < N:
        if S[i] == 'X':

            patches += 1

            i += 3
        else:

            i += 1
            
    return patches

# Examples
print(solution(".X..X"))          
print(solution("X.XXXXX.X."))     
print(solution("XX.XXX.."))