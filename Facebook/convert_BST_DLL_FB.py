# merge(fuse) two sorted linked lists
def concatenate_lists(head1, head2):
    
    if head1 == None:
      return head2

    if head2 == None:
        return head1
    
    # use left for previous.
    # use right for next.
    tail1 = head1.left
    tail2 = head2.left
    
    tail1.right = head2
    head2.left = tail1
    
    head1.left = tail2
    tail2.right = head1
    return head1

def convert_to_linked_list(root):
    
    if root == None:
        return None
    
    list1 = convert_to_linked_list(root.left)
    list2 = convert_to_linked_list(root.right)
    
    root.left = root.right = root
    result = concatenate_lists(list1, root)
    result = concatenate_lists(result, list2)
    
    return result
  
def get_list(head):
    r = []
    if head == None:
        return r
    
    temp = head
    while True:
        r.append(temp.data)
        temp = temp.right
        if temp == head:
          break

    return r

def test(orig_data):
  
  root = create_BST(orig_data)
  
  all_data = bst_to_list(root)
  #print(all_data);
  
  head = convert_to_linked_list(root)
  #print_list(all_data)
  #print_list(v)

  return head

def main():
   
  data = [100,50,200,25,75,350]
  res = test(data) 
  v = get_list(res)
  print_list(v)

main() 
