<template>
  <div class="container mx-auto px-4 py-8">
    <div class="relative">
      <input
        v-model="searchQuery"
        v-on:keyup.enter="searchMovies"
        class="w-full px-6 py-4 rounded-full bg-gray-800 text-white border border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-800 pl-12 text-lg focus:shadow-lg focus:shadow-blue-600/50"
        placeholder="Найти фильмы"
      />
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6 absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
        />
      </svg>
      <SearchFilter
        v-model="filterObject"
        @filtersUpdate="
          (e) => {
            filterObject = e;
          }
        "
        class="h-6 w-6 absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400"
      ></SearchFilter>
    </div>
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-12 mt-8">
       <div
        v-for="movie in sortedMovies"
        :key="movie.id"
        class="bg-gray-800 rounded-lg shadow-lg overflow-hidden transform hover:scale-105 transition duration-300 flex flex-col hover:shadow-md hover:shadow-blue-600/50"
      >
        <div class="relative">
          <img
            :src="movie.poster.previewUrl"
            class="w-full h-100 object-cover"
          />
          <div
            class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-gray-900 to-transparent p-4"
          >
            <h2 class="text-xl font-semibold mb-1 text-white">
              {{ movie.name }}
            </h2>
            <h2 class="text-md text-gray-300">{{ movie.year }}</h2>
          </div>
        </div>
        <div class="p-4 flex-grow flex flex-col justify-between">
          <p class="text-gray-300 text-md mb-4 line-clamp-3">
            {{
              movie.shortDescription
                ? movie.shortDescription
                : movie.description
            }}
          </p>
          <div class="flex justify-between items-center">
            <span class="text-yellow-500 text-lg"
              >★
              {{
                movie.rating?.kp?.toFixed(1)
                  ? movie.rating?.kp?.toFixed(1)
                  : "Нет рейтинга"
              }}</span
            >
            <nuxt-link :to="'/movie/' + movie.id" class="block">
              <button
                class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition duration-300"
              >
                Больше информации
              </button>
            </nuxt-link>
          </div>
        </div>
      </div>


    </div>
    <div class=" flex flex-row mt-20 items-center justify-center">
      <q-pagination
      v-if="movies.length>0"
      @update:model-value="(v)=>{$router.push({path: $route.path,
          query: { page: v, searchQuery: searchQuery }}); currentPage=v; updateQuery()}"
      v-model="currentPage"
      text-color="white"
      color="blue"
      :max="maxPages"
      :max-pages="6"
      :boundary-numbers="false"
      />
    </div>
    <q-ajax-bar
      ref="bar"
      position="bottom"
      color="blue"
      size="10px"
      skip-hijack
    />
  </div>
</template>
<script>
import { TestDataProvider } from "~/testData";
import {MoviesService} from "~/services/moviesService"
export default {
  data() {
    return {
      currentPage: 1,
      maxPages: 1,
      moviesService: new MoviesService(1),
      movies: [],
      filteredMovies: [],
      searchQuery: "",
      filterObject: {
        genre: "Все жанры",
        countries: "Все страны",
        yearsRange: { min: 1920, max: 2024 },
        ratingRange: { min: 0, max: 10 },
        movieLength: { min: 0, max: 400 },
        sortBy: "По рейтингу"
      },
    };
  },
   async mounted() {
    watch(() => this.$route.query.searchQuery, () => {
      this.updateQuery()
    })
   // if(this.$route.query.searchQuery)
    await nextTick(async ()=>{await this.updateQuery()})
    console.log(useApiFetch.prototype)
  
  },
  methods: {
    updateQuery()
    {
      if(!this.$route.query.searchQuery)
      return
      this.searchQuery = this.$route.query.searchQuery
      this.searchMovies()
      console.log(this.$router.currentRoute.value.query)
    },
    async searchMovies() {
      this.moviesService.page = this.currentPage
      const barRef = this.$refs.bar;
      
      barRef.start();
      if (this.searchQuery == "") {
        let res = await this.moviesService.SearchMoviesByFilter(this.filterObject)
         this.movies = res.docs
         this.maxPages = res.pages
          barRef.stop();
          return;
        }

        let res = await this.moviesService.SearchMoviesByQeury(this.searchQuery)
        this.movies = res.docs
        this.maxPages = res.pages
        
        this.$router.push({
          path: this.$route.path,
          query: { searchQuery: this.searchQuery, page: this.currentPage, },
        });
        barRef.stop();
      },
      onLoad()
      {
        console.log("loaad") 
      }
    },
    computed:{
      sortedMovies()
      {
        let filter = this.filterObject
        this.filteredMovies = this.movies.filter((m)=>{
          return m.rating.kp >= filter.ratingRange.min && 
          m.rating.kp <= filter.ratingRange.max &&
          m.year >= filter.yearsRange.min &&
          m.year <= filter.yearsRange.max &&
          m.poster.url &&
          m.description &&
          m.name
        })
        if(this.filterObject.genre!="Все жанры")
        this.filteredMovies = this.filteredMovies.filter((m)=>{
          return m.genres.some(g=>g.name.toLowerCase()==this.filterObject.genre.toLowerCase())
        })
        if(this.filterObject.countries!="Все страны")
        this.filteredMovies = this.filteredMovies.filter((m)=>{
          return m.countries.some(с=>с.name.toLowerCase()==this.filterObject.countries.toLowerCase())
        })
        if(this.filterObject.sortBy=="По рейтингу")
        {
          return this.filteredMovies.sort((m1,m2)=>{
            if(m1.rating.kp<m2.rating.kp)
            return 1 
            
            if(m1.rating.kp>m2.rating.kp)
            return -1 
            
            return 0
          })
        }
        if(this.filterObject.sortBy=="По дате выхода")
        {
          return this.filteredMovies.sort((m1,m2)=>{
            if(m1.year<m2.year)
            return 1 
            
            if(m1.year>m2.year)
            return -1 
            
            return 0
          })
        }
      }
    },
  };
</script>
