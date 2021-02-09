#! /bin/sh

# all targets are at local and in one directory
dirs=`find . -maxdepth 1 -type d`

# defs
check_main="git for-each-ref --format='%(refname:short)' | grep '^main$'"
ghactions='.github/workflows'
commit_msg='Updated GHActions file see https://github.com/immersive-web/administrivia/issues/151'
gitpush="git push"

for dir in $dirs;
do
  if [ ! -d "${dir}/.git" ]; then
    echo "Directory $dir is not git repository"
    continue
  fi
  echo "Working on $dir"
  cd $dir
  out=`eval ${check_main}`
  if [ ! "x$out" = "xmain" ]; then
    echo "$dir does not have main branch"
    cd ..
    continue
  fi
  git checkout -q main
  if [ $? -gt 0 ]; then
    echo "ERROR: git checkout main failed on $dir"
    cd ..
    continue
  fi
  git pull -q
  if [ $? -gt 0 ]; then
    echo "ERROR: git pull failed on $dir"
    cd ..
    continue
  fi
  if [ ! -d "$ghactions" ]; then
    echo "$dir does not have GHActions directory"
    cd ..
    continue
  fi

  # Write your operation here
  cp ../deploy.yml .github/workflows/deploy.yml

  # commit and push
  git commit -a -m "$commit_msg"
  if [ $? -gt 0 ]; then
    echo "Commit failed for $dir"
    cd ..
    continue
  fi
  out=`eval ${gitpush}`
  if [ $? -gt 0 ]; then
    echo "Push failed for $dir"
    cd ..
    continue
  fi

  echo "Finished for $dir"
  cd ..
done

