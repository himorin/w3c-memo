#! /bin/sh

# all targets are at local and in one directory
dirs=`find . -maxdepth 1 -type d`
gitcmd='git remote set-url origin'

# target
3new_origin='git@github.com:immersive-web/'
new_origin='https://github.com/immersive-web/'

for dir in $dirs;
do
  if [ ! -d "${dir}/.git" ]; then
    echo "Directory $dir is not git repository"
    continue
  fi
  echo "Working on $dir"
  cd $dir
  tgt="${new_origin}`echo $dir | cut -c 3-`"
  eval "$gitcmd $tgt"
  cd ..
done

