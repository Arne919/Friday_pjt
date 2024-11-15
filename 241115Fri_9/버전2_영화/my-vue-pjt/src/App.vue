<template>
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/movies">Movies</RouterLink> | 
      <RouterLink to="/review-search">Review Search</RouterLink> |
      <RouterLink to="/recommended">Recommended</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>

</script>

<style scoped>

</style>