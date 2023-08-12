CREATE TABLE
  users(
    "tg_id" INT UNIQUE PRIMARY KEY,
    "uuid" VARCHAR(50) COMMENT 'ID юзера в Telegram',
    "phone" VARCHAR(30),
    "name" VARCHAR(60),
    "count" INT NULL DEFAULT 2 COMMENT 'Число попыток',
    "finish" BOOLEAN NULL COMMENT 'Завершенность квеста',
    "branch" VARCHAR(255) COMMENT 'Ветка – аналитик / программист и т.д.',
    "result_time" TIMESTAMP COMMENT 'Время окончания квеста',
    "is_login" VARCHAR(30),
    "is_uid" VARCHAR(11)
  )
