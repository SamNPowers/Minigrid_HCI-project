import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from utils import conv_output_size


class RewardNet(nn.Module):
    """ this is a simple neural network """
    
    @staticmethod
    def loss(scores):
        n = len(scores)
        predictions = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                predictions.append(nn.CrossEntropyLoss()(torch.stack((scores[i], scores[j])).reshape(1, 2), torch.tensor([1])))  # T-REX loss

        l = sum([p for p in predictions])
        return l

    def __init__(self, input_shape):
        super(RewardNet, self).__init__()
        self.input_shape = input_shape

        self.conv = nn.Conv2d(in_channels=1, out_channels=15, kernel_size=2)
        o = conv_output_size(input_shape[1], 2, 0, 1)
        self.fc = nn.Linear(15 * o * o, 1)
        self.optimizer = optim.Adam(self.parameters(), lr=1e-5)
        # TODO regolarizzare

    def forward(self, x):
        x = x.view(-1, *self.input_shape)
        batch_size = len(x)
        return self.fc(F.relu(self.conv(x)).view(batch_size, -1))

    def fit(self, X_train, max_epochs=1000):
        # training
        for epoch in range(max_epochs):
            self.optimizer.zero_grad()
            scores = torch.zeros(len(X_train))
            for t, trajectory in enumerate(X_train):
                trajectory_score = self(trajectory).sum()
                scores[t] = trajectory_score

            l = RewardNet.loss(scores)
            l.backward()
            # TODO capire per quale motivo il gradiente e la loss a un certo punto esplodono

            self.optimizer.step()

            print("epoch:", epoch, " loss:", l.item())

    def evaluate(self, X):
        # net evaluation
        training = self.training
        self.eval()  # same as: self.training = False
        with torch.no_grad():
            test_scores = []
            for t, trajectory in enumerate(X):
                trajectory_score = self(trajectory).sum()
                test_scores.append(trajectory_score)

            quality = 0

            for i in range(len(test_scores)):
                for j in range(len(test_scores)):
                    if i == j:
                        continue
                    print("i: " + str(i) + ", j: " + str(j) + ", P(J(τj) > J(τi)): " + str(test_scores[j] / (test_scores[i] + test_scores[j])))

                    if j > i and test_scores[j] > test_scores[i]:
                            quality += 1

            n = len(test_scores)
            quality /= n * (n-1) / 2
            print("quality:", quality)
            # quality is the percentage of correctly discriminated pairs

        self.training = training  # restore previous training state
