def solution(A, F, M):
    N = len(A)
    target_sum = M * (N + F)
    current_sum = sum(A)
    
    for roll1 in range(1, 7):
        for roll2 in range(1, 7):
            if current_sum + roll1 + roll2 == target_sum:
                return [roll1, roll2]
    
    return [0]