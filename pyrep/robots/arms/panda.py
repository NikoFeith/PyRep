from pyrep.robots.arms.arm import Arm


class Panda(Arm):
    def __init__(self, count: int = 0, max_velocity=1.0,
                 max_acceleration=4.0, max_jerk=1000):
        super().__init__(count, "Panda", 7,
                         max_velocity=max_velocity,
                         max_acceleration=max_acceleration,
                         max_jerk=max_jerk)
