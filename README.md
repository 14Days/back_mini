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