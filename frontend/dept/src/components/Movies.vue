<template>
    <section class="section">
        <div class="row">
            <div id="search">
                <input class="form-control" Placeholder="Movie" v-model="movieName">
                <button type="submit" class="btn btn-primary" v-on:click="getMovie">SEARCH</button>
                <hr>
            </div>
            <div id="result">
                <div class="item" v-for="movie of msg" :key="movie.name">
                  <img v-if="movie.Poster != 'N/A'" :src="movie.Poster" />
                  <img v-if="movie.Poster == 'N/A'" src="../assets/na.jpg" />
                  <div class="overlay" :id="movie.imdbID" v-on:click="movieClick($event)">
                    <div class="text">{{movie.Title}}</div>
                  </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Movies',
  data() {
    return {
      msg: '',
      movieName: '',
    };
  },
  created: function () {
    this.movieName = localStorage.getItem('lastSearch');
    document.getElementsByTagName('input').value = this.movieName;
    this.getMovie();
  },
  methods: {
    getMovie() {
      let path = 'http://localhost:5000/movies/name/';
      path += this.movieName;
      localStorage.setItem('lastSearch', this.movieName);
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          this.msg = error;
        });
    },
    movieClick(event) {
      let url = 'movie/';
      url += event.target.id;
      this.$router.push(url);
    },
  },
};
</script>

<style>
section {
    position: relative;
    margin-top: 20px;
}

#search,
#result {
    position: relative;
    width: 100%;
}

#search {
    display: flex;
    padding: 3%;
    border-radius: 120px;
}

#search input,
#search button {
    display: flex;
}

#search input {
    border-radius: 6px;
    margin-right: 2%;
    text-align: left;
}

#result span {
    position: relative;
}

#result {
    border-radius: 20px;
    margin-top: 1%;
}

.item {
  position: relative;
  display: inline-flex;
  margin: 1%;
  overflow: hidden;
  min-height: 500px;
  max-height: 500px;
  width: 30%;
  height: 25%;
  border-radius: 16px;
}
.item img {
  width: 100%;
  -moz-transition: all 0.3s;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.item:hover img {
  -moz-transform: scale(1.05);
  -webkit-transform: scale(1.05);
  transform: scale(1.05);
  filter: blur(5px);
  cursor: pointer;
}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .5s ease;
  background: rgba(0, 0, 0, .05);
  cursor: pointer;
}

.item:hover .overlay {
  opacity: 1;
}

.text {
  color: white;
  font-size: 110%;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
  pointer-events: none;
}
</style>
