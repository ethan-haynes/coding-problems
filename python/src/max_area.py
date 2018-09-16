def maxArea(height, width=None):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) <= 1: return -float('inf')
    if width == None: width = len(height) - 1
    h1, h2 = height[0], height[-1]
    area = min(h1,h2) * width
    return max(area, 
                maxArea(height[1:], width-1), 
                maxArea(height[:-1], width-1))
