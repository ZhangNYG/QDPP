import argparse

import gym

from ma_gym.wrappers import Monitor
from ma_gym.wrappers.pymarl_env_wrapper import PyMARLEnvWrapper

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Random Agent for ma-gym')
    parser.add_argument('--env', default='PredatorPrey5x5-v0',
                        help='Name of the environment (default: %(default)s)')
    parser.add_argument('--episodes', type=int, default=1,
                        help='episodes (default: %(default)s)')
    args = parser.parse_args()

    env = gym.make(args.env)
    env = Monitor(env, directory='recordings/' + args.env, force=True)

    # w_env = PyMARLEnvWrapper(env)
    # print(w_env.get_avail_agent_actions(0))

    for ep_i in range(args.episodes):
        done_n = [False for _ in range(env.n_agents)]
        ep_reward = 0

        env.seed(ep_i)
        obs_n = env.reset()
        env.render()

        while not all(done_n):
            action_n = env.action_space.sample()
            obs_n, reward_n, done_n, info = env.step(action_n)
            ep_reward += sum(reward_n)
            env.render()

        print('Episode #{} Reward: {}'.format(ep_i, ep_reward))
    env.close()
