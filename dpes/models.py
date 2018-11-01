from django.db import models

# Create your models here.
##################################
############ 모델 구성 #############
##################################
# User; 회원 계정

# Profile; 회원 프로필 계정
# - id: profile_id
# - name: 프로필 명칭
# - department: 프로필의 소속
# - average_rating: 평균 별점
# - grade; 획득 등급

# ProfileQuestion
# - id: question_id
# - profile_id
# - question1: 가장 자랑스러운 업적 2-3개는 무엇이었나요?
# - question2: 당신은 당신의 레벨에 비추어 당신의 지난 6개월을 어떻게 평가하겠습니까? (5단계 Rating으로 평가)
# - question3: 당신의 일이 팀의 성공에 어떻게 기여하였나요? (5단계 Rating으로 평가)
# - question4: 우리 회사의 핵심 가치관 중에 가장 잘 실천한 것은 무엇입니까?
# - question5: 우리 회사의 핵심 가치관 중 더 잘 실천해야 할 것은 무엇입니까?
# - question6: 당신은 어떠한 강점을 가지고 계십니까?
# - question7: 다음 6개월 동안에 반드시 이루거나 성장하고 싶은 영역을 한 가지만 고르면 어떤 것인가요?

# Evaluation; 평가 데이터베이스
# - id
# - from: 평가를 주는 사람
# - to: 평가를 받은 사람
# 1. 평가 대상자와 밀접하게 일한 1-2개의 프로젝트는 무엇이었습니까?
# 2. 질과 양 모든 측면에서 평가 대상자는 프로젝트에 어떻게 기여하였습니까? (5단계 Rating으로 평가)
# 3. 대상자가 팀의 성공에 얼마큼 기여하였습니까? (5단계 Rating으로 평가)
# 1. 우리 회사의 핵심 가치관 중에 가장 잘 실천한 것은 무엇입니까?
# 2. 우리 회사의 핵심 가치관 중 더 잘 실천해야 할 것은 무엇입니까?
# 1. 평가 대상자는 어떠한 강점을 가지고 있습니까?
# 2. 다음 6개월 동안에 평가 대상자가 더 큰 기여를 하기 위해 성장할 영역을 한 가지만 고르면 어떤 것인가요?

# Grade; 평가 등급
# - 평가되지 않음 (None)
# - 기대에 못 미침 (Does not meet expectations)
# - 일부 기대에 부응함 (Meets some expectations)
# - 모든 기대에 부응함 (Meets All Expectations)
# - 기대 이상의 성과를 보임 (Exceeds Expectations)
# - 매우 크게 기대를 초과 달성함 (Greatly Exceeds Expectations)

class Target(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    average_rating = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
