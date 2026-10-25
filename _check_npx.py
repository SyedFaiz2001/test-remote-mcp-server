import os
import sys
import shutil
import subprocess
import importlib.metadata

print("Python executable:", sys.executable)
print("PATHEXT:", repr(os.getenv("PATHEXT")))

print("\n--- Command lookup ---")
for name in ("node", "npm", "npm.cmd", "npx", "npx.cmd", "npx.exe"):
    print(f"{name}: {shutil.which(name)!r}")

print("\n--- Command execution ---")
for command in ("node --version", "npm.cmd --version", "npx.cmd --version"):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=20
        )
        print(f"\nCommand: {command}")
        print("Exit code:", result.returncode)
        print("STDOUT:", repr(result.stdout))
        print("STDERR:", repr(result.stderr))
    except Exception as exc:
        print(f"\nCommand: {command}")
        print("Exception:", repr(exc))

print("\n--- Installed package versions ---")
for package in ("fastmcp", "mcp"):
    try:
        print(f"{package}: {importlib.metadata.version(package)}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{package}: not installed")
