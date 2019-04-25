<template>
  <div class="banner">
    <a-row>
      <a-col :span="3"></a-col>
      <a-col :span="14">
        <div class="search">
          <router-link to="/" tag="div" class="title">Just Movie</router-link>
          <div class="search-input">
            <div class="form-group">
              <a-input placeholder="搜索 ..." style="width: 400px" @keyup.enter="searchMovie" v-model="movieText"/>
              <a-button type="primary" icon="close" v-show="moviesList.length > 0" class="search-button" @click="cancelSearch">取消搜索</a-button>
            </div>
            <ul class="search-list" v-show="moviesList.length > 0">
              <li @click.prevent.stop="clearSearch(index)" v-for="(movie, index) in moviesList" :key="movie.id">
                <search-list-movie-item :movie="movie"></search-list-movie-item>
              </li>
            </ul>
          </div>
        </div>
      </a-col>

      <a-menu mode="horizontal" class="navigation">
        <a-menu-item>
          <a href="/"><a-icon type="home" />首页</a>
        </a-menu-item>
        <a-menu-item>
          <a href="/category"><a-icon type="tag" />分类</a>
        </a-menu-item>
      </a-menu>
    </a-row>
  </div>
</template>

<script>
  import { getMovieSearch } from '../utils.js'
  import SearchListMovieItem from './SearchListMovieItem.vue'
  export default {
    name: 'Banner',
    components: {
      SearchListMovieItem
    },
    data() {
      return {
        movieText: '',
        moviesList: [],
        moviesListTop5: []
      }
    },
    methods: {
      searchMovie() {
        if (this.movieText.length === 0) {
          this.$message.error('搜索内容不能为空')
          return
        }
        this.getMovieBySearch(this.movieText)
      },
      cancelSearch() {
        this.movieText = ''
        this.moviesList = []
      },
      clearSearch(index) {
        let id = this.moviesList[index]._id
        this.movieText = ''
        this.moviesList = []
        this.$router.push({
          name: 'MovieDetail',
          replace: true,
          params: {
            id: id
          }
        })
        this.$router.go()
      },
      getMovieBySearch(movieText) {
        getMovieSearch(movieText).then(res => {
          this.moviesList = res
          if (this.moviesList.length === 0) {
            this.$message.error('无搜索结果')
            this.movieText = ''
          }
        })
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .banner
    .search
      display flex;
      padding 25px 0
      align-items center
      .title
        font-size 30px
        line-height 45px
        font-weight 700
        cursor pointer
      .search-input
        margin-left 20px
        .search-list
          position absolute
          background-color #fff
          width 400px;
          z-index 999
          border 1px solid #ccc
          max-height 500px
          overflow auto
    .navigation
      font-size 16px
      padding 25px 0
</style>
