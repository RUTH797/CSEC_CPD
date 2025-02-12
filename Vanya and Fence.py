def minimum_road_width(n, h, heights):
    width = 0
    for height in heights:
        if height > h:
            width += 2  
        else:
            width += 1 
    return width
  
n, h = map(int, raw_input().split())
heights = list(map(int, raw_input().split()))

result = minimum_road_width(n, h, heights)

print(result)
