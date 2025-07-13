# Discord Invite Rewards Bot

Este proyecto es un bot de Discord que permite a los usuarios reclamar premios al invitar a otras personas a un servidor. El bot gestiona las invitaciones y las recompensas asociadas a ellas.

## Estructura del Proyecto

```
discord-invite-rewards-bot
├── src
│   ├── bot.py                # Punto de entrada del bot de Discord
│   ├── commands
│   │   └── invite_rewards.py  # Comando para manejar recompensas por invitaciones
│   ├── utils
│   │   └── database.py        # Funciones para interactuar con la base de datos
│   └── config.py              # Configuraciones del bot
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## Requisitos

Asegúrate de tener Python 3.8 o superior instalado en tu sistema. También necesitarás instalar las dependencias listadas en `requirements.txt`.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd discord-invite-rewards-bot
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configura el archivo `src/config.py` con tu token de Discord y la configuración de la base de datos.

## Ejecución

Para ejecutar el bot, utiliza el siguiente comando:
```
python src/bot.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.