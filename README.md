
## 接口文档

### 注册

#### 获取验证码

- URL：/user/code

- method：GET

- args：

  |  Key  | Require |      Value       |
  | :---: | :-----: | :--------------: |
  | phone |  True   | 11位中国手机号码 |

- response：

  ```json
  {
    "status": "success",
    "data": "msg"
  }
  ```

  ```json
  {
    "status": "error",
    "err_msg": "msg"
  }
  ```
  

#### 注册用户

- URL：/user/account

- method：POST

- args：

  ```json
  {
    "phone": "18807424758",
    "code": "6143",
    "password": "123456",
    "name": "Mike"
  }
  ```
  
- response：

  ```json
  {
    "status": "success",
    "data": "msg"
  }
  ```

  ```json
  {
    "status": "error",
    "err_msg": "msg"
  }
  ```

### 登录

- URL：/user/authorization

- method：POST

- args：

  ```json
  {
    "name": "guyunkai",
    "password": "123456"
  }
  ```

- response：

  ```json
  {
    "status": "success",
    "data": "token"
  }
  ```

  ```json
  {
    "status": "error",
    "err_msg": "msg"
  }
  ```


### 公告

- URL：/notice

- method：GET

- header：token

- response：

  ```json
  {
    "status": "success",
    "data": {
      "title": "样例",
      "content": "内容"
    }
  }
  ```

### 图片相关

#### 轮播图

- URL：/img/cycle

- method：GET

- header：token

- response：（`http://pull.wghtstudio.cn/img/`为图片请求前缀）

  ```json
  {
    "status": "success",
    "data": [
      "1.jpg",
      "2.jpg",
      "3.jpg",
      "4.jpg",
      "5.jpg",
      "6.jpg"
    ]
  }
  ```
  

#### 未打标图片

- URL：/img/imgs

- method：GET

- args：

  | Key  | value |
  | :--: | :---: |
  | num  |  int  |

- header：token

- response：

  ```json
  {
    "status": "success",
    "data": [
      {
        "id": 1,
        "url": "6.jpg"
      },
      {
        "id": 1,
        "url": "6.jpg"
      }
    ]
  }
  ```

#### 搁置图片

- URL：/img/unknown

- method：GET

- header：token

- response：

  ```json
  {
    "status": "success",
    "data": [
      {
        "id": 1,
        "url": "6.jpg"
      },
      {
        "id": 1,
        "url": "6.jpg"
      }
    ]
  }
  ```

#### 获取标签

- URL：/img/tags

- method：GET

- header：token

- response：

  ```json
  {
    "status": "success",
    "data": [
      {
        "top": "风格",
        "second": [
          {
            "id": 3,
            "tag": "典雅的"
          }
        ]
      }
    ]
  }
  ```

### 打标

- URL: /tag

- method: POST

- args: 

  ```json
  {
    "img_id": 7,
    "tag": [1, 2]
  }
  ```

- response：

  ```json
  {
      "status": "success",
      "data": "图片提交完成"
  }
  ```

  ```json
  {
      "status": "error",
      "err_msg": "提交失败"
  }
  ```

### 统计数据

- URL：/record

- method：GET

- header：token

- response：

  ```json
  {
      "status": "success",
      "data": {
          "day": 0,
          "week": 5
      }
  }
  ```

