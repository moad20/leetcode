class Solution:
    def twoP(self,x,nums,n):
        i,j=0,0
        ans=sys.maxsize
        freq=defaultdict(lambda:0)
        while i<=j and j<n:
            freq[nums[j]]+=1
            if freq[nums[j]]==x:
                while nums[j]!=nums[i]:
                    freq[nums[i]]-=1
                    i+=1
                ans=min(ans,j-i+1)
            j+=1
        return ans          
            
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans=sys.maxsize
        n=len(nums)
        x=max(Counter(nums).values())
        return self.twoP(x,nums,n)