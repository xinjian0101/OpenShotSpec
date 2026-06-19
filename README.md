# OpenShotSpec

A portable JSON format and validator for video shot descriptions.

## MVP

- Validate shot ID, duration, subject, and camera fields
- Check positive duration and required shot type
- Convert structured shot data into a readable description
- Include a JSON Schema

## Run

```bash
python main.py examples/shot.json
python main.py examples/shot.json --describe
```

## Test

```bash
python -m unittest -v
```

## License

MIT
