<template>
    <div v-if="movie" class="container mx-auto px-4 py-8">
      <div v-if="movie" class="bg-gray-800 rounded-lg shadow-xl overflow-hidden">
        <div
          class="flex flex-col md:flex-row bg-gradient-to-t from-gray-900 to-transparent"
        >
          <img
            :src="movie.poster.url"
            :alt="movie.name"
            class="h-96 object-cover"
          />
          <div class="p-6 md:w-2/3">
            <h1 class="text-4xl font-bold text-white">{{ movie.name }}</h1>
            <p class="text-gray-300 text-lg mb-6">{{ movie.description?movie.description:movie.shortDescription }}</p>
            <p class="text-xl text-gray-300 mt-2">{{ movie.tagLine }}</p>
          </div>
        </div>
      </div>
      <div v-if="movie" class="p-6">
        <div class="flex flex-wrap justify-start items-start text-sm">
          <span class="bg-blue-600 text-white px-3 py-1 rounded-full mr-2 mb-2">{{
            movie.year
          }}</span>
          <span class="bg-green-600 text-white px-3 py-1 rounded-full mr-2 mb-2"
            >{{ movieLength }} мин.</span
          >
          <span
            v-for="genre in movie.genres"
            :key="genre.name"
            class="bg-purple-600 text-white px-3 py-1 rounded-full mr-2 mb-2"
            >{{ genre.name }}</span
          >
          <div
            class="mb-6 self-end justify-self-end place-self-end ml-auto mr-24"
          >
            <h2 class="text-2xl font-semibold text-blue-400 mb-3">Рейтинг</h2>
            <div class="flex items-center">
              <span class="text-4xl font-bold text-yellow-500 mr-2">{{
                movie.rating?.kp?.toFixed(1)
              }}</span>
            </div>
          </div>
        </div>
      </div>
      <div v-if="movie" class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div>
          <h2 class="text-2xl font-semibold text-blue-400 mb-3">Актеры</h2>
          <q-scroll-area style="height: 400px; max-width: 300px">
            <ul>
              <li
                v-for="actor in movie.persons?.filter(
                  (person) => person.enProfession == 'actor'
                )"
                :key="actor.id"
                class="flex items-center"
              >
                <img
                  :src="actor.photo"
                  :alt="actor.name"
                  class="w-16 h-16 m-1 rounded-full object-cover mr-3"
                />
                <div>
                  <nuxt-link :to="`/actor/${actor.id}`" class="block">
                    <p>{{ actor.name }}</p>
                  </nuxt-link>
                  <p>{{ actor.description }}</p>
                </div>
              </li>
            </ul>
          </q-scroll-area>
        </div>
        <div>
          <h2 class="text-2xl font-semibold text-blue-400 mb-3">Дополнительно</h2>
          <p class="text-white">
            <span class="text-gray-400">Статус: </span> {{ movie.status }}
          </p>
          <p class="text-white">
            <span class="text-gray-400">Бюджет: </span>
            {{ movie.budget ? movie.budget : "Неизвестно" }}
          </p>
          <p class="text-white">
            <span class="text-gray-400">Сборы: </span>
            {{ movie.revenue ? movie.revenue : "Неизвестно" }}
          </p>
          <p class="text-white">
            <span class="text-gray-400">Страна: </span>
            {{ movie.countries[0].name }}
          </p>
        </div>
      </div>
    </div>
  </template>
  <script>
 

  export default {
    data() {
      return {
        movie: false,
        
      };
    },
    computed: {
      movieLength() {
        let length = this.movie.movieLength
          ? this.movie.movieLength
          : this.movie.seriesLength;
        return length;
      },
    },
    async mounted()
    {
      console.log(this.$route.params.movieId)

      this.movie = (await useApiFetch("/movie/"+this.$route.params.movieId)).data.value
    }
  };
  </script>
  