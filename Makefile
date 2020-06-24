CONDA_ENV=polling-app

setup:
	@conda create -n ${CONDA_ENV} python=3.7 \
	source $$(conda info --base)/etc/profile.d/conda.sh && \
	conda activate ${CONDA_ENV} && \
	make install

install:
	@python3 -m pip install -U -r requirements.txt

dev:
	@export FLASK_APP=src/main.py && \
	export FLASK_ENV=development && \
	flask run

start:
	@export FLASK_APP=src/main.py && \
	flask run