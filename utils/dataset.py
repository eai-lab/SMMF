import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR100

def get_dataset(args):
    train_ds = CIFAR100(root='./data', train=True, download=True, transform=transforms.Compose([
        transforms.Resize(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize((0.5071, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762)),  
    ]))
    eval_ds = CIFAR100(root='./data', train=False, download=True, transform=transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.5071, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762)),
    ]))
    
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        num_workers=8,
        persistent_workers=True,
        pin_memory=True,
        shuffle=True,
    )
    eval_ds = DataLoader(
        eval_ds,
        batch_size=args.batch_size,
        num_workers=8,
        persistent_workers=True,
        pin_memory=True,
        shuffle=False,
    )
    return train_loader, eval_ds
