# Визуалзация данных от компаса

```python
json_generator.py - генерирует json файлы для передачи (на данный момент не актуально)
publisher.py - mqtt паблишер, использует функцию json_generator.py из mock/mock.py для создания json файлов с данными. Отправляет данные на брокера
subscriber.py - подкючается к брокеру и на данный момент сохраняет данные в папку subscriber/recieved_json
```

### docker-compose.yaml
* создает контейнеры для publisher, subscriber и eclipse mosquitto
* для mosquitto копируются файлы конфигурации
* **важно** в конфиге mosquitto.conf нужно указать параметры **allow_anonymous true** и **listener 1883**. Данные значения необходимы для того, чтобы достучаться до брокера, запущенного в контейнере


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



### Инструкция по запуску

#### 1) Установаить докер
```sh
sudo apt install docker
```

#### 2) Установаить докер
```sh
git clone https://github.com/Dvorfin/mai_visualisation
```

#### 3) Запустить docker compose
```sh
sudo docker compose up
```