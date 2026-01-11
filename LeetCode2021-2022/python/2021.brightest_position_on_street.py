class Solution:
    from collections import defaultdict
    def brightestPosition(self, lights: List[List[int]]) -> int:
        bound = defaultdict(int)

        for pos, r in lights:
            bound[pos-r] +=1
            bound[pos+r+1] -=1
        
        curr_brightness = 0
        max_brightness = 0
        bright_pos = 0

        for k,v in sorted(bound.items()):
            curr_brightness += v
            
            if curr_brightness > max_brightness:
                max_brightness = curr_brightness
                bright_pos = k
        return bright_pos
