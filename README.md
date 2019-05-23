# Perfect-Or-Nothing-Environment
The environment of final project "Perfect or Nothing" in course Probability2019@NTU

## agent_define.py
All you need to do is to rewrite the classes in agent_define.py
* __init__() will create a class
* Since the created class will be tested several times, please initialize your variables inside restart()
* In one simulation process, we will call decide() of your class N times, and each time with a value, you should decide whether to pick up the value or not

## main.py
The method we test your scripts.

## game_define.py
Define the game.
* get_values() will get the values of one simulation time.
* evaluate_one_simulation() will determine whether you pick the best value or not
* evaluate() will simulation `SIMUL_TIMES` and calculate the average performance