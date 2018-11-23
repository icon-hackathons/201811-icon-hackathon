<template>
  <div id="app">
    <!--
      다른 페이지로 이동하는 링크는 a 태그 말고 이 태그 쓰면 됨
      현재 index, project, profile 라우팅 만들어 놨어.
    <div id="nav">
      <router-link to="/">메인 페이지</router-link> |
      <router-link to="/project/sample-project">프로젝트</router-link> |
      <router-link to="/profile/jinhyun-kim">프로필</router-link>
    </div>
    -->
    <!--
      이 router-view 라는 부분에, router.js에서 정의한 컴포넌트들이 들어가게 됨.
      각 컴포넌트들은 views 디렉토리에 있음. (현재 메인페이지, 프로필, 프로젝트 파일만 임시로 만들어놓음)
    -->
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
