# 예제 10-7 변경한 프로파일을 원격 컴퓨터에 복사하고 테스트하기

# 로컬 컴퓨터에서 실행한다.
$ scp /home/ian/.ipython/profile_mycluster/security/ipcontroller-engine.json
      ian@192.168.0.16:/home/ian/.config/ipython/profile_default/security/

# 이제 원격 컴퓨터에서 실행한다.
$ ipengine
...Using existing profile dir: u'/home/ian/.config/ipython/profile_default'
...Loading url_file u'/home/ian/.config/ipython/profile_default/security/
        ipcontroller-engine.json'
...Registering with controller at tcp://192.168.0.128:35963
...Starting to monitor the heartbeat signal from the hub every 3010 ms.
...Using existing profile dir: u'/home/ian/.config/ipython/profile_default'
...Completed registration with id 4
