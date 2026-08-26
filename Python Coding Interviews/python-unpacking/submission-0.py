from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    a,b,c = triplet 
    return a+b+c


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width , height , depth = box_dimensions
    return width*height*depth


# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
