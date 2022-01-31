
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Benchmarking Visual Geolocalization",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Training parameters
    parser.add_argument("--train_batch_size", type=int, default=4,
                        help="Number of triplets (query, pos, negs) in a batch. Each triplet consists of 12 images")
    parser.add_argument("--infer_batch_size", type=int, default=16,
                        help="Batch size for inference (caching and testing)")
    parser.add_argument("--margin", type=float, default=0.1,
                        help="margin for the triplet loss")
    parser.add_argument("--epochs_num", type=int, default=50,
                        help="Maximum number of epochs to train for")
    parser.add_argument("--patience", type=int, default=3)
    parser.add_argument("--lr", type=float, default=0.00001, help="Learning rate")
    parser.add_argument("--cache_refresh_rate", type=int, default=1000,
                        help="How often to refresh cache, in number of queries")
    parser.add_argument("--queries_per_epoch", type=int, default=5000,
                        help="How many queries to consider for one epoch. Must be multiple of cache_refresh_rate")
    parser.add_argument("--negs_num_per_query", type=int, default=10,
                        help="How many negatives to consider per each query in the loss")
    parser.add_argument("--neg_samples_num", type=int, default=1000,
                        help="How many negatives to use to compute the hardest ones")

    parser.add_argument("--optimizer", type=str, default="adam", choices=["adam","SGD"],
                         help="Which kind of optimizer to use")

    # Other parameters
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--device", type=str, default="cuda", choices=["cuda", "cpu"])
    parser.add_argument("--num_workers", type=int, default=8, help="num_workers for all dataloaders")
    parser.add_argument("--val_positive_dist_threshold", type=int, default=25, help="Val/test threshold in meters")
    parser.add_argument("--train_positives_dist_threshold", type=int, default=10, help="Train threshold in meters")
    parser.add_argument('--recall_values', type=int, default=[1, 5, 10, 20], nargs="+",
                        help="Recalls to be computed, such as R@5.")

    parser.add_argument("--num_clusters", type=int, default=64, help="Number of clusters for the NetVLAD layer")

    # Paths parameters
    parser.add_argument("--datasets_folder", type=str, required=True, help="Path with datasets")
    parser.add_argument("--exp_name", type=str, default="default",
                        help="Folder name of the current run (saved in ./runs/)")
    
    
    
    parser.add_argument("--dataset_name", type=str, default="pitts30k", help="Name of the folder of the dataset to use")
    parser.add_argument("--type", type=str, default='default', help="What type of network would you use; 'GEM' or 'NETVLAD'")
    
    parser.add_argument("--colab_folder", type=str, default=None, help="In what folder you want to save the output of train.py")

    parser.add_argument("--data_aug", type=str, default=None, choices=["CS-HF", "H-RP", "B-GS-R", "GS", "BCSH"], help="Choose the type of data augmentation you want")
    parser.add_argument("--aug_prob", type=float, default=0.5, help="Probability to apply augmentation during training")

    # Images parameters
    parser.add_argument("--img_width", type=int, default=None, help="Width of images used")
    parser.add_argument("--img_height", type=int, default=None, help="Height of images used")
    # Testing
    parser.add_argument("--test_datasets", type=str, default="pitts30k", help="List of test datasets, comma separated")
    parser.add_argument("--model_folder", type=str, default=None, help="Folder of the model used for test")
    
    args = parser.parse_args()
    
    if args.queries_per_epoch % args.cache_refresh_rate != 0:
        raise ValueError("Ensure that queries_per_epoch is divisible by cache_refresh_rate, " +
                         f"because {args.queries_per_epoch} is not divisible by {args.cache_refresh_rate}")
    return args

