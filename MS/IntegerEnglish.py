class Solution(object):
    def numberToWords(self, num):
        result = ""
        nums = [x for x in str(num)]
        nums.reverse()
        place = 1
        numbers_map = dict()
        for x in nums:
            numbers_map[x,place] = int(x) * place
            place *= 10

        word_map = {
            1: "One",2:"Two",3: "Three",4: "Four",5: "Five",6: "Six",7:"Seven",8: "Eight",9: "Nine",10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
            20: "Twenty",30: "Thirty",40: "Forty",50: "Fifty",60: "Sixty",70: "Seventy",80: "Eighty",90: "Ninenty",100: "One Hundred"}


        words = [x for x in numbers_map.values()]
        words.sort(reverse=True)

        for val in words:
            result += word_map[val] + " "
        return result.tri
        # place variable starting at 10
        # starting for the first index, store in map * place
        # multiple place by 10 and move until we've reached end of the num

        # store numbers and the word in a map

        # for each value in map, get the num from the word map and append to word

Solution.numberToWords("", 12345)