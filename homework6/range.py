from __future__ import annotations

class Range:
    def __init__(self, min=None, max=None):
        self.min = min
        self.max = max
    
    def get_min(self):
        return self.min

    def get_max(self):
        return self.max 
    
    def empty_interval(self):
        return self.min is None and self.max is None
    
    def intersection(self, second: Range) -> Range:
        if self.empty_interval() or second.empty_interval() or not self.crossing(second):
            return Range()
        ans_min = max(self.min, second.get_min())
        ans_max = min(self.max, second.get_max())
        return Range(ans_min, ans_max)
    
    def unify_crossing(self, second: Range) -> Range:
        if self.intersection(second).empty_interval():
            return Range()
        ans_min = min(self.min, second.get_min())
        ans_max = max(self.max, second.get_max())
        return Range(ans_min, ans_max)
    
    def is_point_inside(self, point: int):
        if point is None or self.empty_interval():
            return False
        return self.min <= point and point <= self.max
    
    def equals(self, second: Range):
        return self.min == second.get_min() and self.max == second.get_max()
    
    def crossing(self, second: Range):
        if self.empty_interval() or second.empty_interval():
            return False
        ans_min = max(self.min, second.get_min())
        ans_max = min(self.max, second.get_max())
        return ans_min <= ans_max
    
    def is_inside(self, second: Range):
        if self.empty_interval() or second.empty_interval():
            return False
        return self.min <= second.get_min() and second.get_max() <= self.max
    
    def view_points(self) -> list:
        if self.empty_interval():
            return []
        answer = list()
        for i in range(self.min, self.max + 1):
            answer.append(i)
        return answer
    
    def out(self) -> str:
        if self.empty_interval():
            return '[]'
        return f'[{self.min}, {self.max}]'
        