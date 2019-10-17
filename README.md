## 接口文档

### 注册接口

#### 请求验证码

- url：/user/code

- method：GET

- args：

  | key | value |
  | ------ | ------ |
  | phone | 13588213889 |

- response：

  ```json
{
    "status": "success",
    "data": "短信发送成功"
  }
  
  {
    "status": "error",
  "err_msg": "短信发送失败"
  }
```

#### 注册接口

- url：/user/account

- method：POST

- args：

  ```json
  {
  	"phone": "13588213889",
  	"code": "6143",
  	"password": "123456",
  	"name": "Mike"
  }
  ```

- response：

  ```json
{
    "status": "success",
    "data": "验证成功"
  }
  
  {
    "status": "error",
  "err_msg": "验证码错误"
  }
```

### 登录接口

- url：/user/authorization

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
    "data": "headers.payloads.signiture"
  }
  
  {
    "status": "error",
  "err_msg": "登录失败"
  }
```


