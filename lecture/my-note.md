# 我的筆記

## pip

新安裝python建議先更新pip

```shell
python -m pip install --upgrade pip
```

- 顯示過期的包

```shell
pip list --outdated 
```

- 更新所有過期的包，網路上說的很多都已經過期了，下面是最新的指令

```shell
pip list --outdated | ForEach-Object {pip install --upgrade ($_.Split(' ')[0])}
```

- 更新單一的包

```shell
pip install --upgrade 包名
```

