import argparse
import warnings

import torch

import send_msg

from trainer import SFTTrainer
from utils import set_random_seeds

warnings.filterwarnings("ignore")


def parse_args():
    parser = argparse.ArgumentParser(description="MiniMind Full SFT")
    parser.add_argument("--out_dir", type=str, default="out")
    parser.add_argument("--temperature", default=0.85, type=float)
    parser.add_argument("--top_p", default=0.85, type=float)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--learning_rate", type=float, default=5e-5)
    parser.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--dtype", type=str, default="bfloat16")
    parser.add_argument("--use_wandb", action="store_true")
    parser.add_argument("--wandb_project", type=str, default="MiniMind-Full-SFT")
    parser.add_argument("--num_workers", type=int, default=1)
    parser.add_argument("--ddp", action="store_true")
    parser.add_argument("--accumulation_steps", type=int, default=1)
    parser.add_argument("--grad_clip", type=float, default=1.0)
    parser.add_argument("--warmup_iters", type=int, default=0)
    parser.add_argument("--log_interval", type=int, default=100)
    parser.add_argument("--save_interval", type=int, default=100)
    parser.add_argument("--local_rank", type=int, default=-1)
    parser.add_argument("--dim", default=512, type=int)
    parser.add_argument("--n_layers", default=8, type=int)
    parser.add_argument("--max_seq_len", default=512, type=int)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--data_path", type=str, default="./data/sft.jsonl")

    args = parser.parse_args()
    args.wandb_run_name = (
        f"MiniMind-Full-SFT-Epoch-{args.epochs}-BatchSize-{args.batch_size}-LearningRate-{args.learning_rate}"
    )

    return args


def main():
    set_random_seeds()
    args = parse_args()
    trainer = SFTTrainer(args)
    trainer.run()
    trainer.eval()
    send_msg.send_msg("SFT训练完成！")


if __name__ == "__main__":
    main()
