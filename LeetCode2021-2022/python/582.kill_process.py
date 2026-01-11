class Solution:
    from collections import defaultdict
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        if not pid and not ppid:
            return []
        
        
        g = defaultdict(list)
        root = 0
        for i, _id in enumerate(pid):
            g[ppid[i]].append(_id)
            if ppid[i] == 0:
                root = _id
        q =[(root, kill==root)]
        killed =[]
        while q:
            node, isKill =q.pop(0)
            if isKill:
                killed.append(node)
            for neigh in g[node]:
                q.append((neigh, kill == neigh or isKill))
        
        return killed
