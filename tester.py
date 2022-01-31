import test
import parser

args = parser.parse_arguments()
best_model_state_dict = torch.load(join(args.model_folder, "best_model.pth"))["model_state_dict"]
model.load_state_dict(best_model_state_dict)

# Test on different dataset
for test_dataset in args.test_datasets.slpit(","):
    test_ds = datasets_ws.BaseDataset(args, args.datasets_folder, test_dataset, "test")
    logging.info(f"Test set: {test_ds}")
    recalls, recalls_str = test.test(args, test_ds, model)
    logging.info(f"Recalls on {test_ds}: {recalls_str}")