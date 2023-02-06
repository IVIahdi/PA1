import random
class ServerAgent:
    def __init__(self,small_count=10,medium_count=10,large_count=10):
        self.small_count = small_count
        self.medium_count = medium_count
        self.large_count = large_count
    def select_action(self,percept):
        if percept in range(0,34):
            if self.large_count > 0:
                self.large_count -= 1
                return "large"
            else:
                return None
        elif percept in range(34,67):
            if self.medium_count > 0:
                self.medium_count -= 1
                return "medium"
            else:
                return None
        elif percept in range(67,100):
            if self.small_count > 0:
                self.small_count -= 1
                return "small"
            else:
                return None
        elif percept >= 100:
            return None
    def storage_empty(self):
        return True if (self.large_count == 0 and self.small_count == 0 and self.medium_count == 0) else False

class ServerEnvironment:
    def __init__(self,server_agent):
        self.server_agent = server_agent
        self.num_agent_actions=0 
    def tick(self):
        h2 = random.randint(a=0, b=130)
        r = self.server_agent.select_action(h2)
        self.num_agent_actions += 1
    def simulate(self):
        while not self.server_agent.storage_empty():
            self.tick()


