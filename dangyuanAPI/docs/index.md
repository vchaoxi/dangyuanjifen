[TOC]

# 党员积分接口文档 

## 注册

### 核实党员身份信息是否有效

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/users/check_m_valid

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        | 
|   idnumber   |  410324199307112512   |
|   truename   |         刘浩           |

返回值类型： application/json

返回值示例：

```json
{
	"data": {
		"create_time": 1548144988,
		"id": 72,
		"idnumber": "410324199307112512",
		"is_reged": 0,
		"status": 1,
		"truename": "\u5218\u6d69"
	},
	"errmsg": "\u6210\u5458\u6570\u636e\u53ef\u7528",
	"errno": "1"
}
```
——————————————————————————————————————————————————————

### 党内职务列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/dangzhibu/dang_level

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：无

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"10": "\u666e\u901a\u515a\u5458",
		"20": "\u515a\u5c0f\u7ec4\u957f",
		"30": "\u515a\u652f\u90e8\u4e66\u8bb0",
		"40": "\u515a\u59d4\u59d4\u5458",
		"50": "\u515a\u59d4\u4e66\u8bb0"
	},
	"errmsg": "\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 党支部列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/dangzhibu/

请求类型：POST

请求数据类型：application/x-www-form-urlencoded

请求参数：无

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"10": "\u529e\u516c\u5ba4\uff08\u515a\u59d4\u529e\u516c\u5ba4\uff09\u515a\u652f\u90e8",
		"100": "\u515a\u59d4\u7ec4\u7ec7\u90e8\uff08\u4eba\u529b\u8d44\u6e90\u90e8\uff09\u515a\u652f\u90e8",
		"110": "\u515a\u5efa\u5de5\u4f5c\u90e8\uff08\u5de5\u4f1a\u3001\u56e2\u59d4\uff09\u515a\u652f\u90e8",
		"120": "\u76d1\u5bdf\u5ba1\u8ba1\u515a\u652f\u90e8",
		"130": "\u8fd0\u8425\u76d1\u6d4b\u4e2d\u5fc3\u515a\u652f\u90e8",
		"140": "\u7535\u529b\u8c03\u63a7\u4e2d\u5fc3\u515a\u652f\u90e8",
		"150": "\u79bb\u9000\u4f11\u515a\u603b\u652f",
		"160": "\u56fd\u7f51\u7518\u5dde\u533a\u4f9b\u7535\u516c\u53f8\u515a\u603b\u652f",
		"170": "\u56fd\u7f51\u5c71\u4e39\u53bf\u4f9b\u7535\u516c\u53f8\u515a\u603b\u652f",
		"180": "\u56fd\u7f51\u9ad8\u53f0\u53bf\u4f9b\u7535\u516c\u53f8\u515a\u603b\u652f",
		"190": "\u7f51\u4e34\u6cfd\u53bf\u4f9b\u7535\u516c\u53f8\u515a\u603b\u652f",
		"20": "\u53d1\u5c55\u7b56\u5212\u90e8\u515a\u652f\u90e8",
		"200": "\u7ecf\u6d4e\u6280\u672f\u7814\u7a76\u6240\u515a\u652f\u90e8",
		"210": "\u4fe1\u606f\u901a\u4fe1\u516c\u53f8\u515a\u652f\u90e8",
		"220": "\u7269\u8d44\u4f9b\u5e94\u4e2d\u5fc3\u515a\u652f\u90e8",
		"230": "\u7efc\u5408\u670d\u52a1\u4e2d\u5fc3\u515a\u652f\u90e8",
		"240": "\u4e09\u65b0\u4f9b\u7535\u670d\u52a1\u4e2d\u5fc3\u515a\u652f\u90e8",
		"250": "\u4f9b\u7535\u670d\u52a1\u4e2d\u5fc3\u515a\u652f\u90e8",
		"260": "\u91d1\u6e90\u7535\u529b\u5de5\u7a0b\u516c\u53f8\u515a\u603b\u652f",
		"270": "\u8f6f\u4ef6\u6d4b\u8bd5\u515a\u652f\u90e8",
		"30": "\u8d22\u52a1\u8d22\u4ea7\u90e8\u515a\u652f\u90e8",
		"40": "\u5b89\u5168\u76d1\u5bdf\u8d28\u91cf\u90e8\u515a\u652f\u90e8",
		"50": "\u5efa\u8bbe\u90e8\u515a\u652f\u90e8",
		"60": "\u8fd0\u7ef4\u68c0\u4fee\u90e8\u515a\u603b\u652f",
		"70": "\u53d8\u7535\u8fd0\u68c0\u5ba4\u515a\u652f\u90e8",
		"80": "\u8f93\u7535\u8fd0\u68c0\u5ba4\u515a\u652f\u90e8",
		"90": "\u8425\u9500\u90e8\u515a\u652f\u90e8"
	},
	"errmsg": "\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 党小组列表

维护人员：刘浩

接口详情：获取党员所在党支部的党小组列表

请求地址：http://192.168.5.122:5000/api/v1_0/dangzhibu/dang_zu

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        | 
|   dang_zid   |        270            |

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"create_time": 1547985576,
		"dang_zid": 270,
		"id": 57,
		"leader": 0,
		"name": "\u8f6f\u4ef6\u6d4b\u8bd5",
		"sort": 0,
		"status": 1
	}],
	"errmsg": "\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 核实党员联系方式有效性

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/users/check_mobile_valid

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        | 
|   phonenum   |     17625701390       |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u624b\u673a\u53f7\u53ef\u4f7f\u7528",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 短信验证码

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/smsnotify

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        | 
|   phonenum   |     17625701390       |

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"content": "952528",
		"phone": "17625701390"
	},
	"errmsg": "\u77ed\u4fe1\u9a8c\u8bc1\u7801\u53d1\u9001\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 注册

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/users/register

请求类型：POST

请求参数类型：multipart/form-data

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        | 
|    avater    |    头像的二进制文件      |
|   dang_gid   |        57             |
| dang_jointime|     2019-03-08        |
|  dang_level  |        50             |
|  dang_zid    |       270             |
|   jiguan     |       郑州             |
|   madta      |        72             |
|   mingzu     |        汉             |
|  password    |      123456           |
|  phonenum    |    17625701390        |
|    sex       |        1              |
| truename     |      刘浩              |
|  work_date   |   2019-03-08          |
| work_gangwei |      测试              |
| work_xueli   |      本科              |
| work_zhicheng|    测试工程师           |
|     img      |    图片信息二进制文件    |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u6ce8\u518c\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

## 登录

### 登录党员积分app

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/users/login

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值          |
| :-----------:|      :-------:        |
|   password   |       123456          |
|   phonenum   |     17625701390       |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u767b\u5f55\u6210\u529f",
	"errno": "1",
	"info": {
		"act_permission": 0,
		"avatar": "http://oldpic.vchaoxi.com/Fh4MEbGREf-6SllqZC7-9uOTaPa0",
		"dang_gid": 57,
		"dang_level": 50,
		"dang_zid": 270,
		"is_cyjf": 1,
		"is_dabwy": 0,
		"is_djgly": 0,
		"mobile": "17625701390",
		"reg_time": 1552015594,
		"sex": 1,
		"status": 1,
		"token": "MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs",
		"truename": "\u5218\u6d69",
		"uid": 634
	}
}
```
————————————————————————————————————————

## 首页

### 根据小组ID返回小组基本信息

维护人员：刘浩
 
接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/dangzhibu/zu_info

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   dang_gid   |         57                       |
|    token     | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"create_time": 1547985576,
		"dang_zid": 270,
		"id": 57,
		"leader": 604,
		"name": "\u8f6f\u4ef6\u6d4b\u8bd5",
		"sort": 0,
		"status": 1
	},
	"errmsg": "\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 近期安排列表

维护人员：刘浩

接口详情：获取会议和活动列表

请求地址：http://192.168.5.122:5000/api/v1_0/activity/activity_list

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   is_index   |          1                       |
|   is_mydang  |          1                       |
|    token     | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |

返回值类型：application/json

返回值示例：

```json
{
	"current_page": 1,
	"data": [{
		"begin_time": 1551949200,
		"cate_1": "\u57f9\u8bad",
		"cate_2": "",
		"cate_2_son": "",
		"contact_mobile": "17625701390",
		"contact_name": "\u5218\u6d69",
		"create_time": 1551776559,
		"dang_zid": 270,
		"id": 356,
		"is_allin": 0,
		"location": "123",
		"location_small": "",
		"locx": "",
		"locy": "",
		"removes": "",
		"schedule_id": "",
		"title": "\u57f9\u8bad",
		"type": 2,
		"uid": 579,
		"yaoqiu": "321"
	}, {
		"begin_time": 1551938721,
		"cate_1": "\u515a\u5c0f\u7ec4\u4f1a",
		"cate_2": "",
		"cate_2_son": "",
		"contact_mobile": "18530071350",
		"contact_name": "\u59dc\u6b22",
		"create_time": 1551765928,
		"dang_zid": 270,
		"id": 355,
		"is_allin": 0,
		"location": "\u54c7\u997f\u5206111",
		"location_small": "",
		"locx": "",
		"locy": "",
		"removes": "",
		"schedule_id": "",
		"title": "\u5206",
		"type": 1,
		"uid": 629,
		"yaoqiu": "\u5206\u54c7\u4e2a v"
	}, {
		"begin_time": 1551756008,
		"cate_1": "\u515a\u5458\u4e2d\u5fc3\u7ec4\u7406\u8bba\u5b66\u4e60\u4f1a\u8bae",
		"cate_2": "",
		"cate_2_son": "",
		"contact_mobile": "18530071350",
		"contact_name": "\u59dc\u6b22",
		"create_time": 1551756013,
		"dang_zid": 270,
		"id": 343,
		"is_allin": 0,
		"location": "\u5206",
		"location_small": "",
		"locx": "",
		"locy": "",
		"removes": "",
		"schedule_id": "",
		"title": "\u5206",
		"type": 1,
		"uid": 629,
		"yaoqiu": "\u5206"
	}, {
		"begin_time": 1551755752,
		"cate_1": "\u4f5c\u98ce\u5efa\u8bbe",
		"cate_2": "",
		"cate_2_son": "",
		"contact_mobile": "17625701390",
		"contact_name": "\u5218\u6d69",
		"create_time": 1551755756,
		"dang_zid": 270,
		"id": 342,
		"is_allin": 0,
		"location": "\u8bf7\u95ee",
		"location_small": "",
		"locx": "",
		"locy": "",
		"removes": "",
		"schedule_id": "",
		"title": "\u8bf7\u95ee",
		"type": 2,
		"uid": 579,
		"yaoqiu": "\u6c1b\u56f4"
	}],
	"errmsg": "\u83b7\u53d6\u6570\u636e\u6210\u529f",
	"errno": "1",
	"total_page": 10
}
```

————————————————————————————————————————

### 首页轮播图文章展示

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/home/slider

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：无

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"create_time": 1469433395,
		"id": 62,
		"image": "http://pic.vchaoxi.com/2017-05-23_5924038eb9f8d.png",
		"item_id": 5552,
		"level": 1,
		"title": "\u9996\u98753"
	}, {
		"create_time": 1467879809,
		"id": 41,
		"image": "http://pic.vchaoxi.com/2017-05-23_5924039a7954e.png",
		"item_id": 5553,
		"level": 1,
		"title": "\u9996\u98752"
	}, {
		"create_time": 1467879794,
		"id": 40,
		"image": "http://pic.vchaoxi.com/2017-05-23_592403a483ec4.png",
		"item_id": 5550,
		"level": 1,
		"title": "\u9996\u98751"
	}],
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 党委工作计划列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/activity/plan_month

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：无

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"month": 4,
		"year": 2018
	}, {
		"month": 6,
		"year": 2017
	}, {
		"month": 5,
		"year": 2017
	}, {
		"month": 4,
		"year": 2017
	}],
	"errmsg": "\u67e5\u8be2\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 创建会议

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/activity/add_activity

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  begin_time  |      1552035900                  |
|   cate_1     |      支部党员大会                  |
|contact_mobile|      17625701390                 |
| contact_name |        刘浩                       |
| in_dang_zid  |        270                       |
| location     |      102会议室                    |
|   title      |        测试                       |
|   token      |  MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs|
|  type        |          1                       |
|  yaoqiu      |        正装                       |

返回值类型：  application/x-www-form-urlencoded

返回值示例：

```json
{
	"errmsg": "\u6dfb\u52a0\u4f1a\u8bae\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 获取当前会议参会人员列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/activity/inmembers

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       357                        |
|    token     | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"avatar": "http://oldpic.vchaoxi.com/2019-02-16_5c676b5330196.jpg",
		"truename": "\u5180\u626c\u8fea",
		"uid": 581
	}, {
		"avatar": "http://oldpic.vchaoxi.com/2019-01-23_5c47eee97b6d9.jpg",
		"truename": "\u590f\u57f9",
		"uid": 582
	}, {
		"avatar": "http://oldpic.vchaoxi.com/2019-02-21_5c6e639d3755f.jpg",
		"truename": "\u738b\u94ed\u5fc3",
		"uid": 584
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u5bd2\u54f2\u4e3d",
		"uid": 523
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u8868\u4e91\u98de",
		"uid": 524
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u67f3\u82e5\u5170",
		"uid": 525
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u4e1c\u591c\u6625",
		"uid": 526
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6bdb\u5f00\u8bda",
		"uid": 527
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u8303\u661f\u8fb0",
		"uid": 528
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u5409\u6653\u66fc",
		"uid": 529
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u4f9d\u4e00\u51e1",
		"uid": 530
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6d82\u96ea\u73cd",
		"uid": 531
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u67ef\u831c\u831c",
		"uid": 532
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6c5f\u82b3\u6da6",
		"uid": 533
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6d0b\u4e66\u6587",
		"uid": 534
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6c99\u590f\u67f3",
		"uid": 535
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u9646\u5bc4\u6587",
		"uid": 536
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6842\u767d\u98ce",
		"uid": 537
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u5df4\u5143\u9f99",
		"uid": 538
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u53f0\u601d\u806a",
		"uid": 539
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u767d\u5c71\u5f64",
		"uid": 540
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u7f57\u5c14\u4e91",
		"uid": 541
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u4f59\u4e39\u7434",
		"uid": 542
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u5ba3\u4e91\u98de",
		"uid": 543
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u5e38\u7ff0\u6d77",
		"uid": 544
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u96f7\u6620\u5929",
		"uid": 545
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u53f2\u4e39\u4e91",
		"uid": 546
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6b66\u624d\u54f2",
		"uid": 547
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u9648\u4e39\u7434",
		"uid": 548
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u6d2a\u4f1f\u535a",
		"uid": 549
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u626c\u98de\u5170",
		"uid": 550
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u8d1d\u82b8\u82b8",
		"uid": 551
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u817e\u73b2\u73b2",
		"uid": 552
	}, {
		"avatar": "http://pic-old.vchaoxi.com/2017-05-26_5927da1fb40ed.",
		"truename": "\u5e38\u5b50\u660e",
		"uid": 563
	}, {
		"avatar": "http://pic-old.vchaoxi.com/2017-05-26_5927e118afc27.",
		"truename": "\u4e91\u83f2",
		"uid": 564
	}, {
		"avatar": "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
		"truename": "\u674e\u91d1\u8d85",
		"uid": 565
	}, {
		"avatar": "http://pic-old.vchaoxi.com/2017-06-01_592fd99f8fd0f.jpg",
		"truename": "\u5a04\u5ef6\u98de",
		"uid": 569
	}, {
		"avatar": "http://oldpic.vchaoxi.com/2019-02-23_5c70b148beacf.jpg",
		"truename": "\u738b\u6657",
		"uid": 604
	}, {
		"avatar": "http://oldpic.vchaoxi.com/FhFqadQQVr6Q9pz-uaAKz2YTIIJL",
		"truename": "\u5c24\u660e",
		"uid": 625
	}, {
		"avatar": "http://oldpic.vchaoxi.com/2019-02-25_5c737f54b834c.",
		"truename": "\u59dc\u6b22",
		"uid": 629
	}, {
		"avatar": "http://oldpic.vchaoxi.com/FmMgF64R54C9ouc3VtvN-7eLkDom",
		"truename": "\u59dc\u6b22",
		"uid": 630
	}, {
		"avatar": "http://oldpic.vchaoxi.com/2019-02-28_5c778f03dc256.",
		"truename": "\u8def\u897f",
		"uid": 632
	}, {
		"avatar": "http://oldpic.vchaoxi.com/Fh4MEbGREf-6SllqZC7-9uOTaPa0",
		"truename": "\u5218\u6d69",
		"uid": 634
	}],
	"errmsg": "\u67e5\u8be2\u6210\u529f",
	"errno": "1"
}
```
——————————————————————————————————————

### 会议签到

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/activity/signin

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       357                        |
|    token     | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u7b7e\u5230\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 全体人员会议签到状态

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/activity/signed

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       357                        |
|    token     | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"act_id": 357,
		"create_time": 1552035275,
		"id": 90,
		"uid": 634
	}],
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————

### 会议打分

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.122:5000/api/v1_0/score/activity_grade

请求类型：POST

请求参数类型：multipart/form-data

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       357                        |
|   reason     |       签到                        |
|   score      |        2                         |
|   token      | MBkxvSBW7fq8jv73RuihuauA4Pu4YBAs |
|    uid       |       631                        |
|   img        |      签到人员头像的二进制文件        |

返回值类型： application/json

返回值示例：

```json
{
	"errmsg": "\u6253\u5206\u6210\u529f",
	"errno": "1"
}
```
——————————————————————————————————————————————————————

## 党员积分
### 接口简介1：党员积分列表
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/score/dang/members
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
|dang_zid | 270|
|token	|u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q|
返回值类型：
application/json
返回值示例：

```json
{
  "data": [
    {
      "id": 57, 
      "members": [
        {
          "avatar": "http://oldpic.vchaoxi.com/2019-02-16_5c676b5330196.jpg", 
          "is_cyjf": 1, 
          "mobile": "13729923564", 
          "total_score": 0, 
          "truename": "\u5180\u626c\u8fea", 
          "uid": 581, 
          "ydinfo": {
            "cdate": "201903", 
            "score": 7.0, 
            "status": 0
          }
        }, 
        {
          "avatar": "http://oldpic.vchaoxi.com/2019-01-23_5c47eee97b6d9.jpg", 
          "is_cyjf": 1, 
          "mobile": "17558829660", 
          "total_score": 0, 
          "truename": "\u590f\u57f9", 
          "uid": 582
        }, 
        {
          "avatar": "http://oldpic.vchaoxi.com/2019-02-28_5c778f03dc256.", 
          "is_cyjf": 1, 
          "mobile": "18530071352", 
          "total_score": 23.0, 
          "truename": "\u8def\u897f", 
          "uid": 632, 
          "ydinfo": {
            "cdate": "201903", 
            "score": 23.0, 
            "status": 1
          }
        }
      ], 
      "name": "\u8f6f\u4ef6\u6d4b\u8bd5"
    }
  ], 
  "errmsg": "\u67e5\u8be2\u6210\u529f", 
  "errno": "1"
}

```



### 接口简介2：党员积分-排行榜
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/score/ranklist
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
|  month	 |	3   |
| token	  | 	u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q  |
|  year	| 	2019  |
返回值类型：
application/json 
返回值示例：
```json
{
	"data": [{
		"total": 23.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/2019-02-28_5c778f03dc256.",
			"dang_gid": 57,
			"dang_level": 10,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 1,
			"mobile": "18530071352",
			"reg_time": 1551339267,
			"sex": 1,
			"status": 1,
			"truename": "\u8def\u897f",
			"uid": 632
		},
		"uid": 632
	}, {
		"total": 17.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/FmMgF64R54C9ouc3VtvN-7eLkDom",
			"dang_gid": 57,
			"dang_level": 10,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 0,
			"mobile": "15201187510",
			"reg_time": 1551074530,
			"sex": 1,
			"status": 1,
			"truename": "\u59dc\u6b22",
			"uid": 630
		},
		"uid": 630
	}, {
		"total": 12.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/2019-02-25_5c737f54b834c.",
			"dang_gid": 57,
			"dang_level": 20,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 0,
			"mobile": "18530071350",
			"reg_time": 1551073108,
			"sex": 1,
			"status": 1,
			"truename": "\u59dc\u6b22",
			"uid": 629
		},
		"uid": 629
	}],
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```
### 接口简介3：党员积分-排行榜-党支部列表
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/score/ranklist
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
| dang_zid	  | 	270  |
| month	  |	3   |
|  token	 | 	token	u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q  |
| year	  | 	2019  |
返回值类型：
application/json 
返回值示例：
```json
{
	"data": [{
		"total": 23.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/2019-02-28_5c778f03dc256.",
			"dang_gid": 57,
			"dang_level": 10,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 1,
			"mobile": "18530071352",
			"reg_time": 1551339267,
			"sex": 1,
			"status": 1,
			"truename": "\u8def\u897f",
			"uid": 632
		},
		"uid": 632
	}, {
		"total": 17.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/FmMgF64R54C9ouc3VtvN-7eLkDom",
			"dang_gid": 57,
			"dang_level": 10,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 0,
			"mobile": "15201187510",
			"reg_time": 1551074530,
			"sex": 1,
			"status": 1,
			"truename": "\u59dc\u6b22",
			"uid": 630
		},
		"uid": 630
	}, {
		"total": 12.0,
		"uInfo": {
			"avatar": "http://oldpic.vchaoxi.com/2019-02-25_5c737f54b834c.",
			"dang_gid": 57,
			"dang_level": 20,
			"dang_zid": 270,
			"is_cyjf": 1,
			"is_dabwy": 0,
			"is_djgly": 0,
			"mobile": "18530071350",
			"reg_time": 1551073108,
			"sex": 1,
			"status": 1,
			"truename": "\u59dc\u6b22",
			"uid": 629
		},
		"uid": 629
	}],
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```

### 接口简介4：党员积分-积分审核
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/score/dang/members
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
| dang_zid	  | 	270  |
| token	  |	u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q   |


返回值类型：
application/json 
返回值示例：
```python
{
	"data": [{
		"id": 57,
		"members": [{
			"avatar": "http://oldpic.vchaoxi.com/2019-02-16_5c676b5330196.jpg",
			"is_cyjf": 1,
			"mobile": "13729923564",
			"total_score": 0,
			"truename": "\u5180\u626c\u8fea",
			"uid": 581,
			"ydinfo": {
				"cdate": "201903",
				"score": 7.0,
				"status": 0
			}
		}, {
			"avatar": "http://oldpic.vchaoxi.com/2019-01-23_5c47eee97b6d9.jpg",
			"is_cyjf": 1,
			"mobile": "17558829660",
			"total_score": 0,
			"truename": "\u590f\u57f9",
			"uid": 582
		}, {
			"avatar": "http://oldpic.vchaoxi.com/2019-02-21_5c6e639d3755f.jpg",
			"is_cyjf": 1,
			"mobile": "15516155491",
			"total_score": 0,
			"truename": "\u738b\u94ed\u5fc3",
			"uid": 584
		},  {
			"avatar": "http://oldpic.vchaoxi.com/Fh4MEbGREf-6SllqZC7-9uOTaPa0",
			"is_cyjf": 1,
			"mobile": "17625701390",
			"total_score": 0,
			"truename": "\u5218\u6d69",
			"uid": 634
		}],
		"name": "\u8f6f\u4ef6\u6d4b\u8bd5"
	}],
	"errmsg": "\u67e5\u8be2\u6210\u529f",
	"errno": "1"
}
```

——————————————————————————————————————————————————————

## 学习教育
### 接口简介1：学习教育-他山之石主页面
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/document/doc_list
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
| page	  | 1 |
| token  | u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q  |
|  type |  1 |
返回值类型：
application/json 
返回值示例：
```json
{
    "current_page": 1,
    "data": [
        {
            "cover": "http://192.168.5.117:5000/static/images/icon80@2x.png?imageMogr2/thumbnail/220x130!",
            "create_time": 1495762879,
            "description": "暂无描述",
            "id": 6437,
            "title": "“迎接十九大 做合格党员” 征文启事"
        },
        {
            "cover": "http://192.168.5.117:5000/static/images/icon80@2x.png?imageMogr2/thumbnail/220x130!",
            "create_time": 1495762819,
            "description": "暂无描述",
            "id": 6436,
            "title": "“供给侧结构性改革”故事应该这样讲"
        }
    ],
    "errmsg": "查询成功",
    "errno": "1",
    "total_page": 1
}
```
### 接口简介2：学习教育-风采展示
维护人员：王晗
请求地址：
http://192.168.5.122:5000/api/v1_0/document/doc_list
请求类型：
POST
请求参数类型：
application/x-www-form-urlencoded
请求参数：
|   参数名   |参考值|
| :-------- | --------:| :--: |
| page	  | 1 |
| token  | u060FoiN5yxBEeSzwUNoTS9FG3ggN94Q  |
|  type |  2 |
返回值类型：
application/json 
返回值示例：
```json
{
    "current_page": 1,
    "data": [
        {
            "cover": "http://192.168.5.117:5000/static/images/icon80@2x.png?imageMogr2/thumbnail/220x130!",
            "create_time": 1546909050,
            "description": "ddd",
            "id": 6440,
            "title": "今天天气不错"
        }
    ],
    "errmsg": "查询成功",
    "errno": "1",
    "total_page": 1
}
```
——————————————————————————————————————————————————————


## 我 - 模块

### 我的会议、我的活动

维护人员：刘浩

接口详情：会议和活动只有一个参数不一样

请求地址：http://192.168.5.127:5000/api/v1_0/activity/activity_list

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
| is_mycreate  |         1                        |
|   page       |         1                        |
|   token      | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |
|   type       |         1                        |

返回值类型：application/json

返回值示例：

```json
{
	"current_page": 1,
	"data": [{
		"begin_time": 1552035900,
		"cate_1": "\u652f\u90e8\u515a\u5458\u5927\u4f1a",
		"cate_2": "",
		"cate_2_son": "",
		"contact_mobile": "17625701390",
		"contact_name": "\u5218\u6d69",
		"create_time": 1552032429,
		"dang_zid": 270,
		"id": 357,
		"is_allin": 0,
		"location": "102\u4f1a\u8bae\u5ba4",
		"location_small": "",
		"locx": "",
		"locy": "",
		"removes": "",
		"schedule_id": "",
		"title": "\u6d4b\u8bd5",
		"type": 1,
		"uid": 634,
		"yaoqiu": "\u6b63\u88c5"
	}],
	"errmsg": "\u83b7\u53d6\u6570\u636e\u6210\u529f",
	"errno": "1",
	"total_page": 1
}
```

——————————————————————————————————————————————————————

### 追加参会人员

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/activity/addtomember

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|    act_id    |        360                       |
|   token      | YO9enbbitaTTB3vjzcNo7q6pvUkZq5hn |
|   uids       |        540                       |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u8ffd\u52a0\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————————————————

### 删除参会人员

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/activity/removemember

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       360                        |
|    token     | YO9enbbitaTTB3vjzcNo7q6pvUkZq5hn |
|    uids      |       551                        |

返回值类型：application/json

返回值示例：

```json

{
	"errmsg": "\u5220\u9664\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————————————————

### 党员个人资料

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/profile_detail

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  token       | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"avatar": "http://oldpic.vchaoxi.com/Fh4MEbGREf-6SllqZC7-9uOTaPa0",
		"dang_gid": 57,
		"dang_jointime": "2019-03-08",
		"dang_level": 50,
		"dang_zid": 270,
		"email": "",
		"is_cyjf": 1,
		"is_djgly": 0,
		"is_dzbwy": 0,
		"jiguan": "\u90d1\u5dde",
		"last_active_time": 1552015594,
		"last_login_ip": 0,
		"last_login_time": 0,
		"login": 0,
		"mingzu": "\u6c49",
		"mobile": "17625701390",
		"nickname": "\u5218\u6d69",
		"reg_ip": 192168,
		"reg_time": 1552015594,
		"sex": 1,
		"status": 1,
		"truename": "\u5218\u6d69",
		"type": 1,
		"uid": 634,
		"work_date": "2019-03-08",
		"work_gangwei": "\u6d4b\u8bd5",
		"work_xueli": "\u672c\u79d1",
		"work_zhicheng": "\u6d4b\u8bd5\u5de5\u7a0b\u5e08",
		"zu_title": "\u8f6f\u4ef6\u6d4b\u8bd5"
	},
	"errmsg": "\u67e5\u8be2\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 党员个人积分详情

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/myscore_info

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  token       | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"data": {
		"is_signed": 1,
		"rank": 6,
		"score": 0.5,
		"signin_days": 1
	},
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```

 ——————————————————————————————————————————————————————
 
### 我的荣誉列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/myhonor

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|     page     |         1                        |
|   token      | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |
 
返回值类型：application/json

返回值示例：

```json
{
	"current_page": 1,
	"data": [{
		"audit_time": 0,
		"audit_uid": 635,
		"beizhu": "\u4e0a\u4f20\u8d44\u6599",
		"create_time": 1552112445,
		"id": 128,
		"jigou_title": "",
		"level": "\u9ad8\u7ea7\u804c\u79f0",
		"pics": [
			"http://oldpic.vchaoxi.com/FoO-seQDBfypCeETBR0FeF8AfPwI"],
		"status": 0,
		"title": "\u9ad8\u7ea7\u804c\u79f0",
		"type": "\u804c\u79f0",
		"uid": 634
	}],
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1",
	"total_page": 1
}
```
———————————————————————————————————————————————————————

### 签到

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/day_signin

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  token       | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u7b7e\u5230\u6210\u529f",
	"errno": "1"
}
```
——————————————————————————————————————————————————————

### 全体党员列表

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/activity/members_list

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  token       | YO9enbbitaTTB3vjzcNo7q6pvUkZq5hn |

返回值类型：application/json

返回值示例：

```json
{
	"data": [{
		"dang_zid": 0,
		"is_cyjf": 0,
		"truename": "",
		"uid": 1
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u8def\u5a1f",
		"uid": 580
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5180\u626c\u8fea",
		"uid": 581
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u590f\u57f9",
		"uid": 582
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u738b\u94ed\u5fc3",
		"uid": 584
	}, {
		"dang_zid": 260,
		"is_cyjf": 1,
		"truename": "\u5b63\u4f1f",
		"uid": 585
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u5218\u777f\u6377",
		"uid": 586
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u738b\u52c3\u7131",
		"uid": 587
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5bd2\u54f2\u4e3d",
		"uid": 523
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u8868\u4e91\u98de",
		"uid": 524
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u67f3\u82e5\u5170",
		"uid": 525
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u4e1c\u591c\u6625",
		"uid": 526
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6bdb\u5f00\u8bda",
		"uid": 527
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u8303\u661f\u8fb0",
		"uid": 528
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5409\u6653\u66fc",
		"uid": 529
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u4f9d\u4e00\u51e1",
		"uid": 530
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6d82\u96ea\u73cd",
		"uid": 531
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u67ef\u831c\u831c",
		"uid": 532
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6c5f\u82b3\u6da6",
		"uid": 533
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6d0b\u4e66\u6587",
		"uid": 534
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6c99\u590f\u67f3",
		"uid": 535
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u9646\u5bc4\u6587",
		"uid": 536
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6842\u767d\u98ce",
		"uid": 537
	}, {
		"dang_zid": 270,
		"is_cyjf": 0,
		"truename": "\u5df4\u5143\u9f99",
		"uid": 538
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u53f0\u601d\u806a",
		"uid": 539
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u767d\u5c71\u5f64",
		"uid": 540
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u7f57\u5c14\u4e91",
		"uid": 541
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u4f59\u4e39\u7434",
		"uid": 542
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5ba3\u4e91\u98de",
		"uid": 543
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5e38\u7ff0\u6d77",
		"uid": 544
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u96f7\u6620\u5929",
		"uid": 545
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u53f2\u4e39\u4e91",
		"uid": 546
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6b66\u624d\u54f2",
		"uid": 547
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u9648\u4e39\u7434",
		"uid": 548
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u6d2a\u4f1f\u535a",
		"uid": 549
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u626c\u98de\u5170",
		"uid": 550
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u8d1d\u82b8\u82b8",
		"uid": 551
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u817e\u73b2\u73b2",
		"uid": 552
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u5f20\u6c38\u5b89",
		"uid": 591
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u5f20\u857e",
		"uid": 574
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u6768\u68e3",
		"uid": 575
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u9ec4\u6653\u7ea2",
		"uid": 576
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5e38\u5b50\u660e",
		"uid": 563
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u90ed\u94f6\u82b3",
		"uid": 577
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u4e91\u83f2",
		"uid": 564
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u674e\u91d1\u8d85",
		"uid": 565
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u5415\u82b3\u5b81",
		"uid": 589
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u8521\u76fc",
		"uid": 578
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5a04\u5ef6\u98de",
		"uid": 569
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u5f20\u660e",
		"uid": 592
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u8bb8\u65f8",
		"uid": 590
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u738b\u6657",
		"uid": 604
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u5434\u5c0f\u83b9",
		"uid": 588
	}, {
		"dang_zid": 210,
		"is_cyjf": 1,
		"truename": "\u767d\u4e07\u8363",
		"uid": 573
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u738b\u7434\u82b3",
		"uid": 593
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u5218\u5c0f\u971e",
		"uid": 594
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u6731\u5c0f\u9f99",
		"uid": 595
	}, {
		"dang_zid": 90,
		"is_cyjf": 1,
		"truename": "\u674e\u957f\u6d77",
		"uid": 596
	}, {
		"dang_zid": 250,
		"is_cyjf": 1,
		"truename": "\u674e\u4e66\u8bb0",
		"uid": 597
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5c24\u660e",
		"uid": 625
	}, {
		"dang_zid": 200,
		"is_cyjf": 1,
		"truename": "\u59dc\u6b22",
		"uid": 633
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u59dc\u6b22",
		"uid": 629
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u59dc\u6b22",
		"uid": 630
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u8def\u897f",
		"uid": 632
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u5218\u6d69",
		"uid": 634
	}, {
		"dang_zid": 270,
		"is_cyjf": 1,
		"truename": "\u590f\u5929",
		"uid": 635
	}],
	"errmsg": "\u67e5\u8be2\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————————————————

### 会议请假申请

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/activity/leave_request

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  token       | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |
|  act_id      |        360                       |
| reason       |     不知道                        |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u7533\u8bf7\u6210\u529f",
	"errno": "1"
}
```
——————————————————————————————————————————————————-———

### 会议请假审批

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/activity/leave_approve

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   act_id     |       360                        |
|  status      |        2                         |
|  token       | YO9enbbitaTTB3vjzcNo7q6pvUkZq5hn |
|  uid         |        631                       |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u5ba1\u6279\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————————————————

### 添加荣誉

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/add_honor

请求类型：POST

请求参数类型：multipart/form-data

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|  beizhu      |       上传资料                    |
|  level       |      高级职称                     |
|  title       |      高级职称                     |
|  token       | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |
|  type        |       职称                       |
|  img[]       |     资料的二进制文件                |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u6dfb\u52a0\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 审核提交荣誉

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/audit_honor_operation

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   honor_id   |        128                       |
|    score     |       7                          |
|   status     |        1                         |       
|   token      | YO9enbbitaTTB3vjzcNo7q6pvUkZq5hn |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u64cd\u4f5c\u6210\u529f",
	"errno": "1"
}
```
———————————————————————————————————————————————————————

### 修改密码

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/change_password

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   old_pw     |       123456                     |
|  replace_pw  |      098765                      |
|   token      | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u4fee\u6539\u6210\u529f",
	"errno": "1"
}
```
————————————————————————————————————————————————-——————

### 修改手机号

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/change_mobile

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
| mobile       |     17748656010                  |
| token        | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u4fee\u6539\u6210\u529f",
	"errno": "1"
}
```

————————————————————————————————————————————————————

### 使用帮助

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/help_document

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
|   type       |       ios                        |

返回值类型：application/json

返回值示例：

```json
{
	"data": "http://elec.vchaoxi.com/ios_read.html",
	"errmsg": "\u83b7\u53d6\u6210\u529f",
	"errno": "1"
}
```
——————————————————————————————————————————————————————

### 退出登录

维护人员：刘浩

接口详情：

请求地址：http://192.168.5.127:5000/api/v1_0/user/logout

请求类型：POST

请求参数类型：application/x-www-form-urlencoded

请求参数：

|     参数名    |        参考值                     |
| :-----------:|      :-------:                   |
| token        | en3y7vQ1SaeHZ/TOw3Mj0vfqE8HPsgEH |

返回值类型：application/json

返回值示例：

```json
{
	"errmsg": "\u9000\u51fa\u767b\u5f55\u6210\u529f",
	"errno": "1"
}
```


