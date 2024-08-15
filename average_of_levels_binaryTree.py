from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])  # Queue stores pairs of (node, level)
        
        while queue:
            node, level = queue.popleft()
            
            # Ensure the result list is long enough to hold the sum for this level
            if level == len(result):
                result.append((0, 0))  # (sum, count)
            
            # Update sum and count for the current level
            current_sum, current_count = result[level]
            result[level] = (current_sum + node.val, current_count + 1)
            
            # Add child nodes to the queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Calculate the averages
        averages = [sum_val / count for sum_val, count in result]
        
        return averages

# Example usage
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
print(solution.averageOfLevels(root1))  # Output: [3.0, 14.5, 11.0]

