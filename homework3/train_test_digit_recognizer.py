import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from digit_recongizer_cnn import DigitRecognizerCNN

MODEL_PATH = 'mnist_cnn_model.pth'
LEARNING_RATE = 0.001
BATCH_SIZE = 100
EPOCHS = 7
VALIDATION_SPLIT = 0.1


def load_full_train_dataset(transform):
    return torchvision.datasets.MNIST(
        root='./data', 
        train=True, 
        transform=transform,
        download=True
    )

def load_test_dataset(transform):
    return torchvision.datasets.MNIST(
        root='./data', 
        train=False, 
        transform=transform,
        download=True
    )

def train_model(train_loader, val_loader):
    model = DigitRecognizerCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=2)
    
    best_val_loss = float('inf')
    
    print(f"Training on {device}")
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for batch_idx, (image_data, labels) in enumerate(train_loader):
            image_data, labels = image_data.to(device), labels.to(device)
            
            optimizer.zero_grad()
            output = model(image_data)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            _, predicted = output.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            
            if batch_idx % 100 == 99:
                print(f'Epoch: {epoch+1}/{EPOCHS}, Batch: {batch_idx+1}/{len(train_loader)}, '
                      f'Loss: {running_loss/100:.3f}, Acc: {100.*correct/total:.2f}%')
                running_loss = 0.0
                correct = 0
                total = 0
        
        # Validation phase
        model.eval()
        val_loss = 0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for image_data, labels in val_loader:
                image_data, labels = image_data.to(device), labels.to(device)
                output = model(image_data)
                val_loss += criterion(output, labels).item()
                _, predicted = output.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()
        
        val_loss /= len(val_loader)
        accuracy = 100. * correct / total
        
        print(f'Validation - Loss: {val_loss:.4f}, Accuracy: {accuracy:.2f}%')
        
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), MODEL_PATH)
            print('Model saved (best validation loss)')
        
        scheduler.step(val_loss)

def test_model(test_loader):
    model = DigitRecognizerCNN().to(device)
    model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
    model.eval()
    
    correct = 0
    total = 0
    
    with torch.no_grad():
        for image_data, labels in test_loader:
            image_data, labels = image_data.to(device), labels.to(device)
            output = model(image_data)
            _, predicted = output.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
    
    accuracy = 100. * correct / total
    print(f'\nTest Accuracy: {accuracy:.2f}%')

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    full_train_dataset = load_full_train_dataset(transform)
    test_dataset = load_test_dataset(transform)
    
    train_size = int((1 - VALIDATION_SPLIT) * len(full_train_dataset))
    val_size = len(full_train_dataset) - train_size
    
    train_dataset, val_dataset = torch.utils.data.random_split(
        full_train_dataset, [train_size, val_size]
    )
    
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    print("Starting training...")
    train_model(train_loader=train_loader, val_loader=val_loader)
    print("\nEvaluating model...")
    test_model(test_loader=test_loader)
