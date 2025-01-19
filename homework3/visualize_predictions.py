import torch
import torchvision
import matplotlib.pyplot as plt
from digit_recongizer_cnn import DigitRecognizerCNN

MODEL_PATH = 'mnist_cnn_model.pth'

def load_model():
    model = DigitRecognizerCNN()
    model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
    model.eval()

    return model

def load_data():
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize((0.1307,), (0.3081,))
    ])

    return torchvision.datasets.MNIST(
        root='./data', 
        train=False, 
        transform=transform,
        download=True
    )

def visualize_predictions(model, test_dataset):
    plt.figure(figsize=(20, 4))
    print("\nPredictions for the first 10 test images:")
    print("----------------------------------------")

    for i in range(10):
        image, expected_label = test_dataset[i]

        with torch.no_grad():
            output = model(image.unsqueeze(0))
            probabilities = torch.nn.functional.softmax(output, dim=1)
            predicted_label = torch.argmax(output).item()
            confidence = probabilities[0][predicted_label].item() * 100

        plt.subplot(1, 10, i + 1)
        plt.imshow(image.squeeze(), cmap='gray')
        color = 'green' if predicted_label == expected_label else 'red'
        plt.title(f'Expected: {expected_label}\nPred: {predicted_label}\nConfidence {confidence:.2f}%', color=color)
        plt.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    model = load_model()
    test_dataset = load_data()
    visualize_predictions(model, test_dataset)
