<template>
    <header class="bg-gray-800 text-white">
        <div class="flex items-center justify-between mx-auto px-4 py-4">
            <nuxt-link to="/" class="block">
                <h1 class="text-2xl font-bold hover:cursor-pointer" @click="$router.push('/')">Filmoteka app</h1>
            </nuxt-link>
        </div>
    </header>
</template>