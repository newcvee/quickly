<template>
  <main>
    <h1>New Category</h1>
    <form>
      <label for="category-name">Give the new category a name:</label>
      <input type="text">
      <label for="category-id">Now, an id:</label>
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