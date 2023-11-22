class OverlapCounter():
    def __init__(self):
        return
    
    def CountMaxOverlap(self, intervals):
        cnt=0
        max_cnt=0
        intervals_start = [(x[0],'s') for x in intervals]
        intervals_end = [(x[1],'e') for x in intervals]
        intervals = intervals_start + intervals_end
        intervals.sort(key = lambda x:x[0])
        for _,t in intervals:
            if t == 's':
                cnt += 1
            else:
                cnt -= 1
            if cnt > max_cnt:
                max_cnt = cnt

        return max_cnt


C = OverlapCounter()
print(C.CountMaxOverlap([[0,2], [3,7], [1,5], [7,8], [4,6]]))

C = OverlapCounter()
print(C.CountMaxOverlap([[0,5], [6,8], [1,7]]))