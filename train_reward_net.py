from datetime import datetime
import importlib
import json
import os
from glob import glob
import argparse
import torch

from torchsummary import summary

from reward_nets.base_reward_net import RewardNet

default_env = 'MiniGrid-Empty-6x6-v0'
default_reward = "reward_nets/conv_reward/reward_net.py"


def split(my_list, split_fraction):
    split_index = int(len(my_list) * split_fraction)
    return my_list[:split_index], my_list[split_index:]


def train_reward(env_name, reward_net_file=default_reward, games=None):

    games_path = 'games'
    
    # use GPU if available, otherwise use CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"

    torch.manual_seed(0)    # for determinism, both on CPU and on GPU
    if torch.cuda.is_available():
        # required for determinism when using GPU
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    ''' read all trajectories and create the training set as the set of trajectories ordered by score '''
    input_shape = 1, 7, 7
    games_path = os.path.join(games_path, env_name)

    if games is None: # load all trajectories
        games_directories = os.path.join(games_path, "*")
        games_info_files = os.path.join(games_directories, "game.json")

        # get list of all trajectories
        list_game_info_files = sorted(glob(games_info_files))
        # random shuffle list of trajectories
        l = len(list_game_info_files)
        perm = torch.randperm(l)
        list_game_info_files = [list_game_info_files[p] for p in perm]
        # train/validation split
        list_train_game_info_files, list_val_game_info_files = split(list_game_info_files, 2/3)

        train_games_info = sorted([json.load(open(file, "r")) for file in list_train_game_info_files], key=lambda x: x["score"])
        val_games_info = sorted([json.load(open(file, "r")) for file in list_val_game_info_files], key=lambda x: x["score"])

        X_train = [torch.Tensor(game_info["trajectory"]).to(device) for game_info in train_games_info]
        X_val = [torch.Tensor(game_info["trajectory"]).to(device) for game_info in val_games_info]

    else: # load specified trajectories
        list_train_game_info_files = [os.path.join(games_path, game, "game.json") for game in games]
        train_games_info = [json.load(open(file, "r")) for file in list_train_game_info_files]
        X_train = [torch.Tensor(game_info["trajectory"]).to(device) for game_info in train_games_info]
        X_val = None
        val_games_info = None

    print("Training trajectories:", list_train_game_info_files)
    print("Validation trajectories:", list_val_game_info_files if X_val is not None else None)

    # X_test = X_val
    module_path, _ = reward_net_file.rsplit(".", 1)
    net_module = importlib.import_module(module_path.replace("/", "."))
    reward_net = net_module.get_net(input_shape).to(device)

    print("summary")
    summary(reward_net, input_shape, device=device)

    # evaluate before training
    #reward_net.evaluate(X_test, [reward_net.quality])

    # training
    reward_net_dir = module_path.rsplit("/", 1)[0] if "/" in module_path else ""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    output_dir = os.path.join(reward_net_dir, env_name, timestamp)
    reward_net.fit(X_train, max_epochs=20, X_val=X_val, output_folder=output_dir, train_games_info=train_games_info, val_games_info=val_games_info, autosave=True, epochs_for_checkpoint=10)

    # evaluate after training
    #reward_net.evaluate(X_test, [reward_net.quality])

    # with torch.no_grad():
    #     for trajectory in X_test:
    #         print("score: " + str(reward_net(trajectory).sum()))

    # # save trained reward net
    # torch.save(reward_net.state_dict(), "reward_net.pth")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a reward net.')
    parser.add_argument("-e", "--env_name", help="gym environment to load", default=default_env)
    parser.add_argument("-r", "--reward", help="reward network to train", default=default_reward)
    args = parser.parse_args()

    train_reward(args.env_name, args.reward)
