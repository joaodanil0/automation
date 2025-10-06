#!/bin/bash

# Nome padrão da imagem e do container
IMAGE_NAME="appium-image"
CONTAINER_NAME="appium-container"

# Mostrar ajuda
function ajuda() {
    echo "Uso: $0 [comando]"
    echo "Comandos disponíveis:"
    echo "  build        - Buildar a imagem Docker"
    echo "  run          - Rodar o container interativo"
    echo "  start        - Iniciar um container parado"
    echo "  stop         - Parar o container em execução"
    echo "  remove       - Remover container e imagem"
    echo "  shell        - Entrar no bash do container"
    echo "  images       - Listar imagens Docker"
    echo "  containers   - Listar containers Docker"
    echo "  logs         - Ver logs do container"
}

# Buildar imagem
function build() {
    echo "Construindo imagem: $IMAGE_NAME"
    docker build -t $IMAGE_NAME .
}

# Rodar container
function run() {
    echo "Executando container: $CONTAINER_NAME"
    # docker run -it --name $CONTAINER_NAME $IMAGE_NAME
    docker run -d --network host --privileged -v /dev/bus/usb:/dev/bus/usb --name $CONTAINER_NAME -it $IMAGE_NAME
}

# Start container existente
function start() {
    echo "Iniciando container: $CONTAINER_NAME"
    docker start -ai $CONTAINER_NAME
}

# Parar container
function stop() {
    echo "Parando container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
}

# Remover container e imagem
function remove() {
    echo "Removendo container e imagem..."
    docker rm -f $CONTAINER_NAME
    docker rmi -f $IMAGE_NAME
}

# Entrar no bash do container
function shell() {
    echo "Abrindo shell do container: $CONTAINER_NAME"
    docker exec -it $CONTAINER_NAME bash
}

# Listar imagens
function images() {
    docker images
}

# Listar containers
function containers() {
    docker ps -a
}

# Ver logs
function logs() {
    docker logs $CONTAINER_NAME
}

# Lógica principal
case "$1" in
    build) build ;;
    run) run ;;
    start) start ;;
    stop) stop ;;
    remove) remove ;;
    shell) shell ;;
    images) images ;;
    containers) containers ;;
    logs) logs ;;
    *) ajuda ;;
esac
