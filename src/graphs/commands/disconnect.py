"""Comando do intérprete para eliminar unha aresta entre dous nodos."""

from __future__ import annotations

import typing

from graphs.Graph import Graph


def disconnect(
    graph: Graph | None,
    origin_name: str,
    target_name: str,
) -> Graph:
    """Elimina a conexión/aresta existente entre dous nodos do grafo.

    Comportamiento:
        - Localiza os nodos orixe e destino polos seus nomes.
        - Elimina a aresta existente entre ambos mantendo os nodos na rede.

    Sintaxe no script:
        DISCONNECT ISS SAT_1

    Args:
        graph (Graph | None): Grafo actual en memoria.
        origin_name (str): Nome do nodo orixe.
        target_name (str): Nome do nodo destino.

    Returns:
        Graph: O grafo actualizado tras eliminar a conexión.

    Raises:
        ValueError: Se o grafo é None ou se os nodos non existen.
    """
    # TODO: [Práctica Alumno]
    # 1. Validar que o grafo non sexa None e que os dous nodos existan (usar `graph.find_by_name`).
    # 2. Eliminar a aresta entre eles usando `graph.disconnect(origin_node, target_node)`.
    # 3. Imprimir a mensaxe de confirmación e devolver o grafo actualizado.
    ...