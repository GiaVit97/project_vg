import math
import torch

def sos_loss(anchor, positives, negatives):

    nq = anchor.size(0) # number of tuples

    dist_an = torch.sum(torch.pow(anchor - negatives, 2), dim=0)
    dist_pn = torch.sum(torch.pow(positives - negatives, 2), dim=0)

    return torch.sum(torch.pow(dist_an - dist_pn, 2)) ** 0.5 / nq
