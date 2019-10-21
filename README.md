

## 接口文档

### 注册

#### 获取验证码

- URL：/user/code

- method：GET

- args：

  |  key  |    value     |
  | :---: | :----------: |
  | phone | phone number |

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

### 用户登录

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

- args：headers

  | key   | value       |
  | ----- | ----------- |
  | token | token value |

  

- response：

  ```json
  {
    "status": "success",
    "data": "内容内容内容内容"
  }
  ```

### 轮播图

- URL：/img/cycle

- method：GET

- args：headers

- response：

  ```json
  {
    "status": "success",
    "data": [
      "http://pull.wghtstudio.cn/img/1.jpg",
      "http://pull.wghtstudio.cn/img/2.jpg",
      "http://pull.wghtstudio.cn/img/3.jpg",
      "http://pull.wghtstudio.cn/img/4.jpg",
      "http://pull.wghtstudio.cn/img/5.jpg",
      "http://pull.wghtstudio.cn/img/6.jpg"
    ]
  }
  ```
  
  ```json
  {
      "status": "error",
      "err_msg": "jwt已过期,请重新登录"
  }
  ```
  
  



### 图片

- URL：/img/imgs

- method：GET

- args：

  | key  | value |
  | ---- | ----- |
  | num  | 1     |

- response

  ```json
  {
    "status": "success",
    "data": [
      "http://pull.wghtstudio.cn/img/2.jpg",
      "http://pull.wghtstudio.cn/img/3.jpg",
      "http://pull.wghtstudio.cn/img/4.jpg",
      "http://pull.wghtstudio.cn/img/5.jpg",
      "http://pull.wghtstudio.cn/img/6.jpg",
      "http://pull.wghtstudio.cn/img/7.jpg"
    ]
  }
  ```

### 标签

- URL: /tag

- method: POST

- args: 

  ```json
  {
    "img_id": 7,
    "tag": [1, 2]
  }
  ```

- response

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

- URL: /record/count

- method: Get

- args: headers

- response

  ```json
  {
      "status": "success",
      "data": {
          "day": "0",
          "week": "5"
      }
  }
  ```

### 搁置图片

#### 提交搁置图片

- URL: /img/unknown

- method: Post

- args:

  ```json
  {
  	"img_id": 2
  }
  ```

- response

  ```json
  {
      "status": "success",
      "data": "请求成功"
  }
  ```

  ```json
  {
      "status": "error",
      "err_msg": "添加搁置图片失败"
  }
  ```

#### 请求搁置图片

- URL: /img/unknown

- method: Get

- args:

- response

  ```json
  {
      "status": "success",
      "data": [
          {
              "img_id": 1,
              "img_url": "http://pull.wghtstudio.cn/img/1.jpg"
          },
          {
              "img_id": 2,
              "img_url": "http://pull.wghtstudio.cn/img/2.jpg"
          },
          {
              "img_id": 4,
              "img_url": "http://pull.wghtstudio.cn/img/4.jpg"
          }
      ]
  }
  ```

  

