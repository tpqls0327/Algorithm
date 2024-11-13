class Solution:
    longest: int = 0  # "가장 긴 지름의 길이" 변수
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # 1. 자식이 없는 마지막 리프노드(말단노드)인경우 3번 과정에서 2를 더해주기 떄문에 -1로 설정 
            # 현재 노드의 지름 길이 : left 자식노드(-1) + right 자식노드(-1) + 현재노드까지 오는 길이(2) = 0
            # 위의 과정으로 말단노드의 값을 0으로 셋팅해줌
            if not node: 
                return -1
            # 2. 왼쪽, 오른쪽 리프노드 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # 3. 가장 긴 지름의 길이 구하기
            self.longest = max(self.longest, left+right+2)
            # 4. 현재 노드의 길이 반환
            return max(left, right) + 1
        # 5. dfs 수행
        dfs(root)    
        return self.longest
