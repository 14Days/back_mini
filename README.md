## 接口文档

- 注册接口

  - 请求验证码接口

    - url：wghtstudio.cn/user/code

    - 参数

      | key | value |
      | ------ | ------ |
      | phone | 13588213889 |

    - 返回数据格式

      - 请求成功

        ```json
        {
            "status": "success",
            "data": "短信发送成功"
        }
        ```

      - 请求失败

        ```json
        {
            "status": "error",
            "data": "短信发送失败"
        }
        ```

  - 发送验证码接口

    - url：wghtstudio.cn/user/account

    - 参数

      ```json
      {
      	"phone": "13588213889",
      	"code": "6143",
      	"password": "123456",
      	"name": "Mike"
      }
      ```

    - 返回数据格式

      - 请求成功

        ```json
        {
            "status": "success",
            "data": "验证成功"
        }
        ```

      - 请求失败

        ```json
        {
            "status": "error",
            "data": "验证码错误"
        }
        ```

