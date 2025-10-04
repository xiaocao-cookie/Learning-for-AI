# YOLO目标检测系统

一个基于TensorFlow、Keras和Flask的YOLO (You Only Look Once) 目标检测Web应用。

## 项目简介

本项目实现了一个基于YOLO算法的目标检测系统，用户可以通过Web界面上传图片和视频，系统会自动进行目标检测并返回带有检测框和类别标签的结果。

主要功能：
- Web界面上传图片和视频进行目标检测
- 实时显示检测结果，包括边界框、类别标签和置信度
- 美观友好的用户界面，支持响应式设计

## 环境要求

- Python 3.8+ 或更高版本
- TensorFlow 2.x
- Keras 2.14.0
- Flask 3.1.2+ 
- OpenCV
- NumPy 1.18.0+
- Pillow 8.0.0+

## 快速开始

### 方法一：使用批处理脚本（推荐）

1. 确保已安装Python 3.8+环境
2. 双击运行项目根目录下的 `run.bat` 文件
3. 脚本会自动：
   - 创建虚拟环境
   - 安装所有依赖包
   - 启动Web服务
4. 打开浏览器，访问 `http://localhost:5000` 开始使用

### 方法二：手动安装

1. 克隆或下载本项目到本地
2. 安装所需依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```bash
   python app.py
   ```
4. 打开浏览器，访问 `http://localhost:5000` 开始使用

## 项目结构

```
yolo_demo/
├── font/                 # 项目所需字体
├── images/               # 示例图片目录
├── model_data/           # YOLO模型数据文件
├── nb_images/            # notebook图片
├── out/                  # 示例输出结果
├── outputs/              # 检测结果图片存储目录
├── templates/            # Flask模板文件
│   └── index.html        # 项目主页面
├── uploads/              # 用户上传图片存储目录
├── app.py                # 主应用程序文件
├── requirements.txt      # 项目依赖清单
├── run.bat               # 快速启动脚本
├── test.ipynb            # 检测图像格式和视频帧数
├── yolo_demo.ipynb       # yolo_demo
├── yad2k/                # YOLO到Keras转换工具库
```



## 故障排除

1. **端口被占用**：
   - 错误信息：`Address already in use`
   - 解决方法：修改 `app.py` 中的端口号，或关闭占用该端口的程序

2. **依赖安装失败**：
   - 错误信息：`Could not find a version that satisfies the requirement`
   - 解决方法：更新pip工具，或尝试手动安装特定版本的依赖包

3. **模型文件缺失**：
   - 错误信息：`Could not find model_data/yolo.h5`
   - 解决方法：确保 `model_data/` 目录下包含所需的模型文件

4. **中文显示问题**：
   - 错误信息：页面显示乱码
   - 解决方法：确保浏览器编码设置为UTF-8

   
## 注意事项

- <span style="color: red">实现此项目前务必先理解 `yolo_demo` 文件中的每一步</span>
- 上传图片的大小会影响检测速度，建议使用适中大小的图片
- 目标检测的准确率取决于模型训练数据和检测参数设置
- 处理大图片可能会消耗较多系统资源，建议根据实际硬件配置调整
- 本项目仅供学习和研究使用


## Acknowledgements

- 本项目基于YOLO算法实现
- 使用TensorFlow和Keras作为深度学习框架
- 使用Flask构建Web应用界面