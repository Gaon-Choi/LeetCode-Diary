import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode(0)

        temp = answer

        pq = []

        for idx, sorted_list in enumerate(lists):
            if sorted_list:
                heapq.heappush(pq, [sorted_list.val, idx])

        while len(pq) > 0:
            elem, idx = heapq.heappop(pq)

            tmp = ListNode(val = elem)
            temp.next = tmp
            temp = temp.next

            lists[idx] = lists[idx].next

            if lists[idx]:
                heapq.heappush(pq, [lists[idx].val, idx])

        return answer.next


