<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Ecom
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      <ProductComponent
    v-for="product in products"
    :key="product.id"
    :product="product"
  />
    </div>
  </div>

</template>

<script>
import axios from 'axios'

import ProductComponent from "@/components/ProductComponent";

export default {
  name: 'HomeView',
  data() {
    return {
      products: []
    }
  },
  components: {
    ProductComponent
  },
  mounted() {
    this.getProducts()
  },
  methods: {
    async getProducts() {
      await axios
          .get('api/products/')
          .then(response => {
            console.log(response.data)
            this.products = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>
