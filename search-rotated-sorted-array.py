###### given an integer array - nums - sorted in ascending order, and an integer - target - suppose that - nums - is rotated at some pivot unknown to you beforehand (i.e. [0,1,2,3,4] might become [2,3,4,0,1]). You should search for -target- in -nums- and if found, return it's index. Otherwise return -1. #####

### Understand
    # could solve with a linear approach
    # best to solve with logarithmic time
    # if you can find the pivot location:
        # where did the rotation happened
        # treat it like a binary search
        # if target was 6, and did binary search
            # know there is a left and right because you know there is a pivot
            # if you know the first and last number, and you know it's been rotated, you can decide whether to go left or right
                # that's the trick about binary searches

### Plan