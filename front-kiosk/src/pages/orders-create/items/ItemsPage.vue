<template>
<p>hellouuu</p>
<section class="card" v-for="item in items" :key="item.category_id" @click="enterItemDetail(item)" >
<p>{{item.img}}</p>
<p>{{item.name}}</p>
</section>
</template>

<script>
import { getItemsByCategory } from "@/services/api.js";
export default {
    name: "Item",
    data(){
        return { 
            items: {},
            };
    },
    mounted() {
        this.loadItems();
    },
    methods: {
        async loadItems() {
            let categoryId = this.$route.params.category_id;
            this.items = await getItemsByCategory(categoryId);
        },
        enterItemDetail(item){            
         this.$router.push("/items/" + item.id)
        },
        
    }

}
</script>

<style>
.card {
    border: 1px solid;
}

</style>