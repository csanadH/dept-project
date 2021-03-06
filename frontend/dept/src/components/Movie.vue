<template>
<section class="movie section">
    <div v-if="contentLoaded === true" class="row mov">
        <span class="image">
          <img v-if="movie.Poster != 'N/A'" :src="movie.Poster" />
          <img v-if="movie.Poster == 'N/A'" src="../assets/na.jpg" />
        </span>
        <span id="info">
            <table>
                <tr>
                    <th colSpan="4"><span id="title">{{movie.Title}}</span><br>
                    <span id="released">{{ movie.Released }}</span></th>
                </tr>
                <tr>
                    <td colSpan="2" class="key">Runtime:</td>
                    <td colSpan="2" class="value">{{ movie.Runtime }}</td>
                </tr>
                <tr>
                    <td colSpan="2" class="key">Genre:</td>
                    <td colSpan="2" class="value">{{ movie.Genre }}</td>
                </tr>
                <tr>
                    <td colSpan="2" class="key">Director:</td>
                    <td colSpan="2" class="value">{{ movie.Director }}</td>
                </tr>
                <tr>
                    <td colSpan="2" class="key">Actors:</td>
                    <td colSpan="2" class="value">{{ movie.Actors }}</td>
                </tr>
                <tr>
                    <td colSpan="4" class="plot">
                        {{ movie.Plot }}
                    </td>
                </tr>
                <tr v-if="rated">
                    <td class="rating" v-for="rating of movie.Ratings" :key="rating.Value">
                        {{ rating.Source }}<br>{{ rating.Value }}
                    </td>
                    <td class="overall">
                        Overall<br>
                        {{ overall }}%
                    </td>
                </tr>
            </table>
        </span>
        <div class="button-wrap">
            <i class="fas fa-chevron-left" v-on:click="onBack" id="back"></i>
            <button class="btn btn-outline-primary"
            v-on:click="showTrailer = true">WATCH THE TRAILER</button>
            <social-sharing :url="trailerLink"
                :title="movie.Title"
                :description="movie.Released"
                :quote="movie.Plot"
                :hashtags="movie.Actors"
                v-cloak inline-template>
            <network network="facebook">
                <i class="fab fa-facebook-square" id="fb-share"></i>
            </network>
            </social-sharing>
    </div>
    <div v-if="showTrailer == true" id="trailer-wrap" v-on:click="showTrailer = false">
        <i class="fas fa-times" id="quit" v-on:click="showTrailer = false"></i>
        <iframe width="60%" height="60%" align="middle" :src="trailerLink" allowfullscreen></iframe>
    </div>
    <div v-if="contentLoaded === false">
        <square-grid id="squaregrid"></square-grid>
    </div>
    </div>
</section>
</template>

<script>
import axios from 'axios';
import { SquareGrid } from 'vue-loading-spinner';

const SocialSharing = require('vue-social-sharing');

export default {
  components: {
    SquareGrid,
    SocialSharing,
  },
  name: 'Movie',
  data() {
    return {
      movie: '',
      overall: 0,
      rated: false,
      showTrailer: false,
      trailerLink: '',
      contentLoaded: false,
    };
  },
  created() {
    axios.get('/api/id', { params: { movieId: this.fetchID() } })
      .then((res) => {
        this.movie = res.data;
        try {
          this.setupRatings();
        } catch (error) {
          // eslint-disable-next-line
        }
        this.fetchTrailer();
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  methods: {
    onBack() {
      this.$router.push('/');
    },

    fetchID() {
      return this.$route.path.split('/')[2];
    },

    setupRatings() {
      let imdb = this.movie.Ratings[0].Value;
      let rotten = this.movie.Ratings[1].Value;
      let meta = this.movie.Ratings[2].Value;

      imdb = imdb.split('/')[0] * 10;
      meta = meta.split('/')[0];
      rotten = rotten.split('%')[0];
      this.overall = Math.floor((+imdb + +rotten + +meta) / 3);
      this.rated = true;
    },

    fetchTrailer() {
      axios.get('/api/trailer', {
        params: {
          title: this.movie.Title,
          year: this.movie.Year,
        } })
        .then((trailer) => {
          this.trailerLink = 'https://www.youtube.com/embed/';
          this.trailerLink += trailer.data.items[0].id.videoId;
          this.contentLoaded = true;
        })
        .catch((err) => {
          // eslint-disable-next-line
          console.error(err);
        });
    },
  },
};
</script>

<style>
.mov {
    margin: 0 auto;
    margin-top: 2%;
    width: 80%;
    text-align: center;
    min-height: 400px;
    background: rgb(0,0,0);
    padding: 14px;
    border-radius: 24px;
}

.mov span.image {
    width: 30%
}

#info {
    font-size: 42px;
    margin-left: 1%;
    width: 69%;
}

#info table {
    min-height: 100%;
    width: 100%;
    color: white;
}

#info table tr {
    width: 100%;
}

#info div {
    text-align: left;
    font-size: 36px;
    min-height: 100%;
}

.key, .value {
    text-align: left;
}

.key {
    width: 15%;
    font-size: 28px;
}

.value {
    width: 85%;
    font-size: 24px;
}

.rating {
    font-size: 18px;
    width: 20%
}

.overall {
    width: 40%;
    font-size: 24px;
}

#released {
    font-size: 32px;
}

.plot {
    font-size: 18px;
    padding: 10px;
    text-align: justify;
    color: rgba(255, 255, 255, .75);
    border: 1px solid rgba(255, 255, 255, .1);
    background: rgba(255, 255, 255, .08);
}

.button-wrap {
    border-top: 1px solid rgba(255, 255, 255, .2);
    padding-top: 1%;
    text-align:center;
    width: 100%;
    margin: 0 auto;
    display: inline-block;
}

#trailer-wrap {
    top: 0;
    left: 0;
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,.8);
    z-index: 999;
}

#trailer-wrap iframe {
    position: absolute;
    transform: translate(-50%, -50%);
    left: 50%;
    top: 50%;
}

i#back {
    font-size: 48px;
    float: left;
    color: rgb(0, 110, 255);
    padding: 0;
    transition: all 100ms ease-in-out;
    border: 2px solid rgb(0, 110, 255);
    padding: 0 .65%;
    width: 5%;
    height: 100%;
    border-radius: 14px;
    padding-top: .3%;
    padding-right: .8%;
}

i#back:hover {
    color: white;
    background: rgb(0, 110, 255);
    transition: all 100ms ease-in-out;
    cursor: pointer;
}

i#quit {
    float: right;
    margin: 1% 1% 0 0;
    font-size: 64px;
    color: white;
    transition: all 100ms ease-in-out;
}

i#quit:hover {
    color: grey;
    cursor: pointer;
    transition: all 100ms ease-in-out;
}

#squaregrid {
    transform: scale(2) translateY(400%);
}

i#fb-share {
    font-size: 58px;
    float: right;
    color: rgb(0, 110, 255);
    transition: all 100ms ease-in-out;
}

i#fb-share:hover {
    color: white;
    transition: all 100ms ease-in-out;
    cursor: pointer;
}
</style>
