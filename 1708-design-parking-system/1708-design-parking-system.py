class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.curr = [0, 0, 0, 0]
        self.capacity = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.curr[carType] < self.capacity[carType]:
            self.curr[carType] += 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)