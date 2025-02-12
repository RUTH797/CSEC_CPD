def count_solved_problems(n, problems):
    solved_count = 0
    for problem in problems:
        if sum(problem) >= 2:
            solved_count += 1
    return solved_count

n = int(raw_input())
problems = [list(map(int, raw_input().split())) for _ in range(n)]

result = count_solved_problems(n, problems)

print(result)
