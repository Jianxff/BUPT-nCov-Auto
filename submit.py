from datetime import time
import time
import os
import requests
import logging
from base import USER_AGENT, DATA, FORM_URL, logging

def submit(session):
    AREA     = os.environ.get('AREA','')
    area = AREA.split('+')

     # 设置表单数据
    data = DATA
    data['created'] = str(round(time.time()))
    data["area"] = AREA
    data["city"] = area[0] if len(area) == 2 else area[1]
    data["province"] =area[0]
    data["sfzx"] = 1 if area[-1] == '海淀区' else 0
    logging.info('Area: %s', AREA)
    logging.debug(data)

    # 发送请求，设置cookies
    headers = { "User-Agent": USER_AGENT }

    # 填报
    response = session.post(url = FORM_URL, headers = headers, data = data)
    logging.info('Push Response: %s', response)

    if response.status_code != 200:
        return 'HTTP ' + response.status_code
    else:
        try:
            return response.json()['m']
        except Exception:
            return 'Authorize Failed'