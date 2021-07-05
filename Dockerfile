FROM python:3.7

RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_trf

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD . /sensitive_info_detector
WORKDIR /sensitive_info_detector
ENV PYTHONPATH /sensitive_info_detector

EXPOSE 4200
CMD streamlit run app.py