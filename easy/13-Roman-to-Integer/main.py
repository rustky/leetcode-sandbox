class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lookup_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        value = 0
        counter = len(s)-1
        while counter>=0:
            current_letter = s[counter]
            next_letter = s[counter-1]
            if counter != 0:
                if current_letter == "I":
                    if next_letter == "V":
                        value += 4
                        counter -= 1
                    elif next_letter == "X":
                        value += 9
                        counter -= 1
                    else:
                        value = value + lookup_dict[current_letter]
                elif current_letter == "X":
                    if next_letter == "L":
                        value += 40
                        counter -= 1
                    elif next_letter == "C":
                        value += 90
                        counter -= 1
                    else:
                        value = value + lookup_dict[current_letter]
                elif current_letter == "C":
                    if next_letter == "D":
                        value += 400
                    elif next_letter == "M":
                        value += 900
                    else:
                        value = value + lookup_dict[current_letter]
            else:
                value = value + lookup_dict[current_letter]
            counter -= 1
            print(value)
        return value

if __name__ == "__main__":
    test_case_one = "LVIII"
    foo = Solution()
    print(foo.romanToInt(test_case_one))

