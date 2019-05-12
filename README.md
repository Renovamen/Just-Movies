# Just-Movies

Django + Vue 实现的电影站。



## Environment

- Vue 2.9.6
- Django 2.1.1
- Python 3.6.7



## Structure

```‘
├── backend
│   ├── Just_Movies
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── movies
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializer.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── json-to-database.py                  // 把 json 中的数据导入数据库
│   └── movies.sqlite3                       // 存储电影数据的数据库
│   ├── films_all.json                       // 存储电影数据的 json 文件
└── frontend
    ├── build
    ├── config
    ├── index.html
    ├── package.json
    ├── src
    │   ├── App.vue                          // 入口页面
    │   ├── components                       // 组件
    │   │   ├── Banner.vue                   // banner 组件
    │   │   ├── MovieListItem.vue            // 分类页电影列表中的每个电影
    │   │   └── SearchListMovieItem.vue      // 搜索栏下拉列表
    │   ├── main.js                          // 入口，加载组件、初始化等
    │   ├── pages                            // 页面
    │   │   ├── CategoryPage.vue             // 分类页
    │   │   ├── Home.vue                     // 首页
    │   │   └── movie-detail                 // 电影详情
    │   │       ├── MovieDetail.vue          // 详情页
    │   │       ├── MovieIntroduction.vue    // 介绍（导演、编剧、演员等）区域
    │   │       └── MovieRate.vue            // 评分区域
    │   └── router                           // 路由
    └── static                               // 静态文件（films.json等）
```





## Usage

### Frontend

```bash
git clone https://github.com/Renovamen/Just-Movies.git
cd /Just-Movies/frontend

# install dependencies
npm install

# serve with hot reload at 127.0.0.1:8080
npm run dev
```

浏览器访问 http://127.0.0.1:8080



### Backend

```bash
cd /Just-Movies/backend

python3 manage.py runserver 127.0.0.1:8000
```



## Requirments

### Frontend

- [Vue](https://github.com/vuejs/vue)
- [vue-router](https://github.com/vuejs/vue-router)：路由管理
- [axios](https://github.com/axios/axios)：请求数据
- [ant-design-vue](https://github.com/vueComponent/ant-design-vue)：UI 组件库
- [stylus](https://github.com/stylus/stylus)：CSS 预编译器



### Backend

- [Django](https://github.com/django/django)
- [Django REST framework](https://github.com/encode/django-rest-framework)：构建 Web API

- [django-cors-headers](https://github.com/ottoyiu/django-cors-headers)：跨域