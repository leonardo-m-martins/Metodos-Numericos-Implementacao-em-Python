#!/bin/bash

IMAGE_NAME="metodos-numericos"
CONTAINER_NAME="metodos-numericos"

echo "Parando container antigo (se existir)..."
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

echo "Buildando nova imagem..."
docker build -t $IMAGE_NAME .

echo "Rodando container novo..."
docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME

echo "Atualização concluída!"
