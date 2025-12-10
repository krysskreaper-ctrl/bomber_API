# bomber_API
Small and Easy Fast API integrated with SMS Bomber (Only for Educational Purpose)
<p>How to use: <p>
![Example](https://user-images.githubusercontent.com/56478595/131145418-61f8d668-3c10-4173-8b33-50f50685b2ff.png)

## Extra tooling

The API now exposes a helper endpoint to locate files whose names or contents
mention dragon-related keywords ("dragon", "dragon36", "3.6", "3_6"). Call the
endpoint while the app is running to receive a list of matches relative to the
provided root path:

```bash
curl "http://localhost:8000/dragons?root=."
```


