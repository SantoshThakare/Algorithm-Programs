def bubble_sort(list1):
    for val in range(len(list1)):

        for val2 in range(0, len(list1) - val - 1):

            if list1[val2] > list1[val2 + 1]:
                temp = list1[val2]
                list1[val2] = list1[val2 + 1]
                list1[val2 + 1] = temp

    return list1


if __name__ == '__main__':
    list = [15, 2, 22, 5, 18, 16, 9]

    print("Unsorted list is: ", list)
    print("sorted list is : ", bubble_sort(list))