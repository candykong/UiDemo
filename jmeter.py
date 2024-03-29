import os
import time
import subprocess
from util import network
from util.feishu import send_feishu_message
from config import setting

# 定义报告文件夹的路径
# script_folder = '/Users/kongzhibing/Desktop/流量回放'
script_folder = setting.TRAFFIC_PLAYBAN_DIR

# 获取当前时间戳
timestamp = int(time.time())
# 创建结果文件夹
result_folder = os.path.join(script_folder, f'result_{timestamp}')
os.makedirs(result_folder)

report_folder = os.path.join(result_folder, 'report')
os.makedirs(report_folder)

# 获取ip地址和设置端口
ip = network.get_ip_address()
port=12345

def run_jmeter(jmx_file):
    """
    执行jmeter脚本并生成报告
    :param jmx_file:
    :return:
    """


    # 执行 JMeter 命令
    jmx_file = os.path.join(script_folder, jmx_file)
    jtl_file = os.path.join(result_folder, f'result_{timestamp}.jtl')
    subprocess.run([
        'jmeter',
        '-n',
        '-t', jmx_file,
        '-l', jtl_file,
        '-e',
        '-o', report_folder
    ]).check_returncode()

    webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/3a029b35-396c-46c7-8f53-133efc1ee78f'
    message = f"请查看jmeter接口自动化报告：http://{ip}:{port}/index.html"
    send_feishu_message(webhook_url, message)

    subprocess.run([
        'python3',
        '-m',
        'http.server',
        str(port),
        '-d', report_folder,
        '--bind', str(ip)
    ])


if __name__ == '__main__':
    # 调用函数并传入 JMeter 脚本文件路径
    run_jmeter('sbed.jmx')
    # 发送查看报告路径--飞书群内机器人


