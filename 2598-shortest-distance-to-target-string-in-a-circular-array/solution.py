class Solution:
    def closestTarget(self, W: List[str], t: str, s: int) -> int:
        return next((i for i in range(len(W) // 2 + 1) if W[s - i] == t or W[s + i - len(W)] == t), -1)
