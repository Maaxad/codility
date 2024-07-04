def solution(A, F, M):
    N = len(A)
    total_rolls = N + F
    total_sum_needed = M * total_rolls
    current_sum = sum(A)
    missing_sum = total_sum_needed - current_sum
    
    if missing_sum < F or missing_sum > 6 * F:
        return [0]
    
    result = [1] * F
    remaining_sum = missing_sum - F
    
    for i in range(F):
        if remaining_sum == 0:
            break
        add = min(5, remaining_sum)
        result[i] += add
        remaining_sum -= add
    
    return result