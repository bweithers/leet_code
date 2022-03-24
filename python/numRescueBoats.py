class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l,r= 0,len(people)-1
        while people:
            boats+=1
            if people[-1]+people[0] <= limit: 
                people.pop(0)
            if people: people.pop()
        return boats