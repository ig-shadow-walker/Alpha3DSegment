### ☯️ **Hunyuan3D Part**

Available on [![Hunyuan3D-Studio](https://img.shields.io/badge/Hunyuan3D-Studio-yellow)](https://3d.hunyuan.tencent.com/studio) [![Hunyuan3D](https://img.shields.io/badge/Hunyuan-3D-blue)](https://3d.hunyuan.tencent.com)  


[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/vSveLI1AoDw/0.jpg)](https://www.youtube.com/watch?v=vSveLI1AoDw)

---

### **Getting started (P3-SAM)**

To run **P3-SAM** (3D part segmentation) locally:

1. **Environment**  
   Use Python 3.10 and PyTorch 2.4+ with CUDA 12.1 (or compatible). Create and activate a conda environment (recommended):
   ```bash
   conda create -n alpha3d python=3.10 -y
   conda activate alpha3d
   ```

2. **Install Sonata**  
   Install the [Sonata](https://github.com/facebookresearch/sonata) package and its dependencies as per its repo.

3. **Install P3-SAM dependencies**  
   ```bash
   pip install viser fpsample trimesh numba gradio safetensors huggingface_hub scikit-learn tqdm
   ```

4. **Build the Chamfer3D extension** (needs a CUDA GPU and `nvcc` in `PATH`):  
   ```bash
   cd P3-SAM/utils/chamfer3D
   python setup.py install
   cd ../../..
   ```

5. **Run the Gradio demo** (weights download from HuggingFace on first run):  
   ```bash
   cd P3-SAM/demo
   python gradio_demo.py
   ```  
   Open the URL printed (e.g. `http://0.0.0.0:8080`) in your browser.

   **Other ways to run:**  
   - Auto-segment from CLI:  
     `python auto_mask.py --mesh_path assets/1.glb --output_path results/1`  
   - Interactive point-prompt app:  
     `python app.py --data_dir assets`  
   - Optionally download `p3sam.safetensors` from [HuggingFace](https://huggingface.co/tencent/Hunyuan3D-Part) into `P3-SAM/weights/` and use `--ckpt_path ../weights/p3sam.safetensors` with the scripts above.

**X-Part** (shape decomposition) uses the same env and Sonata; pre-trained weights are not yet released (see [XPart/README.md](XPart/README.md)).

---

Our 3D part generation pipeline contains two key components, P3-SAM and X-Part. The holistic mesh is fed to part detection module P3-SAM to obtain the semantic features, part segmentations and part bounding boxes. Then X-Part generate the complete parts.  
<img src="P3-SAM/images/HYpart-fullpip.jpg" alt="drawing" width="800"/>

###  P3-SAM： Native 3D part Segmentation.   



- Paper: [ https://arxiv.org/abs/2509.06784](https://arxiv.org/abs/2509.06784).  
- Code: [https://github.com/Tencent-Hunyuan/Hunyuan3D-Part/tree/main/P3-SAM/](P3-SAM/).  
- Project Page: [https://murcherful.github.io/P3-SAM/ ](https://murcherful.github.io/P3-SAM/).
- Weights: [https://huggingface.co/tencent/Hunyuan3D-Part](https://huggingface.co/tencent/Hunyuan3D-Part)  
- HuggingFace Demo: [https://huggingface.co/spaces/tencent/Hunyuan3D-Part](https://huggingface.co/spaces/tencent/Hunyuan3D-Part).   
<img src="P3-SAM/images/teaser.jpg" alt="drawing" width="800"/>



###  X-Part： high-fidelity and structure-coherent shape decomposition  



- Paper: [https://arxiv.org/abs/2509.08643](https://arxiv.org/abs/2509.08643).  
- Code: [https://github.com/Tencent-Hunyuan/Hunyuan3D-Part/tree/main/XPart](XPart/).
- Project Page: [https://yanxinhao.github.io/Projects/X-Part/](https://yanxinhao.github.io/Projects/X-Part/).  
- Weights: [https://huggingface.co/tencent/Hunyuan3D-Part](https://huggingface.co/tencent/Hunyuan3D-Part)
- HuggingFace Demo: [https://huggingface.co/spaces/tencent/Hunyuan3D-Part](https://huggingface.co/spaces/tencent/Hunyuan3D-Part).    
<img src="XPart/assets/teaser.jpg" alt="drawing" width="800"/>





### **Notice**    
- **The current release is a light version of X-Part**. The full version is available on [![Hunyuan3D-Studio](https://img.shields.io/badge/Hunyuan3D-Studio-yellow)](https://3d.hunyuan.tencent.com/studio).  
- For X-Part, we recommend using ​​scanned​​ or ​​AI-generated meshes​​ (e.g., from Hunyuan3D V2.5 or V3.0) as input.
- P3-SAM can handle any input mesh. 



#### 🔗 Citation

```
@article{ma2025p3sam,
  title={P3-sam: Native 3d part segmentation},
  author={Ma, Changfeng and Li, Yang and Yan, Xinhao and Xu, Jiachen and Yang, Yunhan and Wang, Chunshi and Zhao, Zibo and Guo, Yanwen and Chen, Zhuo and Guo, Chunchao},
  journal={arXiv preprint arXiv:2509.06784},
  year={2025}
}

@article{yan2025xpart,
  title={X-Part: high fidelity and structure coherent shape decomposition},
  author={Yan, Xinhao and Xu, Jiachen and Li, Yang and Ma, Changfeng and Yang, Yunhan and Wang, Chunshi and Zhao, Zibo and Lai, Zeqiang and Zhao, Yunfei and Chen, Zhuo and others},
  journal={arXiv preprint arXiv:2509.08643},
  year={2025}
}
```
