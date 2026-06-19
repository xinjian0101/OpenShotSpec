# OpenShotSpec

A portable JSON format and validator for structured video scene descriptions.

## MVP

- Validate ID, duration, subject, and camera fields
- Check positive duration and required camera type
- Convert structured records into readable production descriptions

## Run

```bash
python main.py scene.json
python main.py scene.json --describe
```

Minimum input:

```json
{"shot_id":"S1","duration":3,"subject":{},"camera":{"shot_type":"medium"}}
```

## Test

```bash
python checks.py
```

## License

MIT
