<template>
  <!-- eslint-disable max-len -->
<div id="app">

  <nav class="navbar navbar-expand-lg navbar-light bg-white">
    <a class="navbar-brand" href="#">
      <router-link to="/">
        <img src="../src/assets/logo-dpes.png" max-width="100" height="50" class="d-inline-block align-middle" alt="">
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
            <router-link class="nav-atag" to="/signin">로그인</router-link><span class="sr-only">(current)</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link">
            <router-link class="nav-atag" to="/signup">회원가입</router-link>
          </a>
        </li>

        <!-- @Decorator; 로그인 상태 -->
        <li class="nav-item">
          <a class="nav-link">
            <router-link class="nav-atag" to="/dashboard">대쉬보드</router-link>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link class="nav-atag" to="/profile">내 프로필</router-link>
          </a>
        </li>

      </ul>

      <!-- @Decorator; 공용 기능 -->
      <span class="nav-atag">
        <button class="btn btn-lg btn-dark" type="button">
          <router-link class="" to="/evaluation/getstarted">평가하기</router-link>
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

.nav-pills .nav-link.active, .nav-pills .show>.nav-link{
  color: black !important;
  border-bottom: 2px solid black;
  border-radius: 0px;
  font-weight: bold;
  background-color: transparent !important;
}

$color-main: rgba(27,176,206,0.8);

.font-weight-extra-bold{
  font-weight:900 !important;
}

.nav-atag{
  color:black;
  text-decoration: none;
  &:hover{
    color:$color-main;
    text-decoration: none;
  }
  a{
    color:white;
    text-decoration: none;
    &:hover{
      color:white;
      text-decoration: none;
    }
  }
}
.thumbnail{
  &.round{
    max-width:100%;
    width:200px;
    border-radius: 50%;
  }
  &.small{
    width:35px;
    height:35px;
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
  background-image: url('../src/assets/index-dark.jpg');
  text-align: left !important;
  padding-top: 50px !important;
  padding-bottom: 50px !important;
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
