// start
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate venv36

// deploy dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json

// update dpes score
tbears deploy dpes_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json -m update -o cx635118b9865c8cddee4759dff5d29360f5664d5a

// send icx to contract
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/send_icx_to_contract.json

// call create_parent_dict demo
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/create_parent_dict_demo.json

// call sign_up
tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_1.json

tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_2.json

tbears sendtx -k ../keystores/Parent1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/sign_up_1_L.json

// deploy project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json

// update project score
tbears deploy dpes_project_score -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json -m update -o cxb787980518b717a7f986500576c6a24c0294ed64

// vote
tbears sendtx -k ../keystores/P1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_1_t_1_1.json

tbears sendtx -k ../keystores/P1-1.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_1_t_1_2.json

tbears sendtx -k ../keystores/P1-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_2_t_1_1.json

tbears sendtx -k ../keystores/P1-2.json -p "@1234qwer" -c ../config/deploy_dpes_project_score.json ../config/vote_f_1_2_t_1_2.json

// call close vote
tbears sendtx -k ../keystores/Admin1.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/close_vote.json

// team validate
tbears sendtx -k ../keystores/P1-L.json -p "@1234qwer" -c ../config/deploy_dpes_score.json ../config/audit_vote_1.json