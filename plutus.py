# Third Party
import loglifos
import uvicorn

# Local
from src.routers.base.base_router import BaseRouter

app = BaseRouter.register_routers()


loglifos.set_config(log_level=loglifos.WARNING)

if __name__ == "__main__":
    uvicorn.run(app=app)
