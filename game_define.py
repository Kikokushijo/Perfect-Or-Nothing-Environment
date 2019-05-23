import numpy as np
import agent_define
import matplotlib.pyplot as plt

SIMUL_TIMES = 10000
PRINT_PER_SIMUL_TIMES = 1000
N = 1000

class Game(object):

    def __init__(self, setting, agents, k=0):
        self.setting = setting
        self.agents = agents
        self.k = k
        assert setting in ['basic-1', 'basic-2', 'basic-3', \
                           'advanced-1-Uniform', 'advanced-1-Normal', 'advanced-2']
        assert (setting in ['basic-2', 'basic-3', 'advanced-2']) == (k != 0)

    def get_values(self):
        if self.setting in ['basic-1', 'basic-2', 'basic-3']:
            # try to make unknown distribution
            values = []
            for i in range(87):
                values.append(np.random.chisquare(np.random.randint(3, 387), size=(np.random.randint(12, 148),)))
            values = np.concatenate(values, axis=None)[:N]
            np.random.shuffle(values)
        elif self.setting == 'advanced-1-Normal':
            mean = np.random.uniform(-10000, 10000)
            std = np.random.uniform(0, 10000)
            values = np.random.normal(loc=mean, scale=std, size=(N,))
        elif self.setting == 'advanced-1-Uniform':
            upper = np.random.uniform(0, 10000)
            lower = np.random.uniform(-10000, 0)
            values = np.random.uniform(low=lower, high=upper, size=(N,))
        elif self.setting == 'advanced-2':
            values = np.random.uniform(low=0, high=1, size=(N,))
            shift = np.arange(1, N+1) / N / self.k
            values += shift
        return values

    def evaluate(self):
        
        score = np.zeros(len(self.agents))

        for i in range(1, SIMUL_TIMES+1):

            for agent in self.agents:
                agent.restart()

            chances = np.ones(len(self.agents), dtype=np.int32)
            if self.setting == 'basic-3':
                chances *= self.k
            choices = [set() for _ in range(len(self.agents))]

            values = self.get_values()
            for value_idx, value in enumerate(values):
                for agent_idx, (agent, chance, choice) in enumerate(zip(self.agents, chances, choices)):
                    # still has chance deciding to pick
                    if chance:
                        result = agent.decide(value)
                        if result:
                            choice.add(value_idx)
                            chances[agent_idx] -= 1
            score += self.evaluate_one_simulation(values, choices)

            if i % PRINT_PER_SIMUL_TIMES == 0:
                print('Has simulated %d of %d times' % (i, SIMUL_TIMES))

        return score / SIMUL_TIMES

    def evaluate_one_simulation(self, values, choices):

        if self.setting == 'basic-2':
            ans = set(np.argsort(values)[-self.k:])
        else:
            ans = set([np.argmax(values)])

        # print(values, choices, ans)

        hit_list = np.array([int(bool(ans & choice)) for choice in choices])
        return hit_list