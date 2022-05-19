<template>
    <main>
        <h1>New Category</h1>
        <form>
            <p>Category id : ----- </p>
            <label for="category-name">:</label>
            <input type="text">
            <label for="category-image">Lastly, an image:</label>
            <input type="image">
            <button>Submit</button>
        </form>
    </main>

</template>

<script>
export default {

}
</script>

<style>
form{
  display: flex;
  flex-direction: column;
}
button{
  width: 10%;
}

</style>