# 예제 10-6 외부 연결을 수락하는 로컬 프로파일 만들기

$ ipython profile create mycluster --parallel
$ gvim /home/ian/.ipython/profile_mycluster/ipengine_config.py
# 맨위 근처에 "c.HubFactory.ip = '*'"를 추가하라
$ ipcluster start -n 4 --profile=mycluster
