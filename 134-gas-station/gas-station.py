class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
       # return -1 if the total gas is less than the total cost
        if sum(gas) < sum(cost):
            return -1

        current_tank, starting_station, num_stations = 0, 0, len(gas)
        for station in range(num_stations):
            current_tank += gas[station] - cost[station]
            # if current_tank is negative, update starting_station to the next station
            # and reset current_tank to 0
            if current_tank < 0:
                starting_station = station + 1
                current_tank = 0 
        
        # return starting_station
        return starting_station



