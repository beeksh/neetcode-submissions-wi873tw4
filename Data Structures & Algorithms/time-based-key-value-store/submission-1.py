class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value, timestamp])
        else:
            self.d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        x = self.d[key]
        l, r = 0, len(x) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if x[m][1] == timestamp:
                return x[m][0]

            if x[m][1] < timestamp:
                res = x[m][0]
                l = m + 1
            else:
                r = m - 1

        return res