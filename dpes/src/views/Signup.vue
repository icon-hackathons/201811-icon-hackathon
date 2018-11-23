<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">
  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">공개 회원으로 가입</h2>
      </div>
    </div>
    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">
          <div class="card border-0 rounded text-left p-5">
            <label class="font-weight-bold mb-0" for="">회원 유형</label>
            <div class="mt-3 btn-group btn-group-toggle" data-toggle="buttons" style="width:100%;">
              <label class="btn btn-secondary active" style="width:100%;"><input type="radio" name="options" id="option1" autocomplete="off" checked>일반 회원</label>
              <label class="btn btn-secondary" style="width:100%;"><input type="radio" name="options" id="option3" autocomplete="off">관리자</label>
            </div>
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">이메일</label>
              <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
              <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <div class="form-group mt-2">
              <label class="font-weight-bold" for="">비밀번호</label>
              <input v-model="pw" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>
            <button @click.prevent="submit" tag="button" class="btn btn-secondary mt-4">가입하기</button>
          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>

<script>
/* eslint-disable func-names */
import { mapState, mapActions } from 'vuex';
import AT from '@/store/action-types';

export default {
  name: 'SignUp',
  data: function () {
    return {
      email: `couldseeme${Math.random()}@icon.foundation`,
      pw: '1234',
    };
  },
  computed: {
    ...mapState({
      auth: state => state.LoginForm.auth,
    }),
  },
  watch: {
    auth: function(val) {
      console.log(val)
      if (val) {
        this.$router.push('/profile/create_profile');
        this[AT.LOGIN_FORM.RESET]();
      }
    },
  },
  methods: {
    ...mapActions([
      AT.LOGIN_FORM.SIGN_UP,
      AT.LOGIN_FORM.RESET,
    ]),
    submit: function () {
      console.log(this.email, this.pw);
      this[AT.LOGIN_FORM.SIGN_UP]({
        email: this.email,
        pw: this.pw,
      });
    },
  },
};
</script>
