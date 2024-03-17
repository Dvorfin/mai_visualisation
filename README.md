# Визуалзация данных от компаса

```python
json_generator.py - генерирует json файлы для передачи (на данный момент не актуально)
publisher.py - mqtt паблишер, использует функцию json_generator.py из mock/mock.py для создания json файлов с данными. Отправляет данные на брокера
subscriber.py - подкючается к брокеру и на данный момент сохраняет данные в папку subscriber/recieved_json (не используется)
mock.py - скрипт генерирующий json файлы с данными по json schema (представлена ниже)
```

### docker-compose.yaml
* создает контейнеры для publisher, subscriber, eclipse mosquitto, telgraf, influxdb и grafana
* для mosquitto копируются файлы конфигурации `mosquitto/config/mosquitto.conf`
* для telegraf копируются файл конфигурации `telegraf/telegraf.conf`
* **важно** в конфиге mosquitto.conf нужно указать параметры `allow_anonymous true` и `listener 1883`. Данные значения необходимы для того, чтобы достучаться до брокера, запущенного в контейнере



### json schema передаваемых данных
- x_grad, y_grad, z_grad - отклонение по трем осям компаса в градусах от севера
- x_a, y_a, z_a - ускорение по трем осям
- time - время получения данных
```json
{
  "type": "object",
  "properties": {
    "x_grad": {
      "type": "number"
    },
    "y_grad": {
      "type": "number"
    },
    "z_grad": {
      "type": "number"
    },
    "x_a": {
      "type": "number"
    },
    "y_a": {
      "type": "number"
    },
    "z_a": {
      "type": "number"
    },
    "time": {
      "type": "string"
    }
  },
  "required": [
    "x_grad",
    "y_grad",
    "z_grad",
    "x_a",
    "y_a",
    "z_a",
    "time"
  ]
}
```



## Инструкция по запуску

#### 1) Установаить докер
```sh
sudo apt update
sudo apt install curl software-properties-common ca-certificates apt-transport-https -y
wget -O- https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable"| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce -y
```

### 2) Установка docker compose
```sh
sudo apt-get install docker-compose
```

#### 3) Установаить git
```sh
sudo apt-get install git
```

#### 4) Скопировать репозиторий
```sh
git clone https://github.com/Dvorfin/mai_visualisation
```

#### 5) Запустить docker compose
```sh
sudo docker compose up
```

#### 6) Запуск grafana
Открыть бразуер и перейти по ip: `http://localhost:3000`


#### Возможные проблемы при заупске:
###### Какой-то сервис занял порт, используемый в docker-compose.yml.
1) запустить:
```sh
netstat | grep 'номер порта'
```
проверить какой сервис использует данный порт и отключиться его командой:
```sh
sudo systemctl stop название_сервиса
```




