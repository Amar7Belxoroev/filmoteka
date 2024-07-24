<template>
    <div class="container mx-auto px-4 py-8">
        <div v-if="actor" class="bg-gray-800 rounded-lg shadow-xl overflow-hidden">
            <div class="flex flex-col md:flex-row">
                <div class="md:w-1/3">
                    <img :src="actor.photo" :alt="actor.name" class="w-72 h-auto object-scale-down"/>
                </div>
                <div class="md:w2/3 p-6">
                    <h1 class="text-4xl font-bold text-white mb-2">{{ actor.name }}</h1>
                    <p v-if="actor.birthday" class="text-xl text-gray-300 mb-4">
                     Дата рождения: {{ birthDate }}
                     <span v-if="actor.death"> - Дата смерти {{ deathDate }}</span>
                    </p>
                    <div class="mb-6" v-if="actor.birthPlace||actor.facts">
                        <h2 class="text-2xl font-semibold text-blue-400 mb-3">Дополнительная информация</h2>
                        <p v-if="actor.birthPlace" class="text-white"><span class="text-gray-400"> Место рождения: {{ birthPlace }} </span></p>
                        <p v-if="actor.fact" v-for="fact in actor.facts" :key="fact.value" class="text-white"><span class="text-gray-400"> {{ fact.value }} </span></p>
                    </div>
                </div>
            </div>
            <div class="p-6">
                <h2 class="text-2xl font-semibold text-blue-400 mb-4">Фильмография</h2>
                <div class="grid grid-cols-2 md:grid-cols-3  gap-4">
                    <div v-for="movie in actor.movies" :key="movie.id" class="bg-gray-700 rounded-lg overflow-hidden p-4">
                        <nuxt-link :to="`/movie/${movie.id}`" class="block">
                            <h3 class="text-white font-semibold mb-1 hover:text-blue-400 transition duration-75">{{ movie.name?movie.name:movie.alternativeName }}</h3>
                            <p class="text-gray-300 text-sm mt-2"> {{ movie.description }}</p>
                        </nuxt-link>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="text-center text-white text-2xl">Загрузка...</div>
    </div>
</template>
<script>
import { TestDataProvider } from '~/testData';

 export default
 {
    data()
    {
        return {
            actor: false,
        }
    },
    async mounted(){
        this.actor = (await useApiFetch("/person/"+this.$route.params.actorId)).data.value
    },

    computed :
    {
        birthDate()
        {
            let str = ''
            console.log(this.actor.birthday.indexOf('T'))
            let birthDateStr = this.actor.birthday.substring(0, this.actor.birthday.indexOf('T'))
            return birthDateStr;
        },
        deathDate()
        {
            let str = ''
            console.log(this.actor.death.indexOf('T'))
            let deathDateStr = this.actor.death.substring(0, this.actor.death.indexOf('T'))
            return deathDateStr;
        },
        birthPlace()
        {
            let bornPlaceStr = ''
            this.actor.birthPlace.forEach(element => {
                bornPlaceStr +=  ` ${element.value},`
            });
            bornPlaceStr = bornPlaceStr.substring(0, bornPlaceStr.length-1)
            return bornPlaceStr
        }
    }
 }
</script>