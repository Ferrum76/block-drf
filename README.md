# block-drf

# Для запуска:
1. Заполнить файл .env.sample, изменить его название на .env
2. Ввести команду для поднятия контейнера в docker-compose (в самом файле стоят переменные - об внимание)
```bash
docker compose up
```
3. Запустить команды
```bash
make migrate
make loaddata
make run
```

