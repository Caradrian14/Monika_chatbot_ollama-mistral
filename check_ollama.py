#!/usr/bin/env python3
"""
check_ollama.py
check if ollama is running
"""

import subprocess
import sys
import socket
import json
import urllib.request
import urllib.error
from typing import Tuple

HOST = "127.0.0.1"
PORT = 11434 #ollama port
MODELS_PATH = "/v1/models"
HTTP_TIMEOUT = 2.0  # segundos


def check_cli_ollama() -> Tuple[bool, str]:
    """
    Intenta ejecutar `ollama list`. Si el comando existe y responde,
    consideramos que Ollama está accesible vía CLI (y normalmente el servicio).
    Devuelve (ok, salida_o_error).
    """
    try:
        # llamamos con timeout para no quedar colgados
        proc = subprocess.run(
            ["ollama", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
        )
        if proc.returncode == 0:
            return True, proc.stdout.strip()
        else:
            # Si el comando existe pero la conexión fue rechazada, lo devolvemos
            return False, proc.stderr.strip() or proc.stdout.strip()
    except FileNotFoundError:
        return False, "Comando 'ollama' no encontrado (no instalado en PATH)."
    except subprocess.TimeoutExpired:
        return False, "Ejecución de 'ollama list' expiró (timeout)."
    except Exception as e:
        return False, f"Error ejecutando 'ollama list': {e}"


def check_port_open(host: str = HOST, port: int = PORT, timeout: float = 1.0) -> Tuple[bool, str]:
    """
    Comprobar si hay un listener TCP en host:port.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True, f"Puerto {host}:{port} aceptó la conexión."
    except socket.timeout:
        return False, f"Timeout al conectar a {host}:{port}."
    except ConnectionRefusedError:
        return False, f"Conexión rechazada en {host}:{port}."
    except Exception as e:
        return False, f"Error al comprobar puerto: {e}"


def check_http_models(host: str = HOST, port: int = PORT, path: str = MODELS_PATH, timeout: float = HTTP_TIMEOUT) -> Tuple[bool, str]:
    """
    Make a get to http://host:port/path and parese JSON, if returns a JSON with an okat strature the API goes well and Monika happy
    """
    url = f"http://{host}:{port}{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "check_ollama/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ct = resp.getheader("Content-Type", "")
            body = resp.read().decode(errors="ignore")
            # Intentamos parsear JSON
            try:
                data = json.loads(body)
                # Comprobación básica: esperamos lista o dict
                if isinstance(data, (list, dict)):
                    # información resumida útil
                    summary = f"HTTP {resp.status} {resp.reason} ; Content-Type: {ct} ; JSON parse ok."
                    return True, summary
                else:
                    return False, "HTTP:Okay but strange JSON"
            except json.JSONDecodeError:
                return False, "HTTP: Okay but JSON not Okay"
    except urllib.error.HTTPError as he:
        return False, f"HTTP error {he.code}: {he.reason}"
    except urllib.error.URLError as ue:
        return False, f"URL error: {ue.reason}"
    except socket.timeout:
        return False, "Timeout in request HTTP."
    except Exception as e:
        return False, f"Error in request  HTTP: {e}"


def main() -> int:
    ok_cli, out_cli = check_cli_ollama()
    if ok_cli:
        print("[1] CLI: 'ollama list' -> OK")
        print(out_cli[:200] + ("" if len(out_cli) <= 200 else "... (truncado)"))

        #If Cli responds OK, LLM goes nice but keep looking
    else:
        print(f"[1] CLI: 'ollama list' -> NO. Detail: {out_cli}")

    ok_port, out_port = check_port_open()
    if ok_port:
        print(f"[2] Socket: {out_port}")
    else:
        print(f"[2] Socket: {out_port}")

    ok_http, out_http = check_http_models()
    if ok_http:
        print(f"[3] HTTP: API is Okay: {out_http}")
    else:
        print(f"[3] HTTP: Fail: {out_http}")

    if ok_port and ok_http:
        print("\n=> Result: Ollama looks RUNNING and Api responf okay.")
        return 0
    if ok_cli:
        print(
            "\n=> Result: 'ollama' CLI respond, but port/API no respond.")
        return 1

    print("\n=> Result: Ollama is NOT looking running inlocalhost:11434 (no 'ollama' accesible).")
    return 1


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
