# DOMjudge ISAS Deployment

This project deploys a full DOMjudge system (Domserver + Judgehost) using Docker Compose.

## Prerequisites
- Docker
- Docker Compose

## Quick Start
1.  Navigate to the `domserver` directory:
    ```bash
    cd domserver
    ```
2.  Start the services:
    ```bash
    docker-compose up -d
    ```

## Services
- **Mariadb**: Database backend.
- **Domserver**: The main web interface for DOMjudge (accessible at port 80).
- **Judgehost**: The worker node that compiles and runs submissions.

## Default Credentials
- **Database**: `domjudgeisas` / `domjudgeisas`
- **Judgehost Password**: `domjudgeisas`
- **Admin Password**: (Check the logs of the domserver container on first launch, or set via `docker exec`)
  ```bash
  docker logs domserver-domserver-1 | grep "initial admin password"
  ```

## Special Thanks
- [Borworntat Dendumrongkul](https://github.com/MasterIceZ) for the domjudge docker compose ⭐