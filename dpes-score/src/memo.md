// start
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate venv36

// deploy dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json

// update dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json -m update -o cx9b8e46f4452b56be19557a21bc436c3fc44d2467

// send icx to contract
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/send_icx_to_contract.json

// call create_parent_dict
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/create_parent_dict.json

// call create_parent_dict demo
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/create_parent_dict_demo.json

// parent array mock
[{"address":"hx435b4dd5f623f2e31c691bf480902a3056b828ac","limit":2,"name":"글로벌팀","parent_level":1},{"address":"hx4ed9e9c34451bd3ceb85a7530cb0b0986fd46f79","limit":2,"name":"개발1팀","parent_level":1},{"address":"hx6efa0281337beea3c3888398e0cba640482aec36","limit":1,"name":"임원진","parent_level":2}]
[
    {
        "address": "hx435b4dd5f623f2e31c691bf480902a3056b828ac",
        "limit": 2,
        "parent_name": "글로벌팀",
        "parent_level": 1
    },
    {
        "address": "hx4ed9e9c34451bd3ceb85a7530cb0b0986fd46f79",
        "limit": 2,
        "parent_name": "개발1팀",
        "parent_level": 1
    },
    {
        "address": "hx6efa0281337beea3c3888398e0cba640482aec36",
        "limit": 1,
        "parent_name": "임원진",
        "parent_level": 2
    }
]

// call sign_up
tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_1.json

tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_2.json

tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_L.json

tbears sendtx -k ../keystores/Parent2.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_2_1.json

tbears sendtx -k ../keystores/Parent2.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_2_2.json

tbears sendtx -k ../keystores/Parent2.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_2_L.json

tbears sendtx -k ../keystores/OracleParent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_O_1.json

// deploy project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json

// update project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json -m update -o cx48b7224207fac3a8c2903c2ceefd9c25b1239f76

// vote
tbears sendtx -k ../keystores/P1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_1_t_1_1.json

tbears sendtx -k ../keystores/P1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_1_t_1_2.json

tbears sendtx -k ../keystores/P1-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_2_t_1_1.json

tbears sendtx -k ../keystores/P1-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_2_t_1_2.json

tbears sendtx -k ../keystores/P2-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_2_1_t_2_1.json

tbears sendtx -k ../keystores/P2-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_2_1_t_2_2.json

tbears sendtx -k ../keystores/P2-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_2_2_t_2_1.json

tbears sendtx -k ../keystores/P2-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_2_2_t_2_2.json

tbears sendtx -k ../keystores/O1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_O_1_t_1_1.json

tbears sendtx -k ../keystores/O1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_O_1_t_1_2.json

tbears sendtx -k ../keystores/O1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_O_1_t_2_1.json

tbears sendtx -k ../keystores/O1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_O_1_t_2_2.json

// call close vote
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/close_vote.json

// team validate
tbears sendtx -k ../keystores/P1-L.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/audit_vote_1.json

tbears sendtx -k ../keystores/P2-L.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/audit_vote_2.json
