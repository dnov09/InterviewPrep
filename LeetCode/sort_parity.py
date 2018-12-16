#%%
def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # rLst = []
        # for nums in A:
        #     if nums % 2 == 0:
        #         rLst.append(nums)
        # for nums in A:
        #     if nums not in rLst:
        #         rLst.append(nums)
        # return rLst
        even = []
        odd = []
        for nums in A:
            if nums % 2 == 0:
                even.append(nums)
            else:
                odd.append(nums)
        return even + odd

sortArrayByParity([1006,1483,2209,3023,2681,1305,1159,593,3918,494,3665,1244,1423,3681,3298,3710])

def sortArraybyParityII(A):
    '''
    :type A: List[int]
    :rtype: List[int]

    input -> [1,2,3,4,5,6,7,8]
    output -> [2,1,4,3,6,5,8,7]
    '''

    pass
