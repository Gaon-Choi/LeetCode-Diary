class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        curr = 0
        max_altitude = 0

        for elem in gain:
            altitude.append(curr + elem)
            max_altitude = max(max_altitude, curr + elem)
            curr += elem

        return max_altitude