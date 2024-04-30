import os
import sys
sys.path.append('/home/lazuardi/FlashAvatar/submodules')

from face_parser.test import evaluate

output_folder = './example/dataset/Obama/parsing_new'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

evaluate(respth=output_folder, dspth='/home/lazuardi/FlashAvatar/example/dataset/Obama/imgs', cp='pretrained/79999_iter.pth')