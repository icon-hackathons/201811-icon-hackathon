<script>
import { mapState, mapActions } from 'vuex';
import AT from '@/store/action-types';
import Constants from '@/constants';
export default {
  name: 'SetOrganization',
  data: function () {
    return {
      projectName: '2018년 4/4분기 인사평가',
      desc: '2018년 4/4분기 인사평가 워크스페이스입니다.',
      threshold: 80
    }
  },
  computed: {
    ...mapState({
      newWorkspaceAddress: state => state.Workspace.newWorkspaceAddress,
    }),
  },
  methods: {
    ...mapActions([
      AT.WORKSPACE.DEPLOY_WORKSPACE,
    ]),
    deploy: function (img) {
      this[AT.WORKSPACE.DEPLOY_WORKSPACE]({
        adminAddress: 'hxa4c3a78d73bb7287f72801c09298f1a5743b1655',
        params: {
          name: this.projectName,
          desc: this.desc,
          prize_amount: '0x2386f26fc10000',
          due_date: `0x${(((new Date()).getTime() + (7 * 24 * 60 * 60 * 1000)) * 1000).toString(16)}`,
          dpes_score_address: Constants.DPES_SCORE_ADDRESS,
          threshold: `0x${Number(this.threshold).toString(16)}`
        }
      })
    },
    submit: function () {
      this[AT.PROFILE.GET_PROFILE](this.user.id);
    }
  }
};
</script>

<template>
<!-- eslint-disable max-len -->
<div class="pb-5 text-body h-100 bg-light">
  <section class="container">
    <div class="row">
      <div class="offset-md-2 col-md-8">
        <h2 class="font-weight-extra-bold mt-5 pt-3">워크스페이스 생성하기</h2>
        <p class="text-muted mt-1">
          원하시는 워크스페이스를 생성하여, 다양한 목적의 평가를 개설해보세요.
        </p>
      </div>
    </div>
    <form>
      <div class="row mt-5">
        <div class="offset-md-2 col-md-8 pb-5">
          <div class="card border-0 rounded text-left p-5">
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">워크스페이스명</label>
              <input v-model="projectName" type="text" class="form-control" placeholder="워크스페이스명을 입력해주세요.">
            </div>
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">최소 점수 기준</label>
              <select v-model="threshold" class="form-control">
                <option>점수 기준을 선택해주세요...</option>
                <option>50</option>
                <option>60</option>
                <option>70</option>
                <option>80</option>
              </select>
              <small class="form-text text-muted">인센티브를 받을 수 있는 최소 점수 기준을 설정해주세요.</small>
            </div>
            <div class="form-group mt-4">
              <label class="font-weight-bold mb-0" for="">소속 그룹 선택</label>
              <small class="form-text text-muted">해당 워크스페이스에 소속될 그룹을 선택해주세요.</small>
              <div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" checked="true">
                  <label class="form-check-label" for="defaultCheck1">
                    비즈니스기획팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck2">
                  <label class="form-check-label" for="defaultCheck2">
                    글로벌팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck3">
                  <label class="form-check-label" for="defaultCheck3">
                    개발1팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck4">
                  <label class="form-check-label" for="defaultCheck4">
                    개발2팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck5">
                  <label class="form-check-label" for="defaultCheck5">
                    컨설팅팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck6">
                  <label class="form-check-label" for="defaultCheck6">
                    퍼블릭플랫폼팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck7">
                  <label class="form-check-label" for="defaultCheck7">
                    아키텍쳐팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck8">
                  <label class="form-check-label" for="defaultCheck8">
                    인프라팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck9">
                  <label class="form-check-label" for="defaultCheck9">
                    QA팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck10">
                  <label class="form-check-label" for="defaultCheck10">
                    선행기술팀
                  </label>
                </div>
                <div class="form-check mt-2">
                  <input class="form-check-input" type="checkbox" value="" id="defaultCheck11">
                  <label class="form-check-label" for="defaultCheck11">
                    컨센서스팀
                  </label>
                </div>
              </div>
              <div class="form-group mt-4">
                <label class="font-weight-bold mb-0" for="">워크스페이스 컨트랙트 생성</label>
                <div class="input-group mt-1 mb-1">
                  <input :value="newWorkspaceAddress" type="text" class="form-control" placeholder="" style="" disabled>
                  <div class="input-group-append">
                    <button @click="deploy" class="btn btn-outline-secondary" type="button" id="button-addon2">컨트랙트 생성</button>
                  </div>
                </div>
                <small class="form-text text-muted">생성한 워크스페이스의 컨트랙트 주소입니다.</small>
              </div>
            </div>
            <router-link :to="{name: 'setrewardpool'}" tag="button" class="btn btn-secondary mt-4">다음으로</router-link>
          </div>
        </div>
      </div>
    </form>
  </section>
</div>
</template>
