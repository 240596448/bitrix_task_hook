# Bitrix-hook транслятор в http-service 1С

- сборка docker-образа  
```sh
docker build . --tag bitrix-hook-translator
```

- запуск контейнера  
```sh
docker run -d --rm \
    --name bitrix-hook-translator \
    --env-file .env \
    -p 5000:5000 \
    bitrix-hook-translator
```
или  
```sh
docker-compose up -d
```