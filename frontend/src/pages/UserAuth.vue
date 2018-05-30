<template>
  <div class="container">
    <h1 class="text-center">Welcome to the Project!</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-6 offset-sm-3">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="true">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="false">Sign Up</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div class="tab-pane fade show active" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="login-username" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input v-model="password" type="password" class="form-control" id="login-password" placeholder="Password" required>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign in</button>
            </form>
          </div>

          <div class="tab-pane fade" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signUp">
              <div class="form-group">
                <input v-model="email" type="email" class="form-control" id="email" placeholder="Email Address" required>
              </div>
              <div class="form-row">
                <div class="form-group col-md-12">
                  <input v-model="username" type="text" class="form-control" id="username" placeholder="Username" required>
                </div>
                <div class="form-group col-md-6">
                  <input v-model="password1" type="password" class="form-control" id="password1" placeholder="Password" required>
                </div>
                <div class="form-group col-md-6">
                  <input v-model="password2" type="password" class="form-control" id="password2" placeholder="Confirm password" required>
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="toc" required>
                  <label class="form-check-label" for="gridCheck">
                    Accept terms and Conditions
                  </label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign up</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        email: '',
        username: '',
        password: '',
        password1: '',
        password2: ''
      }
    },
    methods: {
      signUp() {
        const newUser = {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2
        }

        console.log("Novo usuário: ", newUser);

        fetch('http://localhost:8000/api/v1/rest-auth/registration/', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(newUser)
          }).then((res) => {
            return res.json()
          })
          .then((data) => {
            console.log("DATA", data)
            
          })
          .catch((err) => console.log("ERROOOOO", err))
        // $.post('http://localhost:8000/auth/users/create/', this.$data, (data) => {
        //     alert("Your account has been created. You will be signed in automatically")
        //     this.signIn()
        //   })
        //   .fail((response) => {
        //     alert(response.responseText)
        //   })
      },

      signIn() {
        const credentials = {
          username: this.username,
          password: this.password
        }

        console.log("TESTE: ", credentials);

        let headers = new Headers()

        headers['Content-Type'] = 'application/json'

        fetch('http://localhost:8000/api/v1/rest-auth/login/', {
            method: 'POST',
            // headers: new Headers(),
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(credentials)
          }).then((res) => {
            return res.json()
          })
          .then((data) => {
            localStorage.setItem('authToken', data.key)
            localStorage.setItem('username', this.username)
            // this.$root.token = data.key
            this.$router.push('/map')
          })
          .catch((err) => console.log(err))
      }
    }
  }
</script>

<style scoped>
  #auth-container {
    margin-top: 50px;
  }

  .tab-content {
    padding-top: 20px;
  }
</style>