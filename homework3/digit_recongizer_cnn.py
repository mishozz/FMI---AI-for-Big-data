import torch.nn as nn

class DigitRecognizerCNN(nn.Module):
    def __init__(self):
        super(DigitRecognizerCNN, self).__init__()
        self.initial_conv_block = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.MaxPool2d(2)
        )
        self.secondary_conv_block = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(64 * 7 * 7, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.initial_conv_block(x)
        x = self.secondary_conv_block(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
