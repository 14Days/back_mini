## 接口文档

- 注册接口

  - 请求验证码接口

    - Url：http://{{host}}/user/code

    - Method: get

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

    - Url：http://{{host}}/user/account

    - method: post

    - 参数（Json格式）

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
        

- 登录接口

  - Url: http://{{host}}/user/authorization

  - method: post

  - 参数（Json格式）

    ```json
    {
    	"name": "guyunkai",
    	"password": "123456"
    }
    ```

  - 返回数据格式

    - 请求成功

      ```json
      {
          "status": "success",
          "data": "headers.payloads.signiture"
      }
      ```

    - 请求失败

      ```json
      {
          "status": "error",
          "err_msg": "登录失败"
      }
      ```


