class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = defaultdict(int)
        left = 0
        max_fruit = 0
        
        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left += 1
                
            max_fruit = max(max_fruit, (right-left+1))
        
        
        return max_fruit
        