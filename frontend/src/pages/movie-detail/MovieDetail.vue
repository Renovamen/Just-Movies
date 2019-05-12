<template>
  <div class="movie-detail">
    <a-row>
      <a-col :span="4"></a-col>
      <a-col :span="16">
        <div class="movie-detail-wrapper">
          <h1 class="title">
            {{ movie.title }}
            <span class="year">({{ movie.year }})</span>
          </h1>
          <a-row>
            <a-col :span="17">
              <movie-introduction :movie="movie"></movie-introduction>
            </a-col>
            <a-col :span="7">
              <movie-rate :movie="movie"></movie-rate>
            </a-col>
          </a-row>
          <div class="movie-brief">
            <h2 class="title">剧情简介</h2>
            <div class="summary">{{ movie.summary }}</div>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
  import MovieRate from './MovieRate.vue'
  import MovieIntroduction from './MovieIntroduction.vue'

  export default {
    name: 'MovieDetail',
    data() {
      return {
        movie: {},
      }
    },
    components: {
      MovieRate,
      MovieIntroduction
    },
    created() {
      this.getData()
    },
    activated() {
      this.getData()
    },
    computed: {
      movieID() {
        return this.$route.params.id 
      }
    },
    methods: {
      getData() {
        this.movie = {}
        let id = this.movieID
        /*
        getMovieDetail(id).then(res => {
          this.movie = res
          //console.log("MovieDetail: ", this.movie)
        })
        */
        this.$http.get('getMovie/' + id).then(res => {
          this.movie = res.data
          this.movie.rating_stars = [this.movie.stars5, this.movie.stars4, this.movie.stars3, this.movie.stars2, this.movie.stars1]
        })
        .catch(err => {
          console.log("MovieDetail Get 'getMovie/:id/' Error: ", err)
        })
      }
    },
  }
</script>

<style lang="stylus" scoped>
  .movie-detail
    margin-bottom 40px
    .title
      margin-top 30px
      font-size 30px
      color #494949
      .year
        color #888
    .movie-brief
      margin-top 50px
      .title
        font-size 18px
        color #087626
        margin 20px 0 15px
      .summary
        font-size 13px
</style>