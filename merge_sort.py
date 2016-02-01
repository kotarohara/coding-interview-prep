from types import IntType


def merge_sort(arr):
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return [arr[0], arr[1]]
        else:
            return [arr[1], arr[0]]
    elif len(arr) == 1:
        return arr
    else:
        center = len(arr) / 2
        arr1 = merge_sort(arr[:center])
        arr2 = merge_sort(arr[center:])
        ret = []
        while arr1 or arr2:
            if not arr1:
                ret += arr2
                break
            elif not arr2:
                ret += arr1
                break
            else:
                if arr1[0] < arr2[0]:
                    num = arr1.pop(0)
                else:
                    num = arr2.pop(0)
                ret.append(num)
        return ret


def main():
    arr = [21, 1, 2, 26, 45, 29, None, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
    arr = filter(lambda x: type(x) == IntType, arr)
    print arr
    print merge_sort(arr)

if __name__ == "__main__":
    main()

