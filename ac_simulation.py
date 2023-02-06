class SimpleACReflexAgent:
    def __init__(self, min_threshold, max_threshold):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

    def select_action(self,percept):
        # return "TurnOn" if (percept[0] >= self.max_threshold and not percept[1]) else "TurnOff" if (percept[0] <= self.min_threshold and percept[1]) else None
        if (percept[0] >= self.max_threshold) and (not (percept[1])):
            return "TurnOn"
        elif (percept[1] and percept[0] <= self.min_threshold):
            return "TurnOff"
        else:
            return None


class SimpleACEnvironment:
    def __init__(self, ac_agent, starting_temp=28):
        self.ac_agent = ac_agent
        self.temperature = starting_temp
        self.num_agent_actions = 0
        self.is_ac_on = False
    def tick(self):
        self.status = self.ac_agent.select_action([self.temperature,self.is_ac_on])
        if self.status != None:
            self.num_agent_actions += 1
            self.is_ac_on = True if self.status == "TurnOn" else False
        self.temperature = self.temperature - 1 if self.is_ac_on else self.temperature + 1
    def simulate(self,num_timesteps):
        for i in range(num_timesteps):
            self.tick()
