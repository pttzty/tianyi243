'''
Search a number in a Rotated Sorted Array
'''

import bisect

def find_pivot(rotated_array):
    '''
    Find the pivot index where the array was rotated.
    Overall Log(N)
    '''
    left = 0
    right = len(rotated_array) - 1
    while left < right:
        mid = (left + right) // 2
        # if the mid element is greather than the right element, then the pivot is in the right half
        if rotated_array[mid] > rotated_array[right]:
            left = mid + 1
        else:
            # the pivot is in the left half
            right = mid
    return left

class Solution(object):
    def search(self, rotated_array, target):
        '''
        Search for a target in a rotated array.
        Overall Log(N)
        return -1 if value not found
        '''
        pivot = find_pivot(rotated_array)
        if target == rotated_array[pivot]:
            return pivot
        elif target > rotated_array[pivot] and target <= rotated_array[-1]:
            # target is in the right half range or it's not found
            index = bisect.bisect_left(rotated_array[pivot+1:], target)
            if rotated_array[pivot+1:][index] == target:
                return pivot + 1 + index
            else:
                return -1
        else:
            # target is in the left half range or it's not found
            index = bisect.bisect_left(rotated_array[:pivot], target)
            if index < len(rotated_array[:pivot]) and rotated_array[:pivot][index] == target:
                return index
            else:
                return -1
    
    
if __name__ == '__main__':
    rotated_array = [4, 5, 6, 7, 8, 0, 1, 2]
    target = 0
    S = Solution()
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = 6
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = 7
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = 1
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = 10
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = -1
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))
    target = 5.5
    print('The index of {} in {} is {}'.format(target, rotated_array, S.search(rotated_array, target)))