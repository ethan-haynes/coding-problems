def partition(head, x):
  """
  :type head: ListNode
  :type x: int
  :rtype: ListNode
  """
  if not head: return None
  lt, gte, next = [], [], head

  while next:
    tmp, next = next, next.next
    tmp.next = None
    if tmp.val < x:
      lt.append(tmp)
      if 1 < len(lt): lt[-2].next = lt[-1]
    else:
      gte.append(tmp)
      if 1 < len(gte): gte[-2].next = gte[-1]
              
  if lt and gte:
    lt[-1].next = gte[0]
  return lt[0] if lt else gte[0]
    
