<template>
<!-- eslint-disable max-len -->
<div id="app">
  <nav class="navbar navbar-expand-lg navbar-light bg-white">
    <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
      <ul v-if="userId" class="navbar-nav mr-auto">
        <!-- @Decorator; 로그인 상태 -->
        <li class="nav-item">
          <a class="nav-link">
            <a @click.prevent="logOut" class="nav-atag" to="/">로그아웃</a>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link class="nav-atag" to="/profile">내 정보</router-link>
          </a>
        </li>
      </ul>
      <ul v-else class="navbar-nav mr-auto">
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
      </ul>
    </div>
    <div class="mx-auto order-0">
        <a class="navbar-brand mx-auto" href="#">
          <router-link to="/">
            <img src="../src/assets/logo-dpes.png" max-width="100" height="50" class="d-inline-block align-middle" alt="">
          </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    </div>
    <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
      <ul class="navbar-nav ml-auto">
        <!-- @Decorator; 공용 기능 -->
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link :to="{name: 'setorganization'}" tag="button" class="btn btn-outline-secondary">평가 개설하기</router-link>
          </a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link :to="{name: 'getstarted'}" tag="button" class="btn btn-secondary">평가하기</router-link>
          </a>
        </li>
      </ul>
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

.profile-card {
    .card {
        border-color: transparent;
        padding: 10px;
    }
}

.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
    color: black !important;
    border-bottom: 2px solid black;
    border-radius: 0;
    font-weight: bold;
    background-color: transparent !important;
}

$color-main: rgba(27,176,206,0.8);

.font-weight-extra-bold {
    font-weight: 900 !important;
}

.nav-atag {
    color: black;
    text-decoration: none;
    &:hover {
        color: $color-main;
        text-decoration: none;
    }
    a {
        color: white;
        text-decoration: none;
        &:hover {
            color: white;
            text-decoration: none;
        }
    }
}
.thumbnail {
    &.round {
        max-width: 100%;
        width: 200px;
        border-radius: 50%;
    }
    &.small {
        width: 35px;
        height: 35px;
    }
}

.form-control {
    border-radius: 5px !important;
    font-size: 13px !important;

    &:focus {
        outline: none !important;
        box-shadow: none !important;
        border-color: #595959 !important;

    }

}

.filebox label {
    display: inline-block;
    padding: 50px;
    color: white;
    font-size: inherit;
    line-height: normal;
    vertical-align: middle;
    background-color: #ccc;
    cursor: pointer;

}

.filebox input[type="file"] {
    /* 파일 필드 숨기기 */
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
    border: 0;
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

.jumbotron-wide {
    padding-top: 130px !important;
    padding-bottom: 130px !important;
    border-radius: 0 !important;
    margin-bottom: 0 !important;
}

.jumbotron-breadcrumb {
    background-image: url("../src/assets/index-dark.jpg");
    text-align: left !important;
    padding-top: 50px !important;
    padding-bottom: 50px !important;
    border-radius: 0 !important;
    margin-bottom: 0 !important;

    .title {
        margin-bottom: 0;
        font-weight: 900;
    }
}

.my-hr {
    border: 0;
    height: 3px;
    margin-top: 20px;
    margin-bottom: 40px;
    width: 180px;
}
</style>

<script>
import { mapState, mapActions } from 'vuex';
import Breadcrumb from '@/views/Breadcrumb.vue'
import ProfileHeader from '@/views/profile/ProfileHeader.vue'
import Star from '@/views/common/Star.vue';
import AT from '@/store/action-types';

export default {
  name: 'App',
  computed: {
    ...mapState({
      userId: state => state.LoginForm.userId,
    }),
  },
  watch: {
    userId: function(val) {
      if (!val) {
        this.$router.push('/');
      }
    },
  },
  methods: {
    ...mapActions([
      AT.LOGIN_FORM.LOG_OUT,
    ]),
    logOut: function () {
      this[AT.LOGIN_FORM.LOG_OUT]();
    },
  }
};
</script>
