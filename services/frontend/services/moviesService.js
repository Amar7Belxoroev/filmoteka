export class MoviesService
{
 
    async SearchMoviesByQeury(searchQuery) {
        console.log(useApiFetch.prototype)
          let object = (
          await useApiFetch("/movie/search?query=" + searchQuery)
          ).data.value.docs
          console.log(object)
          return object

        }

    async SearchMoviesByFilter(filter) {
        let queryParams = "";
        queryParams += `releaseYears.end=${filter.yearsRange.min}-${filter.yearsRange.max}&`;
        queryParams += `rating.kp=${filter.ratingRange.min}-${filter.ratingRange.max}&`;
        if (filter.genre != "Все жанры")
        queryParams += `genres.name=${filter.genre}&`;
        if (filter.countries != "Все страны")
        queryParams += `countries.name=${filter.countries}&`;
        queryParams += `movieLength=${filter.movieLength.min}-${filter.movieLength.max}`;
        let object = (await useApiFetch("/movie?page=1&limit=10&" + queryParams)).data.value;
            return object.docs;
    }
    async GetTop250()
    {
        
    }
}