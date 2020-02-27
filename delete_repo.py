from github import Github
import os
 
g = Github("leechungkyu", "password123!")
 
# Github Token 값
github_token = '8a45b2e8bd7f09db0733a2a560c268e367fc1620'
 
# 전체 저장소 명 확인
for repo in g.get_user().get_repos():
    print(repo.name)
 
# 삭제할 저장소 명 기입
repo_name = 'helloworld-20190220'
 
# 삭제할 명령어 # https://api.github.com/repos/<github_id>/<repo_name>
cmd = "curl -X DELETE -H \'Authorization: token " + github_token + "\' " + "https://api.github.com/repos/leechungkyu/" + repo_name
print(cmd)
 
# 삭제 실행
print(os.system(cmd))
