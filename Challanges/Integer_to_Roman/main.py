class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)

        res_list = []

        for rmn in l:
            num = 0

            if rmn == 'I':
                num = 1
            if rmn == 'V':
                num = 5
            if rmn == 'X':
                num = 10
            if rmn == 'L':
                num = 50
            if rmn == 'C':
                num = 100
            if rmn == 'D':
                num = 500
            if rmn == 'M':
                num = 1000

            res_list.append(num)

        for num in range(1, len(res_list)):
                if res_list[0] >= res_list[1]:
                    if len(res_list) >= 3:
                        if res_list[1]  >= res_list[2]:
                            temp = res_list[0] + res_list[1]
                            res_list[0] = temp
                            res_list.pop(1)
                        else:
                            temp = res_list[1] - res_list[0]
                            res_list[0] = temp
                            res_list.pop(1)
                    else:
                        temp = res_list[0] + res_list[1]
                        res_list[0] = temp
                        res_list.pop(1)

                else:
                    temp = res_list[1] - res_list[0]
                    res_list[0] = temp
                    res_list.pop(1)

        return res_list[0]



print(Solution.romanToInt(Solution, s="MCMXCIV"))