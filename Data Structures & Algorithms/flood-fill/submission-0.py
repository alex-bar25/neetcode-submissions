class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        if image[sr][sc] == color:
            return image

        original_color = image[sr][sc]

        def dfs(sr, sc):
            if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
                return
            if image[sr][sc] != original_color:
                return

            image[sr][sc] = color

            dfs(sr - 1, sc)
            dfs(sr + 1, sc)
            dfs(sr, sc - 1)
            dfs(sr, sc + 1)

        dfs(sr, sc)
        
        return image