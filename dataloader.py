import os
from csv import reader
from tqdm import tqdm

import cv2
import matplotlib.pyplot as plt

from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from collections import defaultdict


class CustomImageDataset(Dataset):
    def __init__(self, csv_path, transform=None):
        self.csv_path = csv_path
        self.transform = transform
        self.data_dict = defaultdict(lambda: {"point": [], "label": []})
        self.parse_csv_file()

    def __len__(self):
        return len(self.data_dict.keys())

    def __getitem__(self, idx):
        image, label = self.get_item_by_idx(idx)

        if self.transform is not None:
            image = self.transform(image)
        return image, label

    def get_item_by_idx(self, idx):
        img_path = list(self.data_dict.keys())[idx]
        points = self.data_dict[img_path]["point"]

        label = []
        [label.extend(point) for point in points]

        image = cv2.imread(img_path)


        return image, label


    def parse_csv_file(self):
        
        self.csv_path = os.path.normpath(self.csv_path)
        basepath = os.path.dirname(self.csv_path)
        
        with open(self.csv_path, "r", encoding="UTF8", errors="ignore") as f:
            rdr = reader(f)
            for line in rdr:
                if line[3] == "":
                    self.data_dict[os.path.normpath(os.path.join(basepath, line[0]))]
                else:
                    self.data_dict[os.path.normpath(os.path.join(basepath, line[0]))]["point"].append([int(line[1]), int(line[2])])
                    self.data_dict[os.path.normpath(os.path.join(basepath, line[0]))]["label"].append(line[3])

        self.data_dict = dict(self.data_dict)
                
if __name__ == "__main__":

    tensor_transform = transforms.ToTensor()
 
    dataset = CustomImageDataset(csv_path = "../../data/raw_label.csv",
                                transform = None)
    

    loader = DataLoader(dataset = dataset,
                        batch_size = 1,
                        shuffle = True)


    for image, label in tqdm(loader):
        print(label)
        plt.imshow(image[0,...])
        plt.show()

        
            
