class BinarySearch(list):

    def __init__(self, a, b): 
        self.maxVal = a
        self.step = b
        self.mylist = []
        self.length = a
       
        for x in range(self.maxVal):
            list.append(self, self.step)
            self.mylist.append(self.step)
            self.step += b
   

    def search(self,value):
        left = 0
        right = self.length-1
        found = False
        count = 0
        exists = False
        
        if value == self.mylist[0]:
            return {"count":0,"index":0}
            
        if value == self.mylist[self.length-1]:
            return {"count":0,"index":self.length-1}    
       
        try:
          index = self.index(value)
          exists = True
        except ValueError:
          index = -1
          exists = False
          
       
        while left<=right and value != self[right] and exists and not found:
            mid_point = (left+right)//2
            mid_value = self[mid_point]
            if mid_value == value:
                found = True

                count +=1
                index = mid_point
            else:
                if value < mid_value:
                    right = mid_point - 1
                    count +=1
                else:
                    left = mid_point + 1
                    count +=1
            
            if left > right:
                return {'count': 0, 'index': -1}
                       
        return {"count": count, "index": index}