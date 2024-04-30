import argparse
import os
import torch


def main(args):
    model = torch.hub.load("PeterL1n/RobustVideoMatting", "mobilenetv3")
    convert_video = torch.hub.load("PeterL1n/RobustVideoMatting", "converter")

    base_folder = args.base_folder
    input_source = os.path.join(base_folder, 'imgs')
    output_composition = os.path.join(base_folder, 'composition')
    output_alpha = os.path.join(base_folder, 'alpha')
    output_foreground = os.path.join(base_folder, 'foreground')

    convert_video(
        model,
        input_source=input_source,
        output_type='png_sequence',
        output_composition=output_composition,
        output_alpha=output_alpha,
        output_foreground=output_foreground,
        downsample_ratio=None,
        seq_chunk=12,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_folder', type=str, default='./example/dataset/510_s4')
    args = parser.parse_args()

    main(args)