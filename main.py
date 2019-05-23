from game_define import Game, N
from agent_define import *

g = Game(setting='basic-1', agents=[Agent(N)])
print('Basic-1 Score:', g.evaluate())

g = Game(setting='basic-2', agents=[Basic_2_Agent(N, 2)], k=2)
print('Basic-2 Score for k = 2:', g.evaluate())

g = Game(setting='basic-2', agents=[Basic_2_Agent(N, 5)], k=5)
print('Basic-2 Score for k = 5:', g.evaluate())

g = Game(setting='basic-2', agents=[Basic_2_Agent(N, 20)], k=20)
print('Basic-2 Score for k = 20:', g.evaluate())

g = Game(setting='basic-3', agents=[Basic_3_Agent(N, 2)], k=2)
print('Basic-3 Score for k = 2:', g.evaluate())

g = Game(setting='basic-3', agents=[Basic_3_Agent(N, 5)], k=5)
print('Basic-3 Score for k = 5:', g.evaluate())

g = Game(setting='basic-3', agents=[Basic_3_Agent(N, 20)], k=20)
print('Basic-3 Score for k = 20:', g.evaluate())

g = Game(setting='advanced-1-Uniform', agents=[Advanced_1u_Agent(N)])
print('Advanced-1-Uniform Score:', g.evaluate())

g = Game(setting='advanced-1-Normal', agents=[Advanced_1n_Agent(N)])
print('Advanced-1-Normal Score:', g.evaluate())

g = Game(setting='advanced-2', agents=[Advanced_2_Agent(N, 100)], k=100)
print('Advanced-2 Score:', g.evaluate())