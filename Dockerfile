FROM python:3

WORKDIR /usr/scr/app

COPY Lena-Noisy-image.png .

COPY Denoising_Image.py