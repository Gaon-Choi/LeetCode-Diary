class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        size = len(image)
        row_size = len(image[0])

        for i in range(size):
            image[i] = image[i][-1::-1]

            for j in range(row_size):
                image[i][j] = image[i][j] ^ 1

        return image