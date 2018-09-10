def insertion_sort_ll(head):
    if head:
        next, arr = head, []
        while next:
            arr.append(next)
            for i in range(0, len(arr)):
                for j in range(len(arr) - 1, i, -1):
                    if arr[j - 1] > arr[j]:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    else: break
            next = next.next
        next = head = arr.pop(0)
        while arr:
            next.next = arr.pop(0)
            next = next.next
            next.next = None
        return head
