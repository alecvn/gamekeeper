#!/bin/bash                                                                                                                                                                                                        

BASE_DIR="`dirname \"$0\"`/.."
cd $BASE_DIR

ROOT=`git rev-parse --show-toplevel`
cd ${ROOT}
SRC=${ROOT}/src
SITE_PATH=${SRC}/gamekeeper_api
VENV=${ROOT}/venv


echo "checking for virtualenv"
if [ ! -d ${VENV} ]; then
    cd ${ROOT}
    virtualenv --no-site-packages venv --python=python2.7
fi

echo "activate virtualenv"
cd ${VENV}
. ./bin/activate
if [ $? != 0 ]; then
    echo "failed to activate virtualenv at ${VENV}: ABORTING"
    exit 1
fi
cd -

echo "installing requirements"
cd ${ROOT}
pip install -r requirements.txt
if [ $? != 0 ]; then
    echo "pip install failed: ABORTING"
    exit 1
fi
cd -

cd ${SITE_PATH}/gamekeeper_api
if [ ! -f "local_settings.py" ]; then
    echo "creating default local_settings.py"
    touch local_settings.py
    echo "Please edit ${SITE_PATH}/local_settings.py and set your database configuration based on ${SITE_PATH}/settings.py. Then re-run this script"
    exit 1
fi
cd -

echo "Fixing log folder permissions"
cd ${ROOT}
mkdir -p logs

echo "updating database"
cd ${SITE_PATH}
python manage.py migrate --settings=gamekeeper_api.settings
if [ $? != 0 ]; then
    echo "db migrate failed: ABORTING"
    exit 1
fi

echo "Creating media folder"
cd ${ROOT}
if [ ! -d "media" ]; then
    mkdir "media"
fi

echo "collecting static files"
cd ${SITE_PATH}
python manage.py collectstatic --noinput --verbosity=0 --settings=gamekeeper_api.settings
cd -

echo "Deploy local complete"
