import torch

model = torch.hub.load("PeterL1n/RobustVideoMatting", "mobilenetv3")

convert_video = torch.hub.load("PeterL1n/RobustVideoMatting", "converter")

convert_video(
    model,
    input_source='/home/lazuardi/FlashAvatar/example/dataset/510_s4/color_cropped',
    output_type='png_sequence',
    output_composition='/home/lazuardi/FlashAvatar/example/dataset/510_s4/composition',
    output_alpha='/home/lazuardi/FlashAvatar/example/dataset/510_s4/alpha',
    output_foreground='/home/lazuardi/FlashAvatar/example/dataset/510_s4/foreground',
    downsample_ratio=None,
    seq_chunk=12,
)