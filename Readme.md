# DOMjudge ISAS Deployment

This project deploys a full DOMjudge system with separated Domserver and Judgehost configurations.

## Prerequisites
- Docker
- Docker Compose

## 1. Deploy Domserver
Start the main server and database first.

1.  Navigate to the `domserver` directory:
    ```bash
    cd domserver
    ```
2.  Start the services:
    ```bash
    docker-compose up -d
    ```
3.  **Important**: Retrieve the initial passwords from the logs:
    ```bash
    docker logs domserver-domserver-1 2>&1 | grep "initial"
    ```
    *Note: You will need the "judgehost" password for the next step.*

## 2. Deploy Judgehost
The judgehost can be run on the same machine or a generic separate worker node.

1.  Navigate to the `judgehost` directory:
    ```bash
    cd ../judgehost
    ```
2.  **Configuration**: Edit `docker-compose.yml` before starting!
    *   **DOMSERVER_BASEURL**: Change `http://<DOMSERVER_IP>/` to the actual IP address of your Domserver.
        *   *If running on the same machine, use your LAN IP (e.g., `192.168.1.X`) or host gateway. Do NOT use `localhost`.*
    *   **JUDGEDAEMON_PASSWORD**: set this to the password you found in Step 1.
3.  Start the judgehost:
    ```bash
    docker-compose up -d
    ```

## Services Info
- **Domserver**: Accessible at `http://localhost/` (or your server IP).
- **Database**: Port `13306`.
    - User: `domjudgeisas`
    - Pass: `domjudgeisas`
    - DB: `domjudgeisas`

## Troubleshooting
- **Judgehost not showing up?** Check the logs:
  ```bash
  docker-compose logs -f judgehost
  ```
  *Common issue: 401 Unauthorized (wrong password) or Connection Refused (wrong IP).*

## Special Thanks
- [Borworntat Dendumrongkul](https://github.com/MasterIceZ) for the domjudge docker compose ⭐