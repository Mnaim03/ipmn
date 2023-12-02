#!/bin/bash
op="$1"
host="$2"
# op=0 --> PULL
# op≠0 --> PUSH

if [ $op -eq 0 ]; then

    echo ""
    echo -e "\033[35m########################################\033[0m"
    echo -e "\033[35m######### PULL GIT REPO ################\033[0m"
    echo -e "\033[35m########################################\033[0m"
    echo ""

    git pull  

    chmod +x pull_push.py
    python3 pull_push.py 0 $host

    echo -e "\033[32m Pull eseguita correttamente. \033[0m"
else

    echo "" 
    echo -e "\033[35m########################################\033[0m"
    echo -e "\033[35m######### PUSH GIT REPO ################\033[0m"
    echo -e "\033[35m########################################\033[0m"

    #installa gh
     git add ./*
     git commit -m 'Update'
     git push

     chmod +x pull_push.py
     python3 pull_push.py 3 $host

     echo -e "\033[32m Commit & Push eseguito \033[0m"

fi
