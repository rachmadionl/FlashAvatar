# FlashAvatar
**[Paper](https://arxiv.org/abs/2312.02214)|[Project Page](https://ustc3dv.github.io/FlashAvatar/)**

![teaser](exhibition/teaser.png)
Given a monocular video sequence, our proposed FlashAvatar can reconstruct a high-fidelity digital avatar in minutes which can be animated and rendered over 300FPS at the resolution of 512×512 with an Nvidia RTX 3090.

## Setup

0. Git Clone via:
    ```bash
    git clone https://github.com/rachmadionl/FlashAvatar.git --recursive
    ```

1. Create the environment:

    ```bash
    conda env create --file environment.yml
    ```

2. Ensure that the correct `nvcc.exe` is taken from the conda environment:  
   Linux:
    ```bash
    conda activate FlashAvatar
    conda env config vars set CUDA_HOME=$CONDA_PREFIX
    conda deactivate
    conda activate FlashAvatar
    ```
   Windows: 
   ```bash
    conda activate FlashAvatar
    conda env config vars set CUDA_HOME=$Env:CONDA_PREFIX
    conda deactivate
    conda activate FlashAvatar
    ```
3. Check whether the correct `nvcc` can be found on the path via:
    ```bash
    nvcc --version
    ```
    which should say something like `release 11.8`.

4. Install submodules:
    ```bash
    pip install submodules/diff-gaussian-rasterization
    pip install submodules/simple-knn
    ```

5. Install PyTorch3D:
    ```bash
    conda install -c fvcore -c iopath -c conda-forge fvcore iopath
    conda install -c bottler nvidiacub
    conda install pytorch3d -c pytorch3d
    ```

6. Copy the following files from Metrical Tracker (Assuming you have set up Metrical Tracker on your environment):
    ```
    data/FLAME2020/FLAME_masks.pkl
    data/FLAME2020/generic_model.pkl
    ```
    Into this folder: `flame`

7. DONE! One Note: FlashAvatar is originally ran on RTX3090 (24 GB VRAM), while ours is RTX3080 (10 GB VRAM). With that in mind, an adjustment is needed to be made. Originally, [`test_num`](https://github.com/rachmadionl/FlashAvatar/blob/main/scene/__init__.py#L34) is set to 500 and [`max_train_num`](https://github.com/rachmadionl/FlashAvatar/blob/main/scene/__init__.py#L37) is set to 10000. Due to memory limitation, I changed both value to 100. With this setting, only ~2.6 GPU VRAM is used when training is done on provided example data. So, feel free to increase the parameters.

## Data Convention
The data is organized in the following form：
```
dataset
├── <id1_name>
    ├── alpha # raw alpha prediction
    ├── imgs # extracted video frames
    ├── parsing # semantic segmentation
├── <id2_name>
...
metrical-tracker
├── output
    ├── <id1_name>
        ├── checkpoint
    ├── <id2_name>
...
```
## Running
- **Evaluating pre-trained model**
```shell
python test.py --idname <id_name> --checkpoint dataset/<id_name>/log/ckpt/chkpnt.pth
```
-  **Training on your own data** 
```shell
python train.py --idname <id_name>
```
Download the [example](https://drive.google.com/file/d/1_WLvlmHD73jOAO178N7eX5UQqlrL2ghD/view?usp=drive_link) with pre-processed data and pre-trained model for a try!

## Citation
```
@inproceedings{xiang2024flashavatar,
      author    = {Jun Xiang and Xuan Gao and Yudong Guo and Juyong Zhang},
      title     = {FlashAvatar: High-fidelity Head Avatar with Efficient Gaussian Embedding},
      booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
      year      = {2024},
  }
```
