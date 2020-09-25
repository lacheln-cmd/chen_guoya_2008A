import allure
import requests

@allure.feature("get请求")
@allure.story("嘀嘀嘀")
@allure.title("用例名1")
def test_no_params():
    # r = requests.get("http://www.baidu.com")
    # r = requests.request(method="get",url="http://www.baidu.com")
    sess = requests.session()
    r = sess.request(method="get",url="http://www.baidu.com")
    r =sess.request(method="get",url="http://www.baidu.com")
    print(r.text)
    pass

@allure.feature("get请求")
@allure.story("哈哈哈")
@allure.title("用例名2")
def test_get_params():
    pa = {"accountName":"chao123"}
    r = requests.request("get","http://qa.yanl.com:8084/acc/getAccInfo",params=pa)
    print(r.text)

@allure.feature("get请求")
@allure.story("呵呵呵")
@allure.title("用例名3")
def test_get_path():
    pa = {"accountName":"chao123"}
    r = requests.request("get","http://qa.yansl.com:8084/acc/getAcc/{}/{}".format(1,10))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例名4")
def test_get_file(pub_data):
    with allure.step("第一步：准备测试数据"):pass
    p = {"pridCode":"63803y"}
    h = {"token":pub_data["token"]}
    with allure.step("第二步;发送请求"):pass
    r = requests.request("get","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步：请求数据"):
        allure.attach("sakndfk,jabnfklanpk,sandplamd","请求信息",allure.attachment_type.TEXT)
    with open("cc.xls","wb") as f:
        f.write(r.content)

