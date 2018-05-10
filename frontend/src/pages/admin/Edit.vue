<!-- ./src/pages/admin/Edit.vue -->
<template>
  <div>
    <div class="title">
      <h1>This is Admin/Edit/{{$route.params.id}}</h1>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    console.log(this.$route.params.id) // prints value of :id
  }
}
</script>
