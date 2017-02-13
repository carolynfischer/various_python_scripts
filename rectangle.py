"""
A crack team of love scientists from OkEros (a hot new dating site) have devised 
a way to represent dating profiles as rectangles on a two-dimensional plane.
They need help writing an algorithm to find the intersection of two users' love 
rectangles. They suspect finding that intersection is the key to a matching 
algorithm so powerful it will cause an immediate acquisition by Google or 
Facebook or Obama or something.

Write a function to find the rectangular intersection of two given love 
rectangles.

As with the example above, love rectangles are always "straight" and never 
"diagonal." More rigorously: each side is parallel with either the x-axis or 
the y-axis.
"""

r1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,
}

r2 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,
}

def intersection(r1, r2):
    # write the body of your function here
    left = max(r1['left_x'], r2['left_x'])
    right = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    bottom = max(r1['bottom_y'], r2['bottom_y'])
    top = min(r1['bottom_y'] + r2['height'], r2['bottom_y'] + r2['height'])

    r1_area = r1['width'] * r1['height']
    r2_area = r2['width'] * r2['height']
    intersection_area = (right - left) * (top - bottom)
    if left < right and bottom < top:
        result_area = r1_area + r2_area - intersection_area
        result = {
            'left_x': left,
            'bottom_y': bottom,
            'width': right - left,
            'height': top - bottom,
        }
    else:
        result = "The areas don't overlap"
    return result


# run your function through some test cases here
# remember: debugging is half the battle!
print intersection(r1, r2)