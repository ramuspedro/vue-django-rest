<!-- ./src/pages/admin/New.vue -->
<template>
  <div>
    <div class="title">
      <h1>This is Admin/New</h1>
      <form>
        <input v-model="message" placeholder="edit me">
        <p>Message is: {{ message }}</p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    }
  }
}
</script>

