"""Comando do intérprete para inicializar un novo Grafo."""

from __future__ import annotations

import typing

from graphs import Graph, Node
from utils import parse_json_to_node

T = typing.TypeVar("T")
E = typing.TypeVar("E")

def create(graph: Graph[T, E] | None, value: str) -> Graph[Node, float]:

    """Crea un novo nodo a partir dunha cadea JSON e incorpórao ao grafo.

    Comportamento:
        - Se o grafo recibido (`graph`) é `None`, instánciase un novo obxecto `Graph`:
            * Se se indica a opción `--directed`, créase un grafo dirixido (`directed=True`).
            * En caso contrario, créase un grafo non dirixido por defecto (`directed=False`).
        - Se o grafo xa existe (`graph is not None`), engádese o novo nodo mantendo
          a orientación orixinal da estrutura.

    Notas pedagóxicas de implementación:
        O argumento `value` recíbese como unha cadea de texto en formato JSON. Antes
        de engadilo ou instanciar o grafo, dita cadea debe deserializarse nunha instancia
        do modelo `Node` (mediante `utils.parse_json_to_node`).

    Sintaxe no script:
        CREATE '{"name": "ISS", "x": 0.0, "y": 0.0, "z": 408.0}'
        CREATE '{"name": "ISS", "x": 0.0, "y": 0.0, "z": 408.0}' --directed

    Args:
        graph (Graph[T, E] | None): Grafo actual en memoria ou None se aínda non existe.
        value (str): Cadea en formato JSON que representa o nodo a engadir.
        mode (str | None): Flag opcional ('--directed') para indicar a orientación do grafo inicial.

    Returns:
        Graph[Node, float]: O grafo actualizado co novo nodo incorporado.

    Raises:
        json.JSONDecodeError: Se `value` non é un JSON válido.
        TypeError: Se os campos do JSON non coinciden coa clase do modelo.
    """
    # TODO: [Práctica Alumno]
    # 1. Deserializar o string JSON `value` a un obxecto Node (`utils.parse_json_to_node(value)`).
    # 2. Se `graph` é None, instanciar un novo `Graph[Node, float]` aplicando a orientación indicada no argumento `directed`.
    #    Se xa existe, engadir o nodo co método `graph.add(node)`.
    # 3. Imprimir a mensaxe de confirmación e devolver o grafo.
    ...