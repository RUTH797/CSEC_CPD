def years_to_surpass(a, b):
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    return years

a, b = map(int, raw_input().split())

result = years_to_surpass(a, b)

print(result)
