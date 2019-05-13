<template>
  <div class="category-page">
    <a-row>
      <a-col :span="4"></a-col>
      <a-col :span="16">
        <ul class="tags">
          <li @click="selectTag_Gen(index)" class="tag" :class="{ active: index === activeIndex_gen }" v-for="(category_gen, index) in category_genres" :key="category_gen">{{ category_gen }}</li>
        </ul>
        <ul class="tags">
          <li @click="selectTag_Cou(index)" class="tag" :class="{ active: index === activeIndex_cou }" v-for="(category_cou, index) in category_countries" :key="category_cou">{{ category_cou }}</li>
        </ul>
        <ul class="movie-list">
          <router-link tag="li" :to="{ name: 'MovieDetail', params: {id: movie._id} }" class="movie-item" v-for="movie in movies" :key="movie._id">
            <movie-list-item>
              <img v-bind:src="movie.poster" alt="" class="image" slot="thumbnail" :onerror="noImg">
              <div class="title" slot="title">{{ movie.title }}</div>
              <div class="info" slot="info">{{ movie.pubdate.join(' / ') }}</div>
              <div class="rate" slot="rate" v-if="movie.rating.average">
                <a-rate :defaultValue="movie.rating.average/2" allowHalf disabled/>
                <span class="average">{{ movie.rating.average }}</span> ({{ movie.rating.rating_people }}人评价)
              </div>
              <div class="rate" slot="rate" v-else>暂无评分</div>
            </movie-list-item>
          </router-link>
        </ul>
        <div class="pagination">
          <a-pagination showQuickJumper :defaultCurrent="1" :defaultPageSize="20"	:total="totalMovie" @change="changePage" />
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  import MovieListItem from '../components/MovieListItem.vue'

  export default {
    name: 'CategoryPage',
    components: {
      MovieListItem
    },
    data() {
      return {
        category_genres: [
          '全部类型', '剧情', '爱情', '喜剧', '科幻', '动作', '动画', '悬疑', 
          '犯罪', '同性', '惊悚', '恐怖', '音乐', '歌舞', '传记', '历史', 
          '战争', '西部', '奇幻', '冒险', '灾难', '武侠', '情色', '运动', '纪录片',
          '家庭', '短片', '黑色电影', '儿童', '古装', '戏曲',
        ],
        category_countries: [
          '全部地区', '中国大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', 
          '法国', '德国', '意大利', '西班牙', '阿根廷', '泰国', '俄罗斯', '伊朗', 
          '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦'
        ],
        tag_gen: '全部类型',
        tag_cou: '全部地区',
        movies: [],
        activeIndex_gen: 0,
        activeIndex_cou: 0,
        pageID: 1,
        totalMovie: 0,
        noImg: 'this.src="' + require('../../static/no-img.jpeg') + '"',
      }
    },
    created() {
      this.getMoviesByTag(this.tag_gen, this.tag_cou, this.pageID)
    },
    methods: {
      selectTag_Gen(index) {
        this.tag_gen = this.category_genres[index]
        this.movies = []
        this.activeIndex_gen = index
        this.getMoviesByTag(this.tag_gen, this.tag_cou, this.pageID)
      },
      selectTag_Cou(index) {
        this.tag_cou = this.category_countries[index]
        this.movies = []
        this.activeIndex_cou = index
        this.getMoviesByTag(this.tag_gen, this.tag_cou, this.pageID)
      },
      changePage(page_id){
        this.pageID = page_id
        this.getMoviesByTag(this.tag_gen, this.tag_cou, this.pageID)
      },
      getMoviesByTag(tag_gen, tag_cou, page_id) {
        this.$http.get('../../static/films.json').then(res => {
          
          let result = [], len = res.data.length
          for (var i = 0; i < len; i++)
          {
            let flag = 0
            for(let gen of res.data[i].genres)
            {
              if(gen == tag_gen || tag_gen == "全部类型")
              {
                for(let cou of res.data[i].countries)
                  if(cou == tag_cou || tag_cou == "全部地区") flag = 1
              }
            }
            if(flag == 1) result.push(res.data[i])
          }

          var page_size = 10
          var start = (page_id - 1) * page_size, end
          if(start + page_size >= res.data.length) end = res.data.length
          else end = start + page_size

          this.movies = result.slice(start, end)
          console.log(this.movies)
          this.totalMovie = result.length
        })
        .catch(err => {
          console.log("CategoryPage Get 'getCategory/:genre/:country' Error: ", err)
        })
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .category-page >>> .ant-rate
    color #e2952b
    font-size 12px
  .category-page
    .tags
      margin-top 20px
      display flex
      flex-flow wrap
      .tag
        font-size 14px
        color #333
        padding 2px 10px
        margin-bottom 5px
        cursor pointer
        transition all .3s
        &:hover
          color #108ee9
        &.active
          color #fff
          background-color #2a8ccb
          border-radius 3px
    .movie-list
      .movie-item
        padding 15px 10px
        border-top 1px dashed #ddd
        cursor pointer
        .title
          font-size 14px
          color #3576aa
          margin-bottom 5px
        .info
          color #666
          margin-bottom 5px
        .rate
          color #666
          .average
            color #e2952b
    .pagination  
      float right 
      margin-right 10px
      margin-top 20px
      margin-bottom 20px
</style>