<template>
  <div class="home">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="20">
        <div class="movie-carousel">
          <!-- ------------------------- 第一行 ------------------------ -->
          <div class="carousel" ref="carousel">
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in MovieList.slice(0, 5)" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="" :onerror="noImg">
              <!-- ----------- v-lazy 加载方式 ---------- -->
              <!-- <img class="image" v-lazy="item.poster" :key="item.poster" alt=""> -->
              <div class="content">
                <div class="title">{{ item.title }}</div>
                <div class="rate" v-if="item.rating.average">
                  {{ item.rating.average }}分
                </div>
                <div class="rate" v-else>暂无评分</div>
              </div>
            </router-link>
          </div>

          <!-- ------------------------- 第二行 ------------------------ -->
          <div class="carousel" ref="carousel">
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in MovieList.slice(5, 10)" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="" :onerror="noImg">
              <!-- <img class="image" v-lazy="item.poster" :key="item.poster" alt=""> -->
              <div class="content">
                <div class="title">{{ item.title }}</div>
                <div class="rate" v-if="item.rating.average">
                  {{ item.rating.average }}分
                </div>
                <div class="rate" v-else>暂无评分</div>
              </div>
            </router-link>
          </div>

          <div class="pagination">
            <a-pagination showQuickJumper :defaultCurrent="1" :total="totalMovie" @change="changePage" />
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        MovieList: [],
        totalMovie: 0,
        noImg: 'this.src="' + require('../../static/no-img.jpeg') + '"',
      }
    },
    created() {
      this.getMovielist("1")
    },
    computed: {
      carouselCount() {
        return Math.floor(this.totalMovie / 10)
      }
    },
    methods: {
      getMovielist(page_id){
        this.$http.get('../../static/films.json').then(res => {
          
          var page_size = 10
          var start = (page_id - 1) * page_size, end
          if(start + page_size >= res.data.length) end = res.data.length
          else end = start + page_size

          this.MovieList = res.data.slice(start, end)
          this.totalMovie = res.data.length
        })
        .catch(err => {
          console.log("Home Get 'getMovieList/' Error: ", err)
        })
      },
      changePage(page_id) {
        this.getMovielist(page_id)
      },
    },
  }
</script>

<style lang="stylus" scoped>
  .movie-carousel
    margin-bottom 40px

    .carousel
      width 100%
      display flex
      justify-content space-around
      margin-top 20px
      .item
        align-items stretch
        border 1px solid #ddd
        cursor pointer
        position relative
        display flex
        flex-direction column
        justify-content space-between
        overflow hidden
        padding-bottom 10px
        border-radius 5%
        .image
          min-width 100%
          max-width 100%
          min-height 185px
          padding 5px
          border-radius 5%
          transition all .5s
          &:hover
            transform scale(1.2)
            opacity 0.8
        .content
          z-index 10
          background-color #fff
          .title
            margin-top 10px
            width 100%
            text-align center
            font-size 12px
            overflow hidden
            white-space nowrap
            text-overflow ellipsis
            text-align center
          .rate
            font-size 12px
            text-align center
            font-weight 700
            color #f30
            margin-top 5px
    .pagination  
      float right 
      margin-right 10px
      margin-top 20px
      margin-bottom 20px
</style>