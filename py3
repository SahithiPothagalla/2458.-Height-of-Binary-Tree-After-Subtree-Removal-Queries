# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def f(r, parent, brother, height, depth, lv):
    if r is None:
        return
    height[r.val] = lv
    depth[r.val] = lv
    if r.left is not None:
        parent[r.left.val] = r.val
        f(r.left, parent, brother, height, depth, lv+1)
        height[r.val] = max(height[r.val], height[r.left.val])
    if r.right is not None:
        parent[r.right.val] = r.val
        f(r.right, parent, brother, height, depth, lv+1)
        height[r.val] = max(height[r.val], height[r.right.val])
    if r.right is not None and r.left is not None:
        brother[r.right.val] = r.left.val
        brother[r.left.val] = r.right.val

def g(q, parent, brother, height, depth, x):
    if q not in x:
        z = 0
        if q in brother:
            z = height[brother[q]]
        if q in parent:
            z = max(z, depth[parent[q]], g(parent[q], parent, brother, height, depth, x))
        x[q] = z
    return x[q]
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        parent = dict()
        height = dict()
        brother = dict()
        depth = dict()
        f(root, parent, brother, height, depth, 0)
        x = dict()
        return [g(q, parent, brother, height, depth, x) for q in queries]
