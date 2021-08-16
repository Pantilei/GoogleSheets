import uvicorn

if __name__ == "__main__":
    uvicorn.run("GoogleSheets.app:app", port=8080,
                host='0.0.0.0', reload=False)
