class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n: return 0
        
        @cache
        def rec(dice,total):
            # if we have rolled all die stop. If we are at target, add one.
            if dice == n: return total == target
            # early stopping, dont count if we are already past target
            if total > target: return 0
            
            # check how many combos for this tree
            rv = 0
            # roll one die
            dice += 1
            
            # go through each of its possible rolls, create a call tree
            for face in range(1,k+1):
                total += 1
                
                # early stopping
                if total > target: break
                # Create the call tree checking all possible rolls for all other dice
                rv += rec(dice,total)
            return rv%(10**9+7)
        
        
        return rec(0,0)