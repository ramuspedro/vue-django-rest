<!-- ./src/pages/Cart.vue https://travishorn.com/interactive-maps-with-vue-leaflet-5430527353c8 -->

<template>
  <div id="appMap" class="container">
    <div class="row">
      <div class="col-md-9">
        <div id="map" class="map"></div>
      </div>
      <div class="col-md-3">
        <!-- The layer checkboxes go here -->
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data() {
      return {
        map: null,
        tileLayer: null,
        layers: [],
      }
    },
    mounted() {
      this.initMap();
      this.initLayers();
    },
    methods: {
      initMap() {
        console.log("init map", L);
        this.map = L.map('map').setView([38.63, -90.23], 12);

        this.tileLayer = L.tileLayer(
          'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
          }
        );
        this.tileLayer.addTo(this.map);
      },
      initLayers() {},
    },
  }
</script>

<style scoped>
  .map {
    height: 600px;
  }
</style>