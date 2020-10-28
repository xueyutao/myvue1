# -*- coding:utf-8 -*-
import os
import sys
from Tool.idcard import idcard
from Tool.idcardBack import idcardBack
import uuid
import base64
import Model
from flask_cors import CORS
import flask,json
from flask import request
server = flask.Flask(__name__)  #实例化server，把当前这个python文件当做一个服务，__name__代表当前这个python文件
CORS(server, resources=r'/*')
@server.route('/readID',methods=['post'])
def readID():
    data = request.form.get("image")
    imgString = data.encode().split(b';base64,')[-1]
    imgString = base64.b64decode(imgString)
    jobid = uuid.uuid1().__str__()
    path = 'models/test/{}.png'.format(jobid)
    with open(path, 'wb') as f:
        f.write(imgString)
    result = Model.model(path,'ID')
    idcardList = idcard(result).res
    if idcardList['身份证号码'] == '识别失败':
        os.remove(path)
        return json.dumps({'status': '400','message': '识别失败'}, ensure_ascii=False)
    idcardInfo = {'status': '200', '姓名': idcardList['姓名'], '性别': idcardList['性别'], '民族': idcardList['民族'],
                  '身份证号码': idcardList['身份证号码']}
    os.remove(path)
    return json.dumps(idcardInfo,ensure_ascii=False)

@server.route('/readBack',methods=['post'])
def readBack():
    data = request.form.get("image")
    imgString = data.encode().split(b';base64,')[-1]
    imgString = base64.b64decode(imgString)
    jobid = uuid.uuid1().__str__()
    path = 'models/test/{}.png'.format(jobid)
    with open(path, 'wb') as f:
        f.write(imgString)
    result = Model.model(path,'Back')
    os.remove(path)
    return json.dumps(idcardBack(result).res,ensure_ascii=False)

@server.route('/test', methods=['get'])
def test():
    testInfo = {'status': 'success'}
    return json.dumps(testInfo)

#启动服务
if __name__ == "__main__":
    server.run(port=sys.argv[1], debug=True, host='0.0.0.0')
