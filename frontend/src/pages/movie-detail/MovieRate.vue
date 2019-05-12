<template>
  <div class="movie-rate">
    <div class="rate">评分</div>
    <div class="score-wrapper">
      <div class="score">{{ movie.rating_average }}</div>
      <div class="star-comments">
        <div class="star">
          <a-rate :defaultValue="movie.rating_average/2" allowHalf disabled/>
        </div>
        <div class="comments">
          已有{{ movie.rating_people }}人评价
        </div>
      </div>
    </div>
    <ul class="rating-bar-list">
      <li class="rating-bar" v-for="(score, index) in movie.rating_stars" :key="index">
        <div class="index">{{ 5 - index }}星</div>
        <div class="bar" :style="{width: Percent(score, movie.rating_stars) + '%'}"></div>
        <div class="percent">{{ Percent(score, movie.rating_stars) }}%</div>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'MovieRate',
    props: {
      movie: {
        type: Object,
        default: {}
      },
    },
    methods: {
      Total(details) {
        let total = 0
        for (let key in details)total += parseInt(details[key])
        return total
      },
      Percent(score, details) {
        return (score / this.Total(details) * 100).toFixed(1)
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .movie-rate >>> .ant-rate
    color #e2952b
    font-size 12px

  .movie-rate
    border-left 1px solid #eaeaea
    padding-left 20px
    .rate
      font-size 16px
      color #a5a5a5
    .score-wrapper
      display flex
      justify-content flex-start
      .score
        font-size 24px
        color #494949
        font-weight bolder
        margin 0 10px 0 0
        vertical-align center
      .star-comments
        .comments
          font-size 12px
    .rating-bar-list
      margin-top 10px
      .rating-bar
        display flex
        justify-content flex-start
        font-size 12px
        color #a5a5a5
        .index
          flex 0 0 20px
        .bar
          height 10px
          background-color #fed69a 
          vertical-align bottom
          margin 0 10px 0 10px
          position relative
          top 3px
</style>