<template>
  <nav class="navbar is-light">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>ECom</strong></router-link>

      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
         @click="showMobileMenu = !showMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/log-in" class="button is-light">Log in</router-link>
            <router-link to="/cart" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart ({{ cartTotalLength }})</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
  <section class="section">
    <router-view/>
  </section>
  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2022</p>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  computed:{
    cartTotalLength(){
      let total_length = 0;
      for (let i = 0; i < this.cart.items.length; i++)
      {
        total_length += this.cart.items[i].quantity
      }
      return total_length
    },
  },
}
</script>
<style lang="scss">
@import "../node_modules/bulma";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
