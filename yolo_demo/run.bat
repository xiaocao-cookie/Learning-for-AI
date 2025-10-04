@echo off

REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python环境。请先安装Python 3.8或更高版本。
    pause
    exit /b 1
)

REM 获取Python版本信息
for /f "tokens=2 delims=." %%a in ('python --version 2^>^&1') do set "PYTHON_MINOR=%%a"

REM 检查Python版本是否满足要求（至少3.8）
if %PYTHON_MINOR% LSS 8 (
    echo 错误: Python版本过低。请安装Python 3.8或更高版本。
    pause
    exit /b 1
)

REM 设置虚拟环境目录
set "VENV_DIR=.venv"

REM 检查虚拟环境是否已存在
if not exist %VENV_DIR% (
    echo 创建虚拟环境...
    python -m venv %VENV_DIR%
    if errorlevel 1 (
        echo 错误: 创建虚拟环境失败。
        pause
        exit /b 1
    )
)

REM 激活虚拟环境
echo 激活虚拟环境...
call %VENV_DIR%\Scripts\activate

REM 检查是否成功激活虚拟环境
echo %VIRTUAL_ENV% | findstr /i "%VENV_DIR%" >nul
if errorlevel 1 (
    echo 警告: 虚拟环境激活可能失败，尝试直接安装依赖...
)

REM 更新pip
echo 更新pip...
python -m pip install --upgrade pip

REM 安装项目依赖
echo 安装项目依赖...
pip install -r requirements.txt
if errorlevel 1 (
    echo 警告: 依赖安装过程中出现错误。
)

REM 检查并创建必要的目录
if not exist "uploads" mkdir "uploads"
if not exist "outputs" mkdir "outputs"

REM 启动应用
echo 启动YOLO目标检测服务...
echo 请等待，服务启动后将显示访问地址。
python app.py

REM 如果应用意外退出，则显示错误信息
if errorlevel 1 (
    echo 错误: 应用启动失败。
    pause
    exit /b 1
)

pause