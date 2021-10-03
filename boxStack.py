from operator import itemgetter


# Storing each dimension in boxes.txt into an array
# Rotating each boxes and storing in their respective arrays
# Calculating a base area and adding height to it to be
# able to later sort the merged array
def box_rotations():
    with open('boxes.txt') as box_dimensions:
        box_baseArea = []
        rot_box1_baseArea = []
        rot_box2_baseArea = []
        rot_box3_baseArea = []

        for line in box_dimensions:
            dimension = line.split()
            box = int(dimension[0]), int(dimension[1]), int(dimension[2])
            base_area1 = (int(dimension[1]) * int(dimension[2])) + int(dimension[0])
            box1 = [box, base_area1]
            box_baseArea.append(box1)

            rotation1 = int(dimension[1]), int(dimension[0]), int(dimension[2])
            base_area2 = (int(dimension[0]) * int(dimension[2])) + int(dimension[1])
            box2 = [rotation1, base_area2]
            rot_box1_baseArea.append(box2)

            rotation2 = int(dimension[2]), int(dimension[0]), int(dimension[1])
            base_area3 = (int(dimension[0]) * int(dimension[1])) + int(dimension[2])
            box3 = [rotation2, base_area3]
            rot_box2_baseArea.append(box3)

            rotation3 = int(dimension[1]), int(dimension[2]), int(dimension[0])
            base_area4 = (int(dimension[2]) * int(dimension[0])) + int(dimension[1])
            box4 = [rotation3, base_area4]
            rot_box3_baseArea.append(box4)

    return box_baseArea, rot_box1_baseArea, rot_box2_baseArea, rot_box3_baseArea


# Merging all the rotations together into the same array
def merge():
    box_baseArea, _, _, _ = box_rotations()
    _, rot_box1_baseArea, _, _ = box_rotations()
    _, _, rot_box2_baseArea, _ = box_rotations()
    _, _, _, rot_box3_baseArea = box_rotations()

    merger = box_baseArea + rot_box1_baseArea + rot_box2_baseArea + rot_box3_baseArea

    return merger


# Greedy algorithm: Finding the maximum height
# that can be formed using the boxes in boxes.txt
def greedy_algo():
    sorted_array = merge()
    sorted_array.sort(key=itemgetter(1), reverse=True)

    n = len(sorted_array)

    Stack = [sorted_array[0][0]]

    for i in range(1, n):

        if sorted_array[i][0][1] < Stack[len(Stack) - 1][1] and sorted_array[i][0][2] < Stack[-1][2]:
            Stack.append(sorted_array[i][0])

    maxHeight = 0
    for x in range(len(Stack)):
        maxHeight += Stack[x][0]

    return maxHeight, Stack


# Storing the heights of each boxes that form the
# box stack
def boxStack():
    _, stack = greedy_algo()
    stackHeights = []
    for x in range(len(stack)):
        stackHeights.append(stack[x][0])

    return stackHeights


# Recursive naive
def H(arr, i):
    if i == 1:
        return arr[i - 1]

    return arr[0] + H(arr[1:i], i - 1)


# Used in the top down approach to store sum of previously input data
# to speed up the process for the next number input
def storeSum():
    boxes_heights = boxStack()
    sumHeight = [-1] * len(boxes_heights)

    return sumHeight


def topDown(sum_store, arr, i):
    if sum_store[i] < 0:
        if i == 1:
            sum_store[i] = arr[0]
            return arr[0]
        else:
            sum_store[i] = arr[0] + H(arr[1:i], i - 1)

    return arr[0] + H(arr[1:i], i - 1)


def bottomUp(arr, i):
    maxHeight = 0
    repartition = []
    for x in range(i):
        # arr[x] = dimension
        # arr[x][0] = height
        maxHeight += arr[x][0]
        repartition.append(arr[x])

    print("To obtain maximum height with {} boxes, we use the boxes below:".format(i))
    for x in range(len(repartition)):
        print(repartition[x])

    return print("Maximum height obtained with {} boxes:".format(i), maxHeight)


def main():
    print("====== USING GREEDY ALGORITHM ======")
    maxHeight, _ = greedy_algo()
    _, stack_boxes = greedy_algo()
    print("Maximum height using all the boxes in boxes.txt: ", maxHeight)

    print("Box stack:")
    for x in range(len(stack_boxes)):
        print(stack_boxes[x])

    print("====== USING RECURRENCE & RECURSIVE NAIVE ======")
    num = int(input("i-th box: "))
    stack = boxStack()
    ans = H(stack, num)
    print("The maximum height for the i-th box is: ", ans)

    print("4.2: Complexity is O(n)")

    store = storeSum()
    print("====== USING TOP DOWN APPROACH ======")
    storeSum()
    number = int(input("i-th box: "))
    ans2 = topDown(store, stack, number)
    print("The maximum height for the i-th box is: ", ans2)

    print("====== USING BOTTOM UP APPROACH ======")
    _, stack_dimensions = greedy_algo()
    numBoxes = int(input("Enter number of boxes you want to use: "))
    bottomUp(stack_dimensions, numBoxes)


main()
