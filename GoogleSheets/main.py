import uvicorn

if __name__ == "__main__":
    uvicorn.run("GoogleSheets.app:app", port=5001,
                host='localhost', reload=True)
