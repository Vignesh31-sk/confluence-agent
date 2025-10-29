from google.adk.cli.fast_api import get_fast_api_app
import uvicorn

app = get_fast_api_app(web=True, agents_dir="agents")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
