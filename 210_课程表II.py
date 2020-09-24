from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        elif len(prerequisites)>numCourses*(numCourses-1)/2: #有环
            return []
        ret = []
        remains = {*range(numCourses)}
        noprerequisites_node = self.find_noprerequisites_node(prerequisites)
        while(noprerequisites_node):
            _node = noprerequisites_node[0]
            ret.append(_node)
            remains.remove(_node)
            prerequisites=self.del_edge(prerequisites, _node)
            noprerequisites_node = self.find_noprerequisites_node(prerequisites)
        if len(prerequisites):
            return []
        else:
            ret.extend(remains)
            return ret
    # 在现有的邻接列表中随机返回一个无前驱节点
    def find_noprerequisites_node(self, prerequisites):
        all_forward = {forawrd_node for _, forawrd_node in prerequisites}
        all_back = {back for back, _ in prerequisites}
        return list(all_forward - all_back)
    # 删除某个节点为前驱结点的边
    def del_edge(self, prerequisites, target_node):
        return list(filter(lambda x:x[1]!=target_node, prerequisites))
        
        
sol = Solution()
prerequisites =[[2,1],[1,0]]
ans = sol.findOrder(3,prerequisites)
print(ans)

