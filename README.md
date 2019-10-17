## 接口文档

- 注册接口

  - 请求验证码接口

    - url：http://{{host}}/user/code

    - method: get

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

- 公告接口

  - Url: http://{{host}}/notice

  - Method: get

  - 参数 （无）

  - 返回数据格式

    - 请求成功

      ```json
      {
          "status": "success",
          "data": "内容内容内容内容"
      }
      ```

- 轮播图接口

  - Url: http://{{host}}/img/cycle

  - method: get

  - 参数 （无）

  - 返回数据格式

    - 请求成功

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

- 图片接口

  - 请求图片接口

    - Url: http://{{host}}/img/imgs

    - 参数

      | key  | value |
      | ---- | ----- |
      | num  | 1     |

    - 请求成功

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
