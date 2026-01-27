docker run -d \
  --name judgehost \
  --hostname judgehost \
  --privileged \
  --cgroupns=host \
  --restart always \
  -e DAEMON_ID=4 \
  -e JUDGEDAEMON_PASSWORD=domjudgeisas \
  -e DOMSERVER_BASEURL=http://192.168.17.108/ \
  -e CONTAINER_TIMEZONE=Asia/Bangkok \
  -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
  -v /var/run/docker.sock:/var/run/docker.sock \
  domjudge/judgehost:9.0.0
