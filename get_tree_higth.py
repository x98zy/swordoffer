"""获取一个二叉树高度"""

def depth(root):
    if not root:
        return 0
    left=depth(root.left)
    right=depth(root.right)
    return max(left,right)+1