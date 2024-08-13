from airtest.core.api import *

# 连接到 iOS 设备，假设设备的 IP 地址是 127.0.0.1:8100
connect_device("iOS:///127.0.0.1:8100")

# 等待屏幕亮起
keyevent("HOME")
sleep(2)
keyevent("HOME")

# 模拟滑动解锁，假设从屏幕底部向上滑动
# swipe((150, 800), (150, 90))

# 如果有密码，可以使用 text() 方法输入密码，然后点击确定
# 假设密码是 '1234'
# text("1234")

# 如果需要点击确定按钮，可以使用 touch() 方法点击确定按钮的位置
# 假设确定按钮的位置是 (300, 600)
# touch((300, 600))
