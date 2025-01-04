# on my way to a solution. For each pair of points need to check slope and get 
# both x and y intercept to account for possible parallel lines. Then get the 
# max slope, x, y count as the final value for most points on line.
def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    
    if len(points) < 3:
        return len(points)

    slopes = {}

    for point1 in points:
        for point2 in points:
            if point1 == point2:
                continue
            slope = 

    

print(maxPoints([[1,1],[2,2],[3,3]]))
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(maxPoints([[0,0],[0,0],[1,1],[1,3]]))