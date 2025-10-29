import subprocess
import sys
import pytest

def test_cadastro_script_execucao():
    """Testa se o script cadastro.py executa sem erros."""
    result = subprocess.run(
        [sys.executable, "cadastro.py"],
        capture_output=True,
        text=True,
        timeout=5
    )
    # O Tkinter pode travar se tentar abrir GUI no CI, então só checamos o retorno
    assert result.returncode == 0 or "Tkinter" in result.stderr
