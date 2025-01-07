# 使用

修改代码中的js代码进行测试


##  构建
```bash
docker build -t testjs2py .
```

## 使用
```bash
docker run -d --name test testjs2py
```

# 打包

## 安装打包工具nuitka
```
pip install nuitka
```


## 打包py脚本
```bash
nuitka --standalone --onefile --output-dir=output app.py
```
