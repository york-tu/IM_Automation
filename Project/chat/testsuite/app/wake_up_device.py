# airtest_script.py
from airtest.core.api import *
import subprocess

# 連接設備，這裡的 IP 地址和端口根據你的實際情況設置
# 如果是 USB 連接，可以直接使用 "android:///"
connect_device("android:///")

# 喚醒手機並解鎖
wake()

# 等待解鎖界面出現
sleep(1)  # 根據需要調整等待時間
