class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            # clone the node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # clone neighbors
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)
