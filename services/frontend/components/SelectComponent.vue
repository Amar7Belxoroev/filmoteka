<template>
    <div>
        <label class="block text-sm font-medium text-gray-300 mb-2">{{ Title }}</label>
        <select @input="e=>$emit('update:modelValue', e.target.value)" :value="modelValue"  class="w-full p-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:right-2 focus:ring-blue-500 focus:border-blue-500">
            <option v-for="option in Options" :key="option">{{path?option[Path]:option }}</option>
        </select>
    </div>
</template>
<script>
    export default
    {
        data()
        {
            return
            {
                
            }
        },
        props: ["Title", "Options", "Selected", "Path", "modelValue"]
    }
</script>