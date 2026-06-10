from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.teams import router as teams_router
from api.simulate import router as simulate_router

app = FastAPI(
    title="Football Simulation API",
    description="国家队足球比赛智能体模拟系统",
    version="1.0.0"
)

# 允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 前端可以部署到任何域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 注册模拟比赛API
app.include_router(
    simulate_router,
    prefix="/api",
    tags=["simulate"]
)


app.include_router(
    teams_router, 
    prefix="/api", 
    tags=["teams"])


@app.get("/")
def root():
    return {"message": "Welcome to Football Simulation API!"}