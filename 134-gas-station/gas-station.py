class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_gas = current_gas = starting_station = 0 
        
        # run n-1 times station to fill gas 
        for i in range(n):
            total_gas += gas[i]-cost[i]
            # print(i,total_gas)
            """
            (0, -2)
            (1, -4)
            (2, -6)
            (3, -3)
            (4, 0)

            """
            current_gas += gas[i]-cost[i]

            if current_gas < 0:
                starting_station = i+1

                current_gas= 0
        
        return starting_station if total_gas >= 0 else -1
             