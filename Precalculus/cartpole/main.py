import gym
import numpy as np

from dqn_solver import DQNSolver
from score_logger import ScoreLogger
from static_solver import StaticSolver

ENV_NAME = 'CartPole-v1'


def run(solver='static'):
    env = gym.make(ENV_NAME)
    score_logger = ScoreLogger(ENV_NAME)
    observation_space = env.observation_space.shape[0]
    run = 0

    if solver == 'static':
        static_solver = StaticSolver()
        while True:
            run += 1
            state = env.reset()
            state = np.reshape(state, [1, observation_space])
            step = 0
            while True:
                step += 1
                env.render()
                action = static_solver.act(state)
                state_next, reward, terminal, info = env.step(action)
                state_next = np.reshape(state_next, [1, observation_space])
                state = state_next
                if terminal:
                    print('Run: ' + str(run) + ', score: ' + str(
                        step))
                    score_logger.add_score(step, run)
                    break
    elif solver == 'dqn':
        action_space = env.action_space.n
        dqn_solver = DQNSolver(observation_space, action_space)
        while True:
            run += 1
            state = env.reset()
            state = np.reshape(state, [1, observation_space])
            step = 0
            while True:
                step += 1
                env.render()
                action = dqn_solver.act(state)
                state_next, reward, terminal, info = env.step(action)
                reward = reward if not terminal else -reward
                state_next = np.reshape(state_next, [1, observation_space])
                dqn_solver.remember(state, action, reward, state_next, terminal)
                state = state_next
                if terminal:
                    print('Run: ' + str(run) + ', exploration: ' + str(dqn_solver.exploration_rate) + ', score: ' + str(
                        step))
                    score_logger.add_score(step, run)
                    break
                dqn_solver.experience_replay()


def main():
    solver = 'dqn'
    run(solver)


if __name__ == '__main__':
    main()
