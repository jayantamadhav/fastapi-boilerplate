# Banjararide


# Run Migration

Only once

```aerich init -t config.TORTOISE_ORM```

```aerich init-db```

Everytime for migrations

```aerich migrate```

```aerich upgrade```

Run the app

uvicorn main:app --reload