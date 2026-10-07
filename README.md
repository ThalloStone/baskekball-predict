# baskekball-predict
·best.pt是基于yolo11n的自训练模型
·为保证稳定性，采用了旧版本的yolo，因此同样需要旧版pytorch支持
运行操作：
1.需要ultralytics-8.3.163本体文件
2.配置pytorch
为保证环境安全，使用Anaconda创建虚拟环境后安装
注意cuda版本最好为128
  50系英伟达PyTorch官方安装命令：
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
  非50系英伟达PyTorch官方安装命令：
pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu118
  非50系英伟达PyTorch镜像安装命令：
pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 -f https://mirrors.aliyun.com/pytorch-wheels/cu118
  CPU版PyTorch官方安装命令：
pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cpu
3.用编辑器打开ultralytics-8.3.163项目，将仓库中的“best.pt"和"test-01.py"复制到ultralytics-8.3.163目录下
4.打开"test-01.py"，将其中的中文替换为你要预测的文件的绝对路径
5.指定python解释器为（2）中的conda虚拟环境
6.运行"test-01.py"，一般可以在ultralytics-8.3.163\run目录下找到预测结果
