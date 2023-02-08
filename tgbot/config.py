from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list
    use_redis: bool
<<<<<<< HEAD
    channel_id: int
=======
    channel_id: list
>>>>>>> 12f5b35e53a1b298bc03d28b8284799360e5e4cd


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
<<<<<<< HEAD
            channel_id=env.int("CHANNEL_ID")
=======
            channel_id=list(map(int, env.list("CHANNEL_ID")))
>>>>>>> 12f5b35e53a1b298bc03d28b8284799360e5e4cd
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )
