#!/bin/bash                                                                                                                                                                                                        

BASE_DIR="`dirname \"$0\"`/.."
cd $BASE_DIR

ROOT=`git rev-parse --show-toplevel`
cd ${ROOT}
VENV=${ROOT}/venv

./scripts/deploy_local.sh

cd ${VENV}
. ./bin/activate
if [ $? != 0 ]; then
    echo "failed to activate virtualenv at ${VENV}: ABORTING"
    exit 1
fi

cd ${ROOT}

sudo chown -R www-data:$(whoami) logs

sudo chmod ug+w -R logs
sudo chmod ug+w -R media

sudo /etc/init.d/apache2 reload

echo "Done"
