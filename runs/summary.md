| Head    | Optimizer | LR       | Test Dataset | Train_pos_dist_th | Val_pos_dist_th | Augmentation | img_size | R@5_val | R@5_test | Run  |
| ------- | --------- | -------- | ------------ | ----------------- | --------------- | ------------ | -------- | ------- | -------- | ---- |
| Default | Adam      | 0.00001  | Pitts30k     | 10                | 25              | /            | /        | 81.7    | 81.5     | done |
| Default | Adam      | 0.00001  | St_lucia     | 10                | 25              | /            | /        | 81.7    | 48.0     | done |
| GEM     | Adam      | 0.00001  | Pitts30k     | 10                | 25              | /            | /        | 89.9    | 89.1     | done |
| GEM     | Adam      | 0.00001  | St_lucia     | 10                | 25              | /            | /        | 89.9    | 68.3     | done |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | /            | /        | 96.0    | 93.2     | done |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | /            | /        | 96.0    | 71.3     | done |
| NetVLAD | Adam      | 0.001    | Pitts30k     | 10                | 25              | /            | /        |         |          |      |
| NetVLAD | Adam      | 0.000001 | Pitts30k     | 10                | 25              | /            | /        |         |          |      |
| NetVLAD | SGD M=0.9 | 0.00001  | Pitts30k     | 10                | 25              | /            | /        |         |          |      |
| NetVLAD | SGD M=0.9 | 0.001    | Pitts30k     | 10                | 25              | /            | /        | 96.1    | 93.1     | done |
| NetVLAD | SGD M=0.9 | 0.001    | St_lucia     | 10                | 25              | /            | /        | 96.1    | 71.4     | done |
| NetVLAD | SGD M=0.9 | 0.000001 | Pitts30k     | 10                | 25              | /            | /        |         |          |      |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | CS-HF        | /        | 95.3    | 92.4     | done |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | CS-HF        | /        | 95.3    | 77.5     | done |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | H-RP         | /        | 96.1    | 92.8     | done |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | H-RP         | /        | 96.1    | 72.2     | done |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | B-GS-R       | /        | 93.8    | 91.5     | done |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | B-GS-R       | /        | 93.8    | 64.4     | done |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | GS           | /        |         |          |      |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | GS           | /        |         |          |      |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 25              | BCSH         | /        | 95.7    | 92.5     |      |
| NetVLAD | Adam      | 0.00001  | St_lucia     | 10                | 25              | BCSH         | /        | 95.7    | 82.1     |      |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 10              | /            | /        | /       | 88.3     | done |
| NetVLAD | Adam      | 0.00001  | Pitts30k     | 10                | 40              | /            | /        | /       | 94.7     | done |
