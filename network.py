
import torch
import logging
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from netvlad import NetVLAD
from gem import GeM
from cbam import CBAM


class GeoLocalizationNet(nn.Module):
    """The model is composed of a backbone and an aggregation layer.
    The backbone is a (cropped) ResNet-18, and the aggregation is a L2
    normalization followed by max pooling.
    """
    def __init__(self, args):
        super().__init__()
        self.backbone = get_backbone(args)
        self.attention = None

        if args.att == 'CBAM':
            self.attention = CBAM(64)
        
        if args.type == 'NETVLAD':
            #NetVLAD type
            logging.debug("Using NetVlad network")
            self.aggregation = nn.Sequential(L2Norm(), NetVLAD(dim = 256, num_clusters=args.num_clusters))
        elif args.type == 'GEM':
            #GeM type
            logging.debug("Using GeM network")
            self.aggregation = nn.Sequential(L2Norm(), 
                                                GeM(p = 3), 
                                                Flatten())
        else:
            # Average pooling
            self.aggregation = nn.Sequential(L2Norm(),
                                         torch.nn.AdaptiveAvgPool2d(1),
                                         Flatten())
        
    def forward(self, x):
        x = self.backbone(x)
        if self.attention is not None:
            x = self.attention(x)
        x = self.aggregation(x)
        return x


def get_backbone(args):
    backbone = torchvision.models.resnet18(pretrained=True)
    for name, child in backbone.named_children():
        if name == "layer3":
            break
        for params in child.parameters():
            params.requires_grad = False
    logging.debug("Train only conv4 of the ResNet-18 (remove conv5), freeze the previous ones")
    layers = list(backbone.children())[:-3]
    backbone = torch.nn.Sequential(*layers)
    if args.type == 'NETVLAD':
        args.features_dim = args.num_clusters * 256 # num of NetVLAD clusters * dim  -> as input NetVLAD wants KxD
    else:
        args.features_dim = 256  # Number of channels in conv4
    return backbone


class Flatten(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x):
        assert x.shape[2] == x.shape[3] == 1
        return x[:,:,0,0]


class L2Norm(nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
    def forward(self, x):
        return F.normalize(x, p=2, dim=self.dim)