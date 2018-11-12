/* eslint-disable */

<template>
<div id="app">

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">
      <router-link to="/"><img src="https://m.icon.foundation/resources/image/favicon.ico" width="30" height="30" class="d-inline-block align-top" alt=""> DPES
      </router-link>
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">

        <!-- @Decorator; 비로그인 상태 -->

        <li class="nav-item active">
          <a class="nav-link">
            <router-link to="/signin">로그인</router-link><span class="sr-only">(current)</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link">
            <router-link to="/signup">회원가입</router-link>
          </a>
        </li>

        <!-- @Decorator; 로그인 상태 -->
        <li class="nav-item">
          <a class="nav-link">
            <router-link to="/dashboard">대쉬보드</router-link>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link to="/profile">내 프로필</router-link>
          </a>
        </li>

      </ul>

      <!-- @Decorator; 공용 기능 -->
      <span class="">
        <button class="btn btn-light" type="button">
          <router-link to="/list">평가하기</router-link>
        </button>
      </span>

    </div>

  </nav>
  <router-view/>
</div>
</template>

<style lang="scss">
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#nav {
    padding: 30px;
    a {
        font-weight: bold;
        color: #2c3e50;
        &.router-link-exact-active {
            color: #42b983;
        }
    }
}

.set-bg {
    width: 100%;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    background-position: center !important;
    -webkit-background-size: cover !important;
    -moz-background-size: cover !important;
    -o-background-size: cover !important;
    background-size: cover !important;
}

.jumbotron-wide{
  padding-top: 130px !important;
  padding-bottom: 130px !important;
  border-radius: 0px !important;
  margin-bottom: 0px !important;
}

.jumbotron-breadcrumb{
  text-align: left !important;
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  border-radius: 0px !important;
  margin-bottom: 0px !important;

  .title {
    margin-bottom:0px;
    font-weight: 900;
  }
}

.my-hr {
  border: 0;
  height: 3px;
  margin-top:20px;
  margin-bottom:40px;
  width:180px;
}

</style>
