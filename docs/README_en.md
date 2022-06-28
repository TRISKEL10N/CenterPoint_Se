# **CenterPoint-Se**
## **Contents**
[[中文](../README.md)|English]

  - [**Introduction**](#introduction)
  - [**Experomental Results**](#experomental-results)
  - [**How To Use**](#how-to-use)

## **Introduction**

Our work proposes a 3D point cloud object detection algorithm assisted by semantic information. Firstly, based on the existing semantic segmentation algorithm PMF, we use multimodal data (point cloud and multi-view images) to achieve the task scene's semantic recognition, and reproject the semantic information back to the original point cloud; Then, to improve the CenterPoint, the data loading and preprocessing part of the algorithm is modified to the mode of processing point cloud with semantic features, to use the pre-obtained semantic data and point cloud data to achieve a higher level of the object detection performance.

![CenterPoint-Se Architecture](../Figure/CenterPoint_Se(en).png "CenterPoint-Se Architecture")

## **Experomental Results**

To verify the enhancement of semantic information on object detection tasks, we evaluated the original CenterPoint and the improved CenterPoint-Se using semantic information on the Nuscenes dataset. The experimental results are shown in Table 1:

![Comparison of algorithms with different backbone and semantic information](../Figure/Table1(en).png "Comparison of algorithms with different backbone and semantic information")

To further analyze the reasons for performance improvement, we evaluated the performance breakdown according to the category of detected object. The experimental results are shown in Table 2:

![Performance breakdown in different object categories](../Figure/Table2(en).png "Performance breakdown in different object categories")

## **How To Use**

### **Installion**

Please reffer to [INSTALL](INSTALL_en.md) to set up libraries needed for dietributed trainging and sparse convolution.

### **Model Evaluation and Training**

Please refer to [GETTING_START](GETTING_START.md) to prepare the data. Then follow the instruction there to reproduce our detection and tracking results. All detection configurations are included in [configs](../configs). (Now we only improve the original CenterPoint algorithm on the NuScenes dataset)
