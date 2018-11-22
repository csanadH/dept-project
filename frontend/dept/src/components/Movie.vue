<template>
  <div class="container">
    <div class="row">
    <span id="search" class="span-1-of-10">
        <input v-model="movieName"><br><br>
        <button type="button" class="btn btn-primary" v-on:click="getMovie">Search</button><br>
    </span>
    <span id="results" class="span-8-of-10">
        <div class="row">
        <span v-for="movie of msg" :key="movie.name">
            <p>{{movie.Title}}</p>
            <img :src=movie.Poster />
        </span>
        </div>
    </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Movie',
  data() {
    return {
      msg: '',
      movieName: '',
    };
  },
  methods: {
    getMovie() {
      let path = 'http://localhost:5000/movies/';
      path += this.movieName;
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

<style>
.container {
    margin-top: 12px;
}

#search,
#results {
    background: rgba(0,0,0, .5);
    height: 1200px;
}

#search {
    float: left;
}

#results {
    float: right;
}

#search input,
#search button {
    width: 100%;
}
</style>