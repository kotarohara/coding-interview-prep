# Code from http://stackoverflow.com/questions/18262306/quick-sort-with-python

def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


def main():
    arr = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
    print arr
    print quick_sort(arr)

if __name__ == "__main__":
    main()
