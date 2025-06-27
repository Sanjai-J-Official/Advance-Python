 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1,num2=a,b
        i,j=len(a)-1,len(b)-1
        result=""
        carry=0
        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(num1[i])
                i-=1
            if j>=0:
                total+=int(num2[j])
                j-=1
            result=str(total%2)+result
            carry=total//2
        return result 
