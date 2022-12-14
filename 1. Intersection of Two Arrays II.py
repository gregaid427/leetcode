350. Intersection of Two Arrays II
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

===================================================================================================
Brute Force approach:
class Solution(object):
    def intersect(self, nums1, nums2):
        ls = []
        for i in nums1:
            if i in nums2:
                ls.append(i)
                nums2.remove(i)
        
        return ls
  
  ===================================================================================================
  Approach 2: Using collections.counter
  
  import collections
  def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())
=====================================================================================================
Approach 3: Using Hash

hash1 = {}
result = []
for i in nums1:
	if i in hash1:
		hash1[i]+=1
	else:
		hash1[i]=1
for i in nums2:
	if i in hash1 and hash1[i]>0:
		result.append(i)
		hash1[i]-=1
return result

