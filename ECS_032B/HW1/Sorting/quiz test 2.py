def make_cuboid_volume_function(height: float, length: float):
    c=height*length
    return lambda a: a*c
three_by_four = make_cuboid_volume_function(3, 4)
print(three_by_four(1))
print(three_by_four(3))

