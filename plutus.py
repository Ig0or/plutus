# Third Party
from decouple import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyfiglet import print_figlet
import loglifos
import uvicorn

# Local
from src.routers.base.base_router import BaseRouter

loglifos.set_config(log_level=loglifos.WARNING)


def build_app() -> FastAPI:
    app = BaseRouter.register_routers()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = build_app()

if __name__ == "__main__":
    port = int(config("SERVER_PORT"))

    print_figlet(text="Plutus", colors="76;0;153")
    uvicorn.run(app=app, port=port, host="0.0.0.0")
