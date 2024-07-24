export const useApiFetch = (request, opts) => {
    const config = useRuntimeConfig()
    return useFetch(request, { baseURL: config.public.baseURL, headers:{"X-API-KEY": config.public.apiKey}, ...opts })
  }