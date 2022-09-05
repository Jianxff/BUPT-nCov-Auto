import os
from lxml import etree
from base import EXECUTION_XPATH, LOGIN_URL, SERVICE, USER_AGENT, logging

def login(session):
    USERNAME = os.environ.get('USERNAME','')
    PASSWORD = os.environ.get('PASSWORD','')

    # 发送请求，设置cookies
    headers = { "User-Agent": USER_AGENT }
    params = { "service": SERVICE }
    response = session.get(url=LOGIN_URL, headers=headers, params=params)

    # 获取execution
    html = etree.HTML(response.content)
    execution = html.xpath(EXECUTION_XPATH)[0]
    # logging.debug('execution: %s', execution)

    # 构造表单数据
    data = {
        'username': USERNAME,
        'password': PASSWORD,
        'submit': "登录",
        'type': 'username_password',
        'execution': execution,
        '_eventId': "submit"
    }

    # 登录到疫情防控通
    response = session.post(url=LOGIN_URL, headers=headers, data=data)
    logging.info('Login Response: %s',response)