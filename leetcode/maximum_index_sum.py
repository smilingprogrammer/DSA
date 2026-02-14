class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output = {}

        for index, value in enumerate(list1):
            output[value] = index

        for index, value in enumerate(list2):
            if value in output:
                output[value] += index

        result = {}
        for key, value in output.items():
            if key in list1 and key in list2:
                result[key] = value

        minimum = min(result.values())

        final = []
        for key, value in result.items():
            if value == minimum:
                final.append(key)

        return final