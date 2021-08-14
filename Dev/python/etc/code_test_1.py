# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self,li1,li2):
        self.li1 = li1
        self.li2 = li2
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1 = self.li1[::-1]
        li2 = self.li2[::-1]
        num1 = "".join([str(_) for _ in li1])
        num2 = "".join([str(_) for _ in li2])
        calc = int(num1) + int(num2)
        calc_list = list(str(calc))
        calc_list = [int(i) for i in calc_list][::-1]
        return calc_list


if __name__ =="__main__":
    li1 = input()
    li2 = input()
    li1 = eval(li1)
    li2 = eval(li2)
    solution = Solution(li1,li2)
    result = solution.addTwoNumbers(li1,li2)
