import argparse

arg_lists = []
parser = argparse.ArgumentParser()

def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg

# Dataset
data_arg = add_argument_group('Dataset')
data_arg.add_argument('--dataset', type=str, default='std12k')
data_arg.add_argument('--data_root', type=str, default='/std12k_points')

# Model
model_arg = add_argument_group('Model')
model_choices = ["SAIN"]
model_arg.add_argument('--model', choices=model_choices, type=str, default="SAIN")
model_arg.add_argument('--nbr_frame' , type=int , default=2)
model_arg.add_argument('--joinType' , choices=["concat" , "add" , "none"], default="concat")

# Training / test parameters
learn_arg = add_argument_group('Learning')
learn_arg.add_argument('--loss', type=str, default='0.7*L1+0.3*LPIPS')
learn_arg.add_argument('--lr', type=float, default=2e-4)
learn_arg.add_argument('--beta1', type=float, default=0.9)
learn_arg.add_argument('--beta2', type=float, default=0.999)
learn_arg.add_argument('--batch_size', type=int, default=4)
learn_arg.add_argument('--test_batch_size', type=int, default=4)
learn_arg.add_argument('--start_epoch', type=int, default=0)
learn_arg.add_argument('--max_epoch', type=int, default=50)
learn_arg.add_argument('--resume', action='store_true')
learn_arg.add_argument('--resume_exp', type=str, default=None)
learn_arg.add_argument('--checkpoint_dir', type=str ,default="ckp")
learn_arg.add_argument("--load_from"  ,type=str , default='ckp/checkpoints/model_best.pth')
learn_arg.add_argument("--pretrained" , type=str, help="Load from a pretrained model.")

parser.add_argument('--phase', default='train', type=str)
parser.add_argument('--crop_size', default=192, type=int)
parser.add_argument('--result_dir', default='result', type=str)

# Misc
misc_arg = add_argument_group('Misc')
misc_arg.add_argument('--exp_name', type=str, default='exp')
misc_arg.add_argument('--log_iter', type=int, default=100)
misc_arg.add_argument('--num_gpu', type=int, default=1)
misc_arg.add_argument('--random_seed', type=int, default=103)
misc_arg.add_argument('--num_workers', type=int, default=1)
misc_arg.add_argument('--val_freq', type=int, default=1)

def get_args():
    """Parses all of the arguments above
    """
    args, unparsed = parser.parse_known_args()
    if args.num_gpu > 0:
        setattr(args, 'cuda', True)
    else:
        setattr(args, 'cuda', False)
    if len(unparsed) > 1:
        print("Unparsed args: {}".format(unparsed))
    return args, unparsed
