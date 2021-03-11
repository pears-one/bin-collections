git fetch --all --tags
git checkout main
git branch -d live
latest_tag=$(git describe --tags `git rev-list --tags --max-count=1`)
git checkout tags/$latest_tag -b live
