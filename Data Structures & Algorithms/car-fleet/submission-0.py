class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)   # closest to the target first
        fleets = 0
        fleet_time = 0.0                                    # arrival time of the fleet in front

        for pos, spd in cars:
            time = float(target - pos) / spd                # hours to finish if nothing blocked it
            if time > fleet_time:                           # arrives later than the fleet ahead, so it can't catch up
                fleets += 1
                fleet_time = time                           # this car now leads a new fleet
        return fleets