class Stack:
    def __init__(self):
        self.items = []
      
    def isEmpty(self):
        return self.items == []
      
    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        return self.items.pop()
      
    def peek(self):
        return self.items[len(self.items)-1]
      
    def size(self):
        return len(self.items) 
    
#solve 
def del_mid_element(st, n, curr):
    if (st.isEmpty() or curr == n) :
        return
      
    # Remove current item
    x = st.peek()
    st.pop()
      
    # Remove other items
    del_mid_element(st, n, curr+1)
      
    # Put all items back except middle
    if (curr != int(n/2)) :
        st.push(x)

st = Stack()
  
# push elements into the stack
st.push('1')
st.push('2')
st.push('3')
st.push('4')
st.push('5')
st.push('6')
st.push('7')
  
del_mid_element(st, st.size(), 0)
  
# Printing stack after deletion
# of middle.
while (st.isEmpty() == False) :
    p = st.peek()
    st.pop()
    print (str(p) + " ", end="")