class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        result = []
        
        for j in range(cols):
            i, k = 0, j
            while i < rows and k < cols:
                result.append(encodedText[i * cols + k])
                i += 1
                k += 1
        
        return ''.join(result).rstrip()
