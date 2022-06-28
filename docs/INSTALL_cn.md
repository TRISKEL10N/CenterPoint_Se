## 安装

[中文|[English](INSTALL_en.md)]

根据[det3d](https://github.com/poodarchu/Det3D/tree/56402d4761a5b73acd23080f537599b0888cce07)的原始文档进行修改

### 必要条件

- Linux
- Python 3.6+
- PyTorch 1.1 或更高
- CUDA 10.0 或更高
- CMake 3.13.2 或更高
- [APEX](https://github.com/nvidia/apex)
- [spconv](https://github.com/traveller59/spconv/commit/73427720a539caf9a44ec58abe3af7aa9ddb8e39) 

#### 注释
- 请使用spconv 1.x（具体的版本可能与上文链接不同），2.x版本仍存在一些bug
- 最新的pytorch/spconv/cuda版本速度更快，占用内存更少

我们已经测试了以下版本的操作系统和软件：

- OS: Ubuntu 16.04/18.04
- Python: 3.6.5/3.7.10 
- PyTorch: 1.1/1.9
- spconv: 1.0/1.2.1
- CUDA: 10.0/11.1

### 基础安装 

```bash
# 基础的 python 库
conda create --name centerpoint python=3.6
conda activate centerpoint
conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
git clone https://github.com/tianweiy/CenterPoint.git
cd CenterPoint
pip install -r requirements.txt

# 将下行内容添加到 ~/.bashrc，从而将 CenterPoint 添加到 PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:PATH_TO_CENTERPOINT"
```

### 高级安装 

#### nuScenes dev-kit

```bash
git clone https://github.com/tianweiy/nuscenes-devkit

# 将下行内容添加到 ~/.bashrc，并重新激活 bash （记得修改 PATH_TO_NUSCENES_DEVKIT）
export PYTHONPATH="${PYTHONPATH}:PATH_TO_NUSCENES_DEVKIT/python-sdk"
```

#### Cuda Extensions

```bash
# 设置 cuda 路径（将路径更改为您自己的 cuda 位置）
export PATH=/usr/local/cuda-10.0/bin:$PATH
export CUDA_PATH=/usr/local/cuda-10.0
export CUDA_HOME=/usr/local/cuda-10.0
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
bash setup.sh 
```

#### APEX

```bash
git clone https://github.com/NVIDIA/apex
cd apex
git checkout 5633f6  # 最近的提交未在我们的系统中生成
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

#### spconv
```bash
sudo apt-get install libboost-all-dev
git clone https://github.com/traveller59/spconv.git --recursive
cd spconv && git checkout 7342772
python setup.py bdist_wheel
cd ./dist && pip install *
```

#### 查看[GETTING_START](GETTING_START.md)以准备数据并使用预训练的模型。
