/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 // O(n) runtime
 // Runtime beats 98.95 % of javascript submissions on leetcode
var addTwoNumbers = function(l1, l2) {
  const list = []
  const itr = (ll1, ll2, num) => {
    let val = num + (ll1.val || 0) + (ll2.val || 0)
    if (ll1.next || ll2.next)
        return list.push(val%10), itr(ll1.next || 0, ll2.next || 0, Math.floor(val/10))
    else
        if (val === 0 || Math.ceil(Math.log10(val+1)) === 1)
          return val
        else
          return list.push(val%10), Math.floor(val/10)
  }
  return list.push(itr(l1, l2, 0)), list
}

// test setup
function ListNode(val) {
   this.val = val
   this.next = null
}

let input1 = new ListNode(3)
input1.next = new ListNode(4)
input1.next.next = new ListNode(2)

let input2 = new ListNode(4)
input2.next = new ListNode(6)
input2.next.next = new ListNode(5)
console.log(addTwoNumbers(input1, input2)) // [7,0,8]
