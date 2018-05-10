<template>
  <div>
    <nav>
      <div class="container">
        <ul class="nav__left">

          <!-- Navigation Links -->
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/admin">Admin</router-link></li>
          <li><router-link to="/cart">Cart</router-link></li>

        </ul>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

@import url('https://fonts.googleapis.com/css?family=PT+Sans|Raleway');

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: 'Raleway', sans-serif;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

nav {
  font-family: 'PT Sans', sans-serif;
  font-weight: 300;
  text-transform: uppercase;
  background: #333;
}

nav .container {
  display: flex;
}

nav .nav__left {
  flex-grow: 3;
  display: flex;
}

nav .nav__right {
  flex-grow: 2;
  display: flex;
  flex-direction: row-reverse;
}

nav li a {
  color: #FFFFFF;
  display: block;
  padding: 15px 15px;
  transition: all 150ms ease-out;
}

nav li a:hover {
  text-decoration: none;
  color: #A6A6A6;
}

nav li a:focus {
  text-decoration: none;
}

nav li a i  {
  margin-right: 4px;
}

.title h1 {
  text-align: center;
}

.title {
  padding: 10px 0;
  border-bottom: 2px solid #F5F5F5;
}

button.button {
  background: #EFDB06;
  border: 1px solid #F9E610;
  border-radius: 20px;
  padding: 10px 15px;
  font-family: 'PT Sans', sans-serif;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 12px;
  transition: all 200ms ease-out;
  outline: none;
}

button.button:hover {
  background: #F9E610;
}

button.button.disabled {
  background: #F9E610;
  opacity: 0.6;
  cursor: default;
}

button.button.button-danger {
  background: #FF3333;
  border: 1px solid #FF4747;
  color: #fff;
}

button.button.button-danger:hover {
  background: #FF4747;
}

.new-button {
  display: flex;
  flex-direction: row-reverse;
}

.form-control:focus {
  border-color: #F9E610;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(249, 230, 16, 0.6);
}

.form-control.error {
  border-color: #FF3333;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(255, 71, 71, 0.6);
}

  .overlay {
    background: rgba(255, 255, 255, 0.6);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  .loading-spinner {
    position : absolute;
    top      : 50%;
    left     : 50%;
    -webkit-transform : translateX(-50%) translateY(-50%);
    -moz-transform : translateX(-50%) translateY(-50%);
    transform : translateX(-50%) translateY(-50%);
  }
  .dot {
    background    : black;
    border-radius : 100%;
    color         : white;
    height        : 8px;
    line-height   : 8px;
    text-align    : center;
    width         : 8px;
  }
  .dotOne {
    -webkit-animation : dotOneKeyframes 5s ease  infinite;
    background        : #F9E610;
    position          : absolute;
    top               : 0;
    left              : 0;
  }
  .dotTwo {
    -webkit-animation : dotTwoKeyframes 5s ease 0.4166666666666s infinite;
    background        : #EFDB06;
    position          : absolute;
    top               : 0;
    left              : 14px;
  }
  .dotThree {
    -webkit-animation : dotThreeKeyframes 5s ease 0.83333333333s infinite;
    background        : #DBC906;
    position          : absolute;
    top               : 14px;
    left              : 14px;
  }
  @-webkit-keyframes dotOneKeyframes {
    0% {
      top  : 0;
      left : 0;
    }
    8.3333333333% {
      top  : 14px;
      left : 0;
    }
    16.6666666666% {
    }
    25% {
      top  : 14px;
      left : 0;
    }
    33.3333333333% {
      top  : 14px;
      left : 14px;
    }
    41.6666666666% {
    }
    50% {
      top  : 14px;
      left : 14px;
    }
    58.3333333333% {
      top  : 0;
      left : 14px;
    }
    66.6666666666% {
    }
    75% {
      top  : 0;
      left : 14px;
    }
    83.3333333333% {
      top  : 0;
      left : 0;
    }
    91.6666666666% {
    }
    100% {
    }
  }
  @-webkit-keyframes dotTwoKeyframes {
    0% {
      top  : 0;
      left : 14px;
    }
    8.3333333333% {
      top  : 0;
      left : 0;
    }
    16.6666666666% {
    }
    25% {
      top  : 0;
      left : 0;
    }
    33.3333333333% {
      top  : 14px;
      left : 0;
    }
    41.6666666666% {
    }
    50% {
      top  : 14px;
      left : 0;
    }
    58.3333333333% {
      top  : 14px;
      left : 14px;
    }
    66.6666666666% {
    }
    75% {
      top  : 14px;
      left : 14px;
    }
    83.3333333333% {
      top  : 0;
      left : 14px;
    }
    91.6666666666% {
    }
    100% {
    }
  }
  @-webkit-keyframes dotThreeKeyframes {
    0% {
      top  : 14px;
      left : 14px;
    }
    8.3333333333% {
      top  : 0;
      left : 14px;
    }
    16.6666666666% {
    }
    25% {
      top  : 0;
      left : 14px;
    }
    33.3333333333% {
      top  : 0;
      left : 0;
    }
    41.6666666666% {
    }
    50% {
      top  : 0;
      left : 0;
    }
    58.3333333333% {
      top  : 14px;
      left : 0;
    }
    66.6666666666% {
    }
    75% {
      top  : 14px;
      left : 0;
    }
    83.3333333333% {
      top  : 14px;
      left : 14px;
    }
    91.6666666666% {
    }
    100% {
    }
  }
</style>
