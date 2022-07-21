# echo 'ghp_XXX' | gh auth login --with-token
gh api -H 'Accept: application/vnd.github.v3+json' "/orgs/w3c/teams/w3c-group-87846-members/members?per_page=100" > w3c-87846.json
gh api -H 'Accept: application/vnd.github.v3+json' "/orgs/w3c/teams/w3c-group-109735-members/members?per_page=100" > w3c-109735.json
gh api -H 'Accept: application/vnd.github.v3+json' "/orgs/immersive-web/teams/w3c-group-87846-members/members?per_page=100" > iwwg-87846.json
gh api -H 'Accept: application/vnd.github.v3+json' "/orgs/immersive-web/teams/w3c-group-109735-members/members?per_page=100" > iwwg-109735.json
ls -1 *json | awk '{print "./print_login.py", $1,"|sort > " $1 "-list"}'
