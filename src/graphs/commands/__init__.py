"""Paquete que expón o catálogo de comandos executables polo intérprete.

Cada módulo neste paquete implementa un comando concreto compatible co intérprete.
O intérprete mapea a primeira palabra de cada liña lida nun script (en minúsculas)
coa función correspondente aquí exportada.

Comandos dispoñibles na práctica de grafos:
    - CREATE <json_str>: Engade un novo nodo ao grafo a partir dunha cadea JSON.
    - LOAD <ruta_ficheiro> [alcance_máx]: Carga satélites dende un JSON e conecta opcionalmente por distancia.
    - CONNECT <orixe> <destino> [peso]: Crea unha aresta entre dous nodos do grafo.
    - DISCONNECT <orixe> <destino>: Elimina a aresta existente entre dous nodos.
    - REMOVE <nome>: Elimina un nodo e todas as súas conexións do grafo.
    - FIND <nome>: Busca un nodo no grafo e amosa a súa información detallada.
    - PRINT: Imprime a estrutura do grafo (matriz de adxacencia).
    - TRAVEL <orixe> [WIDTH|DEPTH]: Executa un percorrido en anchura (BFS) ou profundidade (DFS).
    - PATH <orixe> <destino>: Calcula o camiño máis curto entre dous nodos mediante Dijkstra.
    - COMPONENTS: Identifica e amosa as compoñentes conexas da rede.
    - CUT_VERTICES: Atopa os puntos de articulación (vértices de corte) do grafo.
"""

from .components import components
from .connect import connect
from .create import create
from .find_cut_vertices import find_cut_vertices
from .disconnect import disconnect
from .find import find
from .load import load
from .path import path
from .print import print
from .remove import remove
from .travel import travel

__all__ = [
    "components",
    "connect",
    "create",
    "find_cut_vertices",
    "disconnect",
    "find",
    "load",
    "path",
    "print",
    "remove",
    "travel",
]