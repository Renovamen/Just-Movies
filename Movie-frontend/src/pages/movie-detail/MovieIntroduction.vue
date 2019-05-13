<template>
  <div class="movie-introduction">
    <a-row>
      <a-col :span="8">
        <div class="poster-wrapper">
          <img class="poster" :src="movie.poster" alt="" :onerror="noImg">
        </div>
      </a-col>
      <a-col :span="16">
        <div class="introduction">
          <div class="item">
            <span class="item-key">导演: </span>
            <span class="item-value" v-for="director in movie.directors" :key="director.id">{{ director.name }}</span>
          </div>
          <div class="item">
            <span class="item-key">编剧: </span>
            <span class="item-value" v-for="writer in movie.writers" :key="writer.id">{{ writer.name }}</span>
          </div>
          <div class="item">
            <span class="item-key">主演: </span>
            <span class="item-value" v-for="cast in movie.casts" :key="cast.id">{{ cast.name }}</span>
          </div>
          <div class="item">
            <span class="item-key">类型: </span>
            <span class="item-value" v-for="gen in movie.genres" :key="gen">{{ gen }}</span>
          </div>
          <div class="item">
            <span class="item-key">国家: </span>
            <span class="item-value" v-for="cou in movie.countries" :key="cou">{{ cou }}</span>
          </div>
          <div class="info">
            <span class="info-key">语言: </span>
            <span class="info-value">{{ movie.languages.join(' / ') }}</span>
          </div>
          <div class="info">
            <span class="info-key">上映时间: </span>
            <span class="info-value">{{ movie.pubdate.join(' / ') }}</span>
          </div>
          <div class="info">
            <span class="info-key">片长: </span>
            <span class="info-value">{{ movie.duration}}</span>
          </div>
          <div class="info">
            <span class="info-key">又名: </span>
            <span class="info-value">{{ movie.aka.join(' / ') }}</span>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  export default {
    name: 'MovieIntroduction',
    props: {
      movie: {
        type: Object,
        default: {}
      },
    },
    data() {
      return {
        noImg: 'this.src="' + require('../../../static/no-img.jpeg') + '"',
      }
    },
    methods: {
      concatPub(pubdates) {
        return Util.concatPubdates(pubdates, ' / ')
      },
      concatAli(alias) {
        return Util.concatAlias(alias, ' / ')
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .movie-introduction
    .poster-wrapper
      width 100%
      .poster
        width 90%
        border-radius 5%
    .introduction
      font-size 13px
      padding-right 15px
      .item
        margin-bottom 5px
        .item-key
          color #686868
        .item-value
          padding 0 5px
      .info
        margin-bottom 5px
        .info-key
          color #686868
        .info-value
          padding 0 5px
</style>