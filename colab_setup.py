import os
from google.colab import auth

os.system('pip install --upgrade pip==20.2.2')
os.system('rm -rf sample_data')
os.system('unzip Object_detection_in_urban_environments.zip')
os.system(
    'pip install -r Object_detection_in_urban_environments/build/requirements.txt')
os.system(
    'echo "deb http://packages.cloud.google.com/apt gcsfuse-`lsb_release -c -s` main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list')
os.system(
    'curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -')
os.system('sudo apt-get -y -q update')
os.system('sudo apt-get -y -q install gcsfuse')
auth.authenticate_user()
os.system('mkdir -p data/training')
os.system('mkdir -p data/validation')
os.system('mkdir -p data/testing')
os.system('gcsfuse --only-dir training/ waymo_open_dataset_v_1_2_0_individual_files data/training/')
os.system('gcsfuse --only-dir validation/ waymo_open_dataset_v_1_2_0_individual_files data/validation/')
os.system('gcsfuse --only-dir testing/ waymo_open_dataset_v_1_2_0_individual_files data/testing/')
os.system('pip3 install --upgrade tensorflow==2.3.1')
os.system('git clone --depth 1 https://github.com/tensorflow/models')
os.system('apt-get install -qq protobuf-compiler python-pil python-lxml python-tk')
os.system('pip install -q Cython contextlib2 pillow lxml matplotlib')
os.system('pip install -q pycocotools')
os.chdir("/content/models/research")
os.system('protoc object_detection/protos/*.proto --python_out=.')
os.system('cp object_detection/packages/tf2/setup.py .')
os.system('python -m pip install --use-feature=2020-resolver .')
os.system('pip install git+https://github.com/google-research/tf-slim')
os.system('pip install tf-models-official')
os.system('pip install matplotlib==3.1.0')
