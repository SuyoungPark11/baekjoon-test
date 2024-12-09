class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a = rec1[2] - rec2[0]
        b = rec1[3] - rec2[1]
        c = rec1[0] - rec2[2]
        d = rec1[1] - rec2[3]
        if (a > 0) or (b > 0) or (c < 0) or (d < 0):
            return True
        else:
            return False
        