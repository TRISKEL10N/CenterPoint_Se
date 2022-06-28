## Getting Started with CenterPoint on nuScenes

[中文|[English](NUSC_en.md)]

根据[det3d](https://github.com/poodarchu/Det3D/tree/56402d4761a5b73acd23080f537599b0888cce07)的原始文档进行修改

### 数据准备

#### 下载数据并按如下方式组织

```
# For nuScenes Dataset         
└── NUSCENES_DATASET_ROOT
       ├── samples       <-- key frames
       ├── sweeps        <-- frames without annotation
       ├── maps          <-- unused
       ├── v1.0-trainval <-- metadata
```

创建指向数据集root的软链接
```bash
mkdir data && cd data
ln -s DATA_ROOT 
mv DATA_ROOT nuScenes # 重命名为 nuScenes
```
记得将DATA_ROOT改为您系统中的实际路径 


#### 数据生成

数据生成需要在GPU环境下进行

```
# nuScenes
python tools/create_data.py nuscenes_data_prep --root_path=NUSCENES_TRAINVAL_DATASET_ROOT --version="v1.0-trainval" --nsweeps=10

# 建立“sample_data_token”到“token”的对应字典
python tools/try_run.py
```

最后，数据和信息文件应按如下方式组织

```
# For nuScenes Dataset 
└── CenterPoint
       └── data    
              └── nuScenes 
                     ├── samples       <-- key frames
                     ├── sweeps        <-- frames without annotation
                     ├── maps          <-- unused
                     |── v1.0-trainval <-- metadata and annotations
                     |── infos_train_10sweeps_withvelo_filter_True.pkl <-- train annotations
                     |── infos_val_10sweeps_withvelo_filter_True.pkl <-- val annotations
                     |── dbinfos_train_10sweeps_withvelo.pkl <-- GT database info files
                     |── gt_database_10sweeps_withvelo <-- GT database 
```

### 在命令行中训练和评估模型

**现在，我们只支持使用GPU进行培训和评估，不支持仅CPU模式。**

使用以下命令调用4个GPU进行分布式训练。模型和训练日志将保存在```work_dirs/CONFIG_NAME```文件夹中。

```bash
python -m torch.distributed.launch --nproc_per_node=4 ./tools/train.py CONFIG_PATH
```

使用4个GPU的分布式测试

```bash
python -m torch.distributed.launch --nproc_per_node=4 ./tools/dist_test.py CONFIG_PATH --work_dir work_dirs/CONFIG_NAME --checkpoint work_dirs/CONFIG_NAME/latest.pth 
```

使用单个GPU进行测试，并查看推断时间

```bash
python ./tools/dist_test.py CONFIG_PATH --work_dir work_dirs/CONFIG_NAME --checkpoint work_dirs/CONFIG_NAME/latest.pth --speed_test 
```

与训练的模型和配置可以查看[MODEL ZOO](../configs/nusc/README.md)。

### 目标跟踪

你可以在[MODEL ZOO](../configs/nusc/README.md)中找到检测文件。下载检测文件之后，您只需运行

```bash 
# val set 
python tools/nusc_tracking/pub_test.py --work_dir WORK_DIR_PATH  --checkpoint DETECTION_PATH  

# test set 
python tools/nusc_tracking/pub_test.py --work_dir WORK_DIR_PATH  --checkpoint DETECTION_PATH  --version v1.0-test  --root data/nuScenes/v1.0-test    
```

### 测试集

将数据集组织如下

```
# For nuScenes Dataset 
└── CenterPoint
       └── data    
              └── nuScenes 
                     ├── samples       <-- key frames
                     ├── sweeps        <-- frames without annotation
                     ├── maps          <-- unused
                     |── v1.0-trainval <-- metadata and annotations
                     |── infos_train_10sweeps_withvelo_filter_True.pkl <-- train annotations
                     |── infos_val_10sweeps_withvelo_filter_True.pkl <-- val annotations
                     |── dbinfos_train_10sweeps_withvelo.pkl <-- GT database info files
                     |── gt_database_10sweeps_withvelo <-- GT database 
                     └── v1.0-test <-- main test folder 
                            ├── samples       <-- key frames
                            ├── sweeps        <-- frames without annotation
                            ├── maps          <-- unused
                            |── v1.0-test <-- metadata and annotations
                            |── infos_test_10sweeps_withvelo.pkl <-- test info
```

在[此处](https://drive.google.com/drive/folders/1uU_wXuNikmRorf_rPBbM0UTrW54ztvMs?usp=sharing)下载```centerpoint_voxel_1440_dcn_flip```，将其保存到```work_dirs/nusc_0075_dcn_flip_track```轨迹中，然后在主文件夹中运行如下命令以获得检测预测 

```bash
python tools/dist_test.py configs/nusc/voxelnet/nusc_centerpoint_voxelnet_0075voxel_dcn_flip.py --work_dir work_dirs/nusc_centerpoint_voxelnet_dcn_0075voxel_flip_testset  --checkpoint work_dirs/nusc_0075_dcn_flip_track/voxelnet_converted.pth  --testset --speed_test 
```