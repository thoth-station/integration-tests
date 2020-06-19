FROM quay.io/thoth-station/s2i-thoth-ubi8-py36

ENV NO_INSTALL=1

COPY . $HOME

RUN micropipenv install --deploy
