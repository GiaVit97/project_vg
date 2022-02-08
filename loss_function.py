import math
import torch

def sos_loss(anchor, positives, negatives):
    # x is D x N
    #dim = x.size(0) # D
    nq = anchor.size(0) # number of tuples
    #S = x.size(1) // nq # number of images per tuple including query: 1+1+n

    #xa = x[:, label.data==-1].permute(1,0).repeat(1,S-2).view((S-2)*nq,dim).permute(1,0) # D * (B * num_neg)
    #xp = x[:, label.data==1].permute(1,0).repeat(1,S-2).view((S-2)*nq,dim).permute(1,0)
    #xn = x[:, label.data==0]

    dist_an = torch.sum(torch.pow(anchor - negatives, 2), dim=0)
    dist_pn = torch.sum(torch.pow(positives - negatives, 2), dim=0)

    return torch.sum(torch.pow(dist_an - dist_pn, 2)) ** 0.5 / nq