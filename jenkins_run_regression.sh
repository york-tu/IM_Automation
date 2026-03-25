#!/bin/sh
set -e
path=$1
filename=$2
env=$3
brand=$4
user=$5
test_list=$6
server_ip="10.200.252.204"

case "$brand" in
        lv) display=2;;
        ls) display=3;;
        hy) display=4;;
        c7) display=5;;
        c8) display=6;;
        tz) display=7;;
        bh) display=8;;
        3h) display=9;;
	sc) display=10;;
        cdd) display=11;;
        xpj) display=12;;
	co) display=13;;
        ttmj) display=14;;
        gu) display=15;;
        meet) display=16;;
        s365) display=17;;
        zqb) display=18;;
        zab) display=19;;
esac

case "$env" in
        prod) display=$((display + 50));;
        stage) display=$((display + 50));;
esac

xVNC_port=$((display + 5900))
noVNC_port=$(ruby -e 'require "socket"; puts Addrinfo.tcp("", 0).bind {|s| s.local_address.ip_port }')
volume=$(pwd)

sudo docker pull reg.paradise-soft.com.tw:5000/patrick_star
sudo docker stop "qa_${env}_${brand}" || true
sudo docker rm "qa_${env}_${brand}" || true
sudo docker run -i -u 0 -e LANG=zh_CN.UTF-8 --shm-size 31g --network host -v $volume:/qa --name 'qa_'$env'_'$brand -w /qa --rm reg.paradise-soft.com.tw:5000/patrick_star sh -c \
"
chmod 777 driver/driver/chromedriver_linux
sleep 2
Xvfb :$display -ac -screen 0 1920x1080x16 &
sleep 2

### Web VNC URL
x11vnc -display :$display -viewonly -forever -shared -bg -xdamage -rfbport $xVNC_port &
cd /noVNC/utils/ && sh launch.sh  --vnc $server_ip:$xVNC_port --listen $noVNC_port &
sleep 3
echo -e '\nDISPLAY=:' $display
echo '-----------------------------------------------'
echo 'Web VNC: http://'$server_ip':'$noVNC_port'/vnc.html'
echo -e '-----------------------------------------------\n'
export PYTHONPATH=\"/qa:${PYTHONPATH:-}\"
python3.6 -m pip uninstall -y xmlrunner >/dev/null 2>&1 || true
python3.6 -m pip install -r requirements.txt
DISPLAY=:$display python3.6 -B -u ${path}${filename} ${env} ${brand} ${user} ${test_list}
"

### 處理檔案權限
sudo chmod -R 777 *

### delete x11VNC process
echo "Kill Process Start"
ps -aux|grep $server_ip:$xVNC_port|xargs kill -9 &
echo "Kill Process End"