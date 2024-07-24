<template>
  <q-icon name="settings" class="text-gray cursor-pointer text-2xl">
    <q-popup-proxy
      transition-show="flip-up"
      transition-hide="flip-down"
      class="rounded-lg bg-gray-800"
    >
      <div class="p-6 m-6 w-96">
        <div class="grid grid-cols-2 gap-8">
          <div>
            <SelectComponent class="mt-4" v-model="modelValue.sortBy" Title="Сортировка" :Options="sortOptions"></SelectComponent>
            <SelectComponent class="mt-4" v-model="modelValue.genre" Title="Жанры" :Options="genres"></SelectComponent>
            <SelectComponent class="mt-4" v-model="modelValue.countries" Title="Страны" :Options="countries"></SelectComponent>
          </div>
          <div>
           
              <div class="mt-4">
                 <label class="text-gray-300"> {{"Продолжительность фильма: " + movieLengthFormat.min + "-" + movieLengthFormat.max }}</label>
                 <q-range v-model="modelValue.movieLength" :min="0" :max="400"  @change="$emit('update:modelValue', modelValue)"/>
                </div>
                <div class="mt-4">
                  <label class="text-gray-300"> {{"Год релиза: " + modelValue.yearsRange.min + "-" + modelValue.yearsRange.max }}</label>
                  <q-range  v-model="modelValue.yearsRange" :min="1920" :max="2024" @change="$emit('update:modelValue', modelValue)" />
                </div>
                <div class="mt-4">
                  <label class="text-gray-300"> {{"Рейтинг: " + modelValue.ratingRange.min + "-" + modelValue.ratingRange.max }}</label>
                  <q-range v-model="modelValue.ratingRange" :min="0" :max="10" :step="0.1" @change="$emit('update:modelValue', modelValue)"/>
                </div>
              </div>
        </div>
      </div>
    </q-popup-proxy>
  </q-icon>
</template>
<script>
export default {
  data() {
    return {
      filters: {
        genre: "Все жанры",
        countries:"Все страны",
        year: "",
        rating: "",
        model: "",
        yearsRange: {min:1920, max: 2024},
        ratingRange: {min:0, max:10},
        movieLength: {min:0, max:400},
      },
      sortBy: "popularity.desc",
      genres: ["Все жанры", "Боевик", "Драма", "Комедия", "Мелодрама", "Ужасы"],
      countries: ["Все страны", "США", "Россия", "Франция" , "Великобритания"],
      sortOptions:["По рейтингу", "По дате выхода"]
    };
  },
  props:["modelValue"],

computed:{
    movieLengthFormat()
    {
        let minHours = Math.trunc(this.modelValue.movieLength.min/60)
        let minMinutes = this.modelValue.movieLength.min - minHours*60

        let maxHours = Math.trunc(this.modelValue.movieLength.max/60)
        let maxMinutes = this.modelValue.movieLength.max - maxHours*60
        return {min:`${minHours}:${minMinutes}`, max:`${maxHours}:${maxMinutes}`}
    }
}
};
</script>
