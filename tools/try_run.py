#建立“sample_data_token”到“token”的对应字典
#cunstruct the dictionary from "sample_data_token" to "token"
def get_token():
    import os
    try:
        from nuscenes import NuScenes
    except:
        print("nuScenes devkit not Found!")

    nusc = NuScenes(version="v1.0-trainval", dataroot='../data/nuScenes', verbose=True)
     
    semantic_train_path = '../semantic_pred/Train'
    semantic_eval_path = '../semantic_pred/Eval'
 
    semantic_train_files = os.listdir(semantic_train_path)
    semantic_eval_files = os.listdir(semantic_eval_path)
    semantic_files = semantic_train_files + semantic_eval_files

    print('length1: ' + str(len(semantic_files)))

    lidarpath2setoken = dict()

    #senamtic_files 是一个 list
    for semantic_file in semantic_files:
        semantic_token = str(semantic_file[0:32])
        for i in range(len(nusc.sample)):
            if semantic_token == nusc.sample[i]['data']['LIDAR_TOP']:
                #token
                lidar_top_data = nusc.get('sample_data', nusc.sample[i]['data']['LIDAR_TOP'])
                filename = lidar_top_data['filename']
                if semantic_file in semantic_train_files:
                    lidarpath2setoken.update({'data/nuScenes/' + str(filename):'Train/' + str(semantic_token)})
                elif semantic_file in semantic_eval_files:
                    lidarpath2setoken.update({'data/nuScenes/' + str(filename):'Eval/' + str(semantic_token)})
                break
 
    print('length2: ' + str(len(lidarpath2setoken.keys())))

    with open('../lidarpath2setoken.txt', 'w') as infos:
        infos.write(str(lidarpath2setoken))
    print('Write Done!')
 

#训练过程试运行
#try run of the training process
def try_run():
    from det3d.torchie import Config
    from det3d.datasets.builder import build_dataset
    from det3d.models.builder import build_detector
    from det3d.datasets.loader.build_loader import build_dataloader
    from det3d.torchie.apis.train import example_to_device
    import torch

    cfg = Config.fromfile("../configs/nusc/pp/nusc_centerpoint_pp_02voxel_two_pfn_10sweep_circular_nms.py")
    print('creating dataset...')
    dataset = build_dataset(cfg.data.train)
    
    print('creating dataloader...')
    loader = build_dataloader(dataset, cfg.data.samples_per_gpu, cfg.data.workers_per_gpu, dist=False)
    
    print('creating model...')
    model = build_detector(cfg.model, train_cfg=cfg.train_cfg, test_cfg=cfg.test_cfg)
    # model = model.cuda()
    # device = torch.device(0)
    print('running..')
    for _,data_batch in enumerate(loader):
        #data_batch = example_to_device(data_batch,device)
        tmp = model(data_batch)
        with open('../tmp.txt','a') as f:
            f.write(str(data_batch))
        #exit(0)
    print('run done..')


if __name__ == "__main__":
    get_token()
    #try_run()
