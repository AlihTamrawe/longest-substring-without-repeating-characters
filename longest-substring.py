class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = ""
        if s == " ":
            return 1
        if s == "" :
            return 0
        arr +=s[0]
        maxs = 1
        max2 = 1
        lengthString = len(s)
        print (s[0])
        temp = ""
        for i in range(1,lengthString-maxs+1):
            temp = s[i]
            if arr.find(temp)!=-1:
                while arr.find(temp)!=-1: 
                    arr= arr[1:]
                    print(arr)
                arr+=temp
            else:
                arr+=temp
            maxs= len(arr)
            print(maxs)
            if max2 <maxs:
                max2=maxs
        return max2


        # for x in range(1,len(s)):
        #     if arr.find(s[x]) != -1:
        #         arr=s[x]
        #         if counter>=maxs:
        #             maxs=counter
        #         counter = 1
        #     else:
        #         counter+=1
        #         arr+=s[x]
        #         print(arr)
        #     temp= s[x]
        # if counter>maxs :
        #     maxs=counter
        # return maxs

        