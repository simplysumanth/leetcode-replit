import ListNode
from typing import List

def twoSum(nums,target):
  """
  input -> [1,2,3,4,5,6]
  target -> 5
  Output -> [1,2]
  1.loop thru the n elements in the list: 
    1.1 find the diff between target and list[n]
    1.2 if the diff not already in hashMap:
      1.2.1 add list[n] as key and index as value
    1.3 if diff is in hashMap:
      1.3.1 return [hashMap[diff],i]
  """
  hashMap = {}
  print("Target : ", target)
  for i,n in enumerate(nums):
    print("i,n: ", i,n)
    diff = target-n
    print("diff : ", diff)
    print("hashMap : ", hashMap.items())
    if diff in hashMap:
      return [hashMap[diff],i]
    hashMap[n]=i

def validParentheses(s):
  """
  Input: s = "()"
  Output: true

  Explanation:
    An input string is valid if:
      * Open brackets must be closed by the same type of brackets.
      * Open brackets must be closed in the correct order.
      * Every close bracket has a corresponding open bracket of the same
        type.

  Solution:
    1. Create a stack and push for every opening bracket
    2. For closing, pop the top most element in the stack
      2.1 if popped element == opening of popped element -> proceed , else return false
    3. After all elements are looked, return true if stack is empty else false.
  """
  #Method 1 - Most efficient - took 23ms
  stack = []
  paranthesis = {")" : "(",  "}" : "{", "]" : "["}
  for i in s:
    if i in paranthesis:
      if stack and stack[-1] == paranthesis[i]:
        stack.pop()
      else:
        return False
    else:
      stack.append(i)
  return True if not stack else False

  #method 2 - same complexity - but took 50ms
  for i in s:
    if i in paranthesis.values():
      stack.append(i)
    elif i in paranthesis.keys():
      if len(stack) > 0:
        poppedElement = stack.pop(len(stack)-1)
        if not poppedElement == paranthesis[i]:
          return False
      else:
        return False
    else:
      return False
  if len(stack)>0:
    return False
  else:
    return True

def mergeTwoLists(list1, list2):
  """
  This doesn't work on repl, but it does on leetcode -> https://leetcode.com/problems/merge-two-sorted-lists/submissions/
  """
  dummy = ListNode()
  tail = dummy
  while list1 and list2:
      if list1.val<list2.val:
          tail.next = list1
          list1 = list1.next
      else:
          tail.next = list2
          list2 = list2.next
      tail = tail.next
  if list1:
      tail.next = list1
  elif list2:
      tail.next = list2

  

  return dummy.next

def maxProfit(prices: List[int]) -> int:
  """
  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
  """
  #input -> maxProfit([7,1,5,3,6,4])
  # SOLUTION - 1
  # left = 0 #buy
  # right = 1 #right
  # current_profit = 0
  # while right < len(prices):
  #   profit = prices[right] - prices[left]
  #   if prices[left] < prices[right]:
  #     current_profit = max(profit,current_profit)
  #   else:
  #     left = right
  #   right += 1
  # return current_profit
  buy = prices[0]
  profit = 0
  for sell in prices[1:]:
    if sell<buy:
      buy = sell
    if sell - buy > profit:
      profit = sell - buy
  return profit

def majorityElement( nums: List[int]) -> int:
  '''
  https://leetcode.com/problems/majority-element/

  Given an array nums of size n, return the majority element.
  The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume    that the majority element always exists in the array.

  Input -> majorityElement([3,3,4])
  '''
  # SOLUTION - 1
  # count_map = {}
  # for i in nums:
  #   if i not in count_map:
  #     count_map[i] = 1
  #   else:
  #     count_map[i] += 1
  # return max(count_map, key=count_map.get)
  list_set = set(nums)
  count_map = {}
  for i in list_set:
    count_map[nums.count(i)]=i
  return count_map[max(count_map)]    

def lengthOfLongestSubstring(s:str):
  '''
  Given a string s, find the length of the longest substring without repeating characters.
  https://leetcode.com/problems/longest-substring-without-repeating-characters/

  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

  Solution: Sliding window - abcab
  1. Init a set() with number : index
  2. have 2 pointers Right and Left (both contains index values) - R is range(s), L is the         left most part of window
  3. For every iteration of R, check if s[R] in set()
    3.1. If Yes : Remove S[L] until the window has no duplicates 
    3.2. Then add S[R] to set() and store max lenght - max(current_res, r-l+1) and return it           atlast.
  '''

  charSet = set()
  l = 0
  res = 0
  for r in range(len(s)):
    while s[r] in charSet:
      charSet.remove(s[l])
      print("removing .. ", s[r], charSet)
      l+=1
    charSet.add(s[r])
    print(charSet)
    res = max(res,r-l+1)
    print(res)
  return res

def addBinary(a:str,b:str):
  '''
  Given two binary strings a and b, return their sum as a binary string.

  Input: a = "1010", b = "1011"
  Output: "10101"

  Solution : 
  0. create carry = 0
  1. get the last digit from each string and do sum 
    1.1 if sum is 1+1 then carry = 1 Else 1+0 or 0+1 = 1 (normal)
    1.2 Move to next digit and check for carry - if present add that and continue 
  '''
  carry = 0
  new_str = ""
  a,b = a[::-1],b[::-1]
                                  #a = 11 b = 1
  for i in range(max(len(a),len(b))):
    digitA = int(a[i]) if i < len(a) else 0
    digitB = int(b[i]) if i < len(b) else 0

    sum = digitA + digitB + carry  #sum = 1+1+0 = 2              1+0+1 = 2  
    char = str(sum%2)              # char = 2%2 = 0 (remainder)  2%2 = 0  
    new_str = char + new_str       #new_str = "0"                "00"
    carry = sum//2                #carry = 2//2 = 1 (division)   2//2 = 1

  if carry:                          #carry =1 
    new_str = "1" + new_str          #new_str = "1" + "00" -> "100"
  return new_str
  

def isPalindrome(s:str):
  '''
  https://leetcode.com/problems/valid-palindrome/
  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all      non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters     and numbers.

  Given a string s, return true if it is a palindrome, or false otherwise.

  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
  '''
  res = ''
  for i in s.lower():
    if i.isalnum()==True:
      res = i+res
  return res == res[::-1]
  

def longestCommonPrefix(strs: List[str]):
  '''
  https://leetcode.com/problems/longest-common-prefix/
  
  Write a function to find the longest common prefix string amongst an array of strings.
  If there is no common prefix, return an empty string "".

  Input: strs = ["flower","flow","flight"]
  Output: "fl"
  '''

  smallElement = min(strs,key=len)
  for i in strs:
    while smallElement != i[0:len(smallElement)]:
      print(smallElement, i[0:len(smallElement)])
      smallElement = smallElement[:-1]  
  return smallElement

def romanToInt(s : str):
  '''
  https://leetcode.com/problems/roman-to-integer/
  
  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
  
  Input: s = "III"
  Output: 3
  Explanation: III = 3.

  Input: s = "IX"
  Output: 9
  Explanation: IX = 9.

  Solution:
  1. from left get the digit and idx
  2. multiply with 10 for every digit (iteration)
  '''

  hashMap = {'I': 1,'V':5,'X':10,'L' :50,'C':100,'D':'500','M':1000}
  res = 0;
  for i in range(len(s)):
    if i<len(s)-1 and hashMap[s[i]] < hashMap[s[i+1]]:
      res = res - hashMap[s[i]]
    else:
      res = res + hashMap[s[i]]
  
  return res

def convertToTitle(s:str):
  '''
  Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
  For example:
  A -> 1
  B -> 2
  C -> 3
  ...
  Z -> 26
  AA -> 27
  AB -> 28 

  Input: columnNumber = 28
  Output: "AB"

  Input: columnNumber = 701
  Output: "ZY"
...
  
  '''

  return