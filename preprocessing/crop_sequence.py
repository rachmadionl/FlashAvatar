import argparse
import os

import cv2


def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2-50:mid_x+cw2-50]
	return crop_img


def main(args):
    if not os.path.exists(args.output_folder):
        os.mkdir(args.output_folder)

    img_files = sorted(os.listdir(args.input_folder))
    for img_file in img_files:
        filename = os.path.join(args.input_folder, img_file)
        image = cv2.imread(filename)
        cropped_img = center_crop(image, (args.img_size, args.img_size))
        cropped_filename = os.path.join(args.output_folder, img_file)
        cv2.imwrite(cropped_filename, cropped_img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, default='./example/dataset/510_s4/color')
    parser.add_argument('--output_folder', type=str, default='./example/dataset/510_s4/imgs')
    parser.add_argument('--img_size', type=int, default=512)
    args = parser.parse_args()

    main(args)