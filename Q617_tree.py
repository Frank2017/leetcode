# # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode        
        """
        root = None
        return self._create_m_tree(root, t1, t2)
        pass
    def _create_m_tree(self, root, t1, t2):
        val = 0
        flag = False
        if t1 is not None:
            flag = True
            val += int(t1.val)
        if t2 is not None:
            flag = True
            val += int(t2.val)
        if flag == False:
            root = None
        else:
            root = TreeNode(val)
            t1_next = t1.left if t1 is not None else None
            t2_next = t2.left if t2 is not None else None
            root.left = self._create_m_tree(root.left, t1_next, t2_next)
            t1_next = t1.right if t1 is not None else None
            t2_next = t2.right if t2 is not None else None
            root.right = self._create_m_tree(root.right, t1_next, t2_next)
        return root
        pass


def pre_order(t):
    if t == None:
        return
    else:
        print t.val
        pre_order(t.left)
        pre_order(t.right)

def create_tree(t):
    a = raw_input('enter a number:')
    if a == '#':
        t = None
    else:
        t = TreeNode(a)
        t.left = create_tree(t.left)
        t.right = create_tree(t.right)
    return t
    pass


if __name__ == '__main__':
    root1 = None
    print 'create tree 1'
    root1 = create_tree(root1)
    root2 = None
    print 'create tree 2'
    root2 = create_tree(root2)
    root_m = Solution().mergeTrees(root1, root2)
    pre_order(root_m)
    pass