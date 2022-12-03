'''
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_counter = {}
        answer = ''
        for letter in s:
            if letter in freq_counter:
                freq_counter[letter] += 1
            else:
                freq_counter[letter] = 1
        freq_counter_sorted = sorted(freq_counter,key=freq_counter.get, reverse=True)
        for key in freq_counter_sorted:
            print(f' key: {key} and value: {freq_counter[key]}')
            answer += "".join(key*freq_counter[key])
        return answer
'''


from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        count = Counter(s)
#        count.most_common()
#        print(type(count))
        print(count)
        for pair in count.most_common():
            print(f' key: {pair[0]} and value: {pair[1]}')
            answer += "".join(pair[0]*pair[1])
        return answer

obj = Solution()
print(obj.frequencySort('tree'))
print(obj.frequencySort('cccaaa'))
print(obj.frequencySort('Aabb'))

