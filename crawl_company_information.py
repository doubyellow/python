# coding=utf-8
import requests
from lxml import etree
import re
import random
import time

file_write_company = open("./data_company.txt", "w+", encoding='utf-8')
global page

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://etax.shenzhen.chinatax.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def read_one_link():
    url = 'https://www.huangye88.com/'
    print("获取一级目录内容 start")
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # 全部行业一级分类链接
    try:
        one_link_list = html.xpath("//li[@class='menu_sa']/a/@href")
    except:
        return
    print(one_link_list)
    for one_link in one_link_list:
        if not read_two_link(one_link):
            print('获取二级目录内容 fail')
            continue
        "https://qiche.huangye88.com"
        time.sleep(random.random() * 5)
    file_write_company.close()
    print("获取一级目录内容 over")


def read_two_link(url):
    print("获取二级目录内容 start")
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    try:
        two_link_list = html.xpath("//li[@class='s1 indent']/a/@href")
    except:
        return
    print(two_link_list)
    for two_link in two_link_list:
        if not read_three_link(two_link):
            print('获取三级目录内容 fail')
            continue
        "http://qiche.huangye88.com/diandongqiche/"
        time.sleep(random.random() * 5)
        print("获取二级目录内容 over")
    return two_link_list


def read_three_link(url):
    print("获取三级目录内容 start")
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    try:
        three_link_list = html.xpath("//ul[@class='app_list app_list2 clearfix']/li/a/@href")
    except:
        return
    print(three_link_list)
    for three_link in three_link_list:
        if not read_four_link(three_link):
            print('获取四级目录内容 fail')
            continue
        "http://qiche.huangye88.com/diandongqiche/chundiandongqiche/"
        time.sleep(random.random() * 5)
    print("获取三级目录内容 over")
    return three_link_list


def read_four_link(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    try:
        company_link_list = html.xpath("//div[@class='edge company']/a/@href")  # 所有公司链接
    except:
        print('获取企业内容 fail')
        return
    company_destail_list = map(lambda company_link: company_link + 'company_detail.html', company_link_list)
    company_set = set(company_destail_list)
    for company_destail in company_set:
        data = read_company_link(company_destail)
        if data:
            print('获取第%s个公司信息成功' % page)
            page += 1
            file_write_company.write(company_destail + "\n")
            file_write_company.write(data + "\n")
        time.sleep(random.random() * 5)
    return company_set


def read_company_link(url):
    response = requests.get(url, headers=headers)
    text = response.content.decode('UTF-8')
    html = etree.HTML(text)
    try:
        company_name = html.xpath("//p[@class='com-name']/text()")
    except:
        return
    company_data = {}
    if company_name:
        company_data['公司名称'] = company_name[0]
        lis = html.xpath("//ul[@class='con-txt']/li//text()")
        """['企业法人：', '彭运', '注册城市：', '广东 深圳', '企业类型：', '有限责任公司(自然人独资)', '成立时间：', '2011-07-19', '注册资金：', '人民币10万', '员工人数：',
                 '5 - 10 人', '主营行业：', '锂电池', '主营产品：', '回收锂电池,回收聚合物电芯,回收动力电池,回收电池模组']"""
        lis = list(map(lambda a: re.sub("/s|：| ", "", a), lis))
        company_dict = dict(zip(lis[0::2], lis[1::2]))  # 将list转化为dict
        """{'企业法人': '彭运', '注册城市': '广东深圳', '企业类型': '有限责任公司(自然人独资)', '成立时间': '2011-07-19', '注册资金': '人民币10万', '员工人数': '5-10人',
                 '主营行业': '锂电池', '主营产品': '回收锂电池,回收聚合物电芯,回收动力电池,回收电池模组'}"""
        company_data.update(company_dict)

        company_text = ''.join(html.xpath("//p[@class='txt']/text()"))
        company_text = re.sub("\s", "", company_text)
        company_data['公司介绍'] = company_text
        detail_list = html.xpath("//div[@class='r-content']/table/tr//text()")
        detail_list = list(map(lambda a: re.sub("/s|：| ", "", a), detail_list))
        detail_dict = dict(zip(detail_list[0::2], detail_list[1::2]))  # 将list转换为dict
        """
        {'采购产品': '锂电池', '主营地区': '中国', '研发部门人数': '5-10人', '经营模式': '生产型', '经营期限': '1949-01-01至2026-01-01', '最近年检时间': '2017年',
         '登记机关': '深圳市市场监督管理局', '主要客户群': '所有人群', '年营业额': '人民币10万元/年以下', '年营出口额': '人民币10万元/年以下', '年营进口额': '人民币10万元/年以下',
         '经营范围': '电池、移动电源、电子元器件、电子产品、数码产品的销售；国内贸易，货物及技术进出口。(法律、行政法规、国务院决定规定在登记前须经批准的项目除外，涉及行政许可的，须取得行政许可后方可经营）^',
         '是否提供OEM': '否', '公司邮编': '518000', '公司电话': '\U000880fb\U00088102\U00088100\U00088100-\U000880fc\U000880fe\U000880ff\U00088103\U000880fb\U00088102\U000880fc\U000880fd\U000880fb\U00088100\U00088101',
                                                              0755-13480712056
          '行政区域': '广东深圳', '公司地址': '宝安'}
        """
        company_data.update(detail_dict)
        our_content = html.xpath("//div[@class='l-content']/ul/li//text()")[:10]
        our_content = list(map(lambda a: ''.join(a.split()), our_content))
        our_content = list(map(lambda a: re.sub("/s|：| ", "", a), our_content))
        our_content = dict(zip(our_content[0::2], our_content[1::2]))  # 将list转换为dict
        company_data.update(our_content)
        return str(company_data)


if __name__ == '__main__':
    read_one_link()
