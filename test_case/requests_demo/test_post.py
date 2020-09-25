import requests
#
# def test_post_json():
#     data = {
#   "pwd": "abc123",
#   "userName": "tuu653"
# }
#     r = requests.post("http://qa.yansl.com:8084/login",json=data)
#     print(r.text)


# def test_post_formdata(pub_data):
#     # post请求键值对数据
#     data = {
#   "userName": "tuu653"
# }
#     h = {"token":pub_data["token"]}
#     r = requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h)
#     print(r.text)


def test_post_upload_file(pub_data):
    # post请求上传文件
    data = {
        "file":open("cc.xls","rb")
}
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h)
    print(r.text)