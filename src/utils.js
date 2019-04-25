import axios from 'axios'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.withCredentials = true

// 电影详情：从 films.json 中获取 _id = id 的电影详情
export function getMovieDetail(id) {
  return new Promise((resolve) => {
    axios.get('./static/films.json').then(res => {
      res = res.data
      let len = res.length
      for (var i = 0; i < len; i++)
        if(res[i]._id == id)
        {
          resolve(res[i])
          break
        }
    })
  })
}

// 首页：从 films.json 中读取电影列表
export function getMovieList() 
{
  return new Promise((resolve) => 
  {
    axios.get('./static/films.json').then(res => 
    {
      //console.log("Movielist: ", res.data)
      resolve(res.data)
    })
  })
}

// 分类：从 films.json 中读取符合 tag 的电影列表
export function getMovieTag(tag_gen, tag_cou) 
{
  return new Promise((resolve) => 
  {
    axios.get('./static/films.json').then(res => 
    {
      console.log(tag_gen, tag_cou)
      res = res.data
      let result = []
      let len = res.length
      for (var i = 0; i < len; i++)
      {
        let flag = 0
        for(let gen of res[i].genres)
        {
          if(gen == tag_gen || tag_gen == "全部类型")
          {
            for(let cou of res[i].countries)
              if(cou == tag_cou || tag_cou == "全部地区") flag = 1
          }
        }
        if(flag == 1) result.push(res[i])
      }
      //console.log("movie", result)
      //console.log("Movielist: ", res.data)
      resolve(result)
    })
  })
}

// 搜索：从 films.json 中读取符合搜索内容的电影列表（原名、别名）
export function getMovieSearch(text) 
{
  return new Promise((resolve) => 
  {
    axios.get('./static/films.json').then(res => 
    {
      res = res.data
      let result = []
      let len = res.length
      for (let movie of res)
      {
        // 电影名
        if(movie.title.search(text) != -1)result.push(movie)
        // 电影别名
        else
          for(let alias of movie.aka)
            if(alias.search(text) != -1)
            {
              result.push(movie)
              break
            }
      }
      console.log("movie", result)
      //console.log("Movielist: ", res.data)
      resolve(result)
    })
  })
}

function concatPubdates(pubdates, character) {
  if(pubdates[0] == '')return "暂无"
  return pubdates.join(character)
}

function concatAlias(alias, character) {
  if(alias[0] == '')return "暂无"
  return alias.join(character)
}

const Util = {
  concatPubdates,
  concatAlias,
}

export default Util