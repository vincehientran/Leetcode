class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        queue = [(sr, sc)]
        color = image[sr][sc]

        while queue:

            for _ in range(len(queue)):
                i, j = queue.pop(0)

                if color == image[i][j] and newColor != image[i][j]:
                    image[i][j] = newColor

                    if i > 0:
                        queue.append((i-1, j))
                    if j > 0:
                        queue.append((i, j-1))
                    if i < len(image) - 1:
                        queue.append((i+1, j))
                    if j < len(image[0]) - 1:
                        queue.append((i, j+1))

        return image
