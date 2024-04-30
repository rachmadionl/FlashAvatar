import argparse
import os
import sys

project_folder = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(project_folder, 'submodules'))

from face_parser.test import evaluate

def main(args):
    if not os.path.exists(args.output_folder):
        os.mkdir(args.output_folder)

    evaluate(dspth=args.input_folder, respth=args.output_folder, cp=args.pretrained_filepath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, default='./example/dataset/510_s4/imgs')
    parser.add_argument('--output_folder', type=str, default='./example/dataset/510_s4/parsing')
    parser.add_argument('--pretrained_filepath', type=str, default='pretrained/79999_iter.pth')
    args = parser.parse_args()

    main(args)