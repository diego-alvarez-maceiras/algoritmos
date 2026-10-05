"""Comando do intérprete para eliminar un nodo do grafo."""

from __future__ import annotations

import typing

from graphs import Graph


def remove(graph: Graph | None, node_name: str) -> Graph:
    """Elimina un nodo e todas as súas arestas incidentes do grafo.

    Comportamiento:
        - Atopa o nodo identificado por `node_name`.
        - Elimínao do conxunto de vértices e borra as súas conexións.

    Sintaxe no script:
        REMOVE ISS

    Args:
        graph (Graph | None): Grafo actual en memoria.
        node_name (str): Nome do nodo a eliminar.

    Returns:
        Graph: O grafo actualizado tras a eliminación.

    Raises:
        ValueError: Se o grafo é None ou o nodo non existe.
    """
    # TODO: [Práctica Alumno]
    # 1. Validar que o grafo non sexa None e que o nodo exista no mesmo (usar `graph.find_by_name`).
    # 2. Eliminar o nodo do grafo co método `graph.remove(target_node)`.
    # 3. Imprimir a mensaxe de confirmación e devolver o grafo actualizado.
    ...