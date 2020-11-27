FROM python:3

WORKDIR /usr/scr/app

COPY Lena-Noisy-image.png .

COPY Denoising_Image.py .


RUN pip install numpy 

RUN pip install scikit-image


CMD ["python", "./Denoising_Image.py"]