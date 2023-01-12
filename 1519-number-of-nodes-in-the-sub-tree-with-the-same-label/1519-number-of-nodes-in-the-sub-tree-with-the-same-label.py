class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def post_order(cur, parent):
            tmp_cnt = [0] * 26
            tmp_cnt[ord(labels[cur]) - ord('a')] += 1
            
            for child in d[cur]:
                if child == parent:
                    continue
                    
                child_val = post_order(child, cur)

                for i in range(26):
                    tmp_cnt[i] += child_val[i]
                
            ans = tmp_cnt[ord(labels[cur]) - ord('a')]
            ret[cur] = ans
            return tmp_cnt
                
                
        d = defaultdict(list)
        
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
            
        ret = [0] * n
        post_order(0, -1)
        return ret
    