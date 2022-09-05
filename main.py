import requests
from login import login
from push import push
from submit import submit
from base import logging

if __name__ == '__main__':
    # os.environ['USERNAME'] = '' # 学号
    # os.environ['PASSWORD'] = '' # 信息门户密码
    # os.environ['AREA'] = ''     # '省+市+县'
    # os.environ['PUSHDEER'] = '' # PushDeer Key
    
    session = requests.Session()
    login(session)
    msg = submit(session)

    # msg push
    logging.info(msg)
    push(msg)
