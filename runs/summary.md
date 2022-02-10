| Head    | Optimizer | LR       | Train_pos_dist_th | Val_pos_dist_th | Augmentation | Attention | img_size | R@5_val | R@5_test (Pitts30k)| R@5_test (St.Lucia) | Run     |
| ------- | --------- | -------- | ----------------- | --------------- | ------------ | --------- | -------- | ------- | ------------------ | ------------------- | ------- |
| Default | Adam      | 0.00001  | 10                | 25              | /            | /         | /        | 81.7    | 81.5               | 48.0                | done    |
| GEM     | Adam      | 0.00001  | 10                | 25              | /            | /         | /        | 89.9    | 89.1               | 68.3                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | /            | /         | /        | 96.0    | 93.2               | 71.3                | done    |
| NetVLAD | Adam      | 0.001    | 10                | 25              | /            | /         | /        | 93.1    | 89.6               | 57.7                | done    |
| NetVLAD | Adam      | 0.000001 | 10                | 25              | /            | /         | /        | 95.8    | 93.0               | 70.4                | done    |
| NetVLAD | SGD M=0.9 | 0.00001  | 10                | 25              | /            | /         | /        | 90.2    | 89.8               | 70.7                | done    |
| NetVLAD | SGD M=0.9 | 0.001    | 10                | 25              | /            | /         | /        | 96.1    | 93.1               | 71.4                | done    |
| NetVLAD | SGD M=0.9 | 0.000001 | 10                | 25              | /            | /         | /        | 80.2    | 79.4               | 65.3                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | CS-HF        | /         | /        | 95.3    | 92.4               | 77.5                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | H-RP         | /         | /        | 96.1    | 92.8               | 72.2                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | B-GS-R       | /         | /        | 93.8    | 91.5               | 64.4                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | GS           | /         | /        | 95.5    | 92.7               | 71.0                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | BCSH         | /         | /        | 95.7    | 92.5               | 82.1                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 10              | /            | /         | /        | /       | 88.3               | \                   | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 40              | /            | /         | /        | /       | 94.7               | \                   | done    |
| NetVLAD | Adam      | 0.00001  | 5                 | 25              | /            | /         | /        | 96.4    | 92.9               | 70.8                | done    |
| NetVLAD | Adam      | 0.00001  | 15                | 25              | /            | /         | /        |         |                    |                     | Aless   |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | /            | CBAM      | /        | 95.7    | 93.3               | 70.8                | done    |
| NetVLAD | Adam (SOS)| 0.00001  | 10                | 25              | /            | /         | /        | 93.3    | 91.8               | 71.0                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | /            | /         | 300x200  | 95.2    | 92.6               | 81.5                | done    |
| NetVLAD | Adam      | 0.00001  | 10                | 25              | /            | /         | 800x600  | 95.9    | 92.8               | 66.5                | done    |

