# Weirdly dissatisfying solution
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    total_length = m+n-1
    length_nums2 = n-1
    length_nums1 = m-1

    while length_nums2 >= 0:
        if length_nums1 >= 0 and nums1[length_nums1] > nums2[length_nums2]:
            print(nums1)
            nums1[total_length] = nums1[length_nums1]
            print(nums1)
            length_nums1 -= 1
        else: 
            print("ELSE CONDITION TRIGGERED \n", nums1)
            nums1[total_length] = nums2[length_nums2]
            print(nums1)
            length_nums2 -= 1

        total_length -= 1

    print("FINAL NUMS1", nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)