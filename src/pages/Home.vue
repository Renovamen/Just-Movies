<template>
  <div class="home">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="20">
        <div class="movie-carousel">
          <!-- ------------------------- 第一行 ------------------------ -->
          <div class="carousel" ref="carousel" v-if="firstRender">
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in MovieList.slice(0, 5)" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="">
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

          <div class="carousel" ref="carousel" v-else>
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in carouselItemUp" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="">
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
          <div class="carousel" ref="carousel" v-if="firstRender">
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in MovieList.slice(5, 10)" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="">
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

          <div class="carousel" ref="carousel" v-else>
            <router-link tag="div" :to="{ name: 'MovieDetail', params: {id: item._id} }" class="item" style="width: 18%" v-for="item in carouselItemDown" :key="item.id">
              <img class="image" v-bind:src="item.poster" :key="item.poster" alt="">
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

          <div class="button">
            <span class="pagination">{{ carouselIndex }} / {{ carouselCount }}</span>
            <a-button type="primary" @click="onPrevious"><a-icon type="left" /></a-button>
            <a-button type="primary" @click="onNext"><a-icon type="right" /></a-button>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  import { getMovieList, getMovieDetail } from '../utils'
  import axios from 'axios'
  export default {
    name: 'Home',
    data() {
      return {
        MovieList: [],
        carouselIndex: 1,
        carouselItemUp: [],
        carouselItemDown: [],
        firstRender: true
      }
    },
    created() {
      // 获取电影列表
      getMovieList().then(res => {
        this.MovieList = res
        //console.log("MoviesList", this.MovieList)
      })
    },
    computed: {
      carouselCount() {
        return Math.floor(this.MovieList.length / 10)
      }
    },
    methods: {
      onPrevious() {
        this.carouselIndex--
          if (this.carouselIndex <= 0) {
            this.carouselIndex = this.carouselCount
          }
          this.getCarouselItem(this.carouselIndex)
      },
      onNext() {
        this.carouselIndex++
          if (this.carouselIndex > this.carouselCount) {
            this.carouselIndex = 1
          }
          this.getCarouselItem(this.carouselIndex)
      },
      getCarouselItem(index) {
        // --------------- 第一行 ---------------
        let start = 10 * (index - 1)
        let end = 10 * index - 6
        let tempArr = []
        this.firstRender = false
        for (let i = start; i <= end; i++) {
          tempArr.push(this.MovieList[i])
        }
        this.carouselItemUp = tempArr

        // --------------- 第二行 ---------------
        start = 10 * index - 5
        end = 10 * index  - 1
        tempArr = []
        this.firstRender = false
        for (let i = start; i <= end; i++) {
          tempArr.push(this.MovieList[i])
        }
        this.carouselItemDown = tempArr
      }
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
    .button    
      float right 
      margin-right 10px
      margin-top 20px
      margin-bottom 20px
      .pagination
        font-size 14px
        margin-right 20px
</style>