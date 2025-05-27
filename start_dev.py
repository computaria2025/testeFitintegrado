import os
import subprocess
import threading


def run_command(cmd, cwd=None):
    process = subprocess.Popen(cmd, cwd=cwd, shell=True)
    return process


def run_frontend():
    print("🚀 Iniciando React Dev Server (npm start)...")
    subprocess.run("npm install", cwd="frontend", shell=True)
    run_command("npm start", cwd="frontend").wait()


def run_backend():
    print("🚀 Iniciando Backend Flask...")
    backend_dir = "backend"

    # Ativar ambiente virtual se quiser, ou garantir que já esteja ativo
    venv_python = os.path.join(backend_dir, "venv", "Scripts", "python.exe") if os.name == 'nt' else os.path.join(
        backend_dir, "venv", "bin", "python")

    if os.path.exists(venv_python):
        python_exec = venv_python
    else:
        python_exec = "python"

    run_command(f"{python_exec} app.py", cwd=backend_dir).wait()


if __name__ == "__main__":
    frontend_thread = threading.Thread(target=run_frontend)
    backend_thread = threading.Thread(target=run_backend)

    frontend_thread.start()
    backend_thread.start()

    frontend_thread.join()
    backend_thread.join()