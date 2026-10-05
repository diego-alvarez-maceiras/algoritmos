"""Comando do intérprete para buscar e mostrar a información dun nodo."""

from __future__ import annotations

import typing

from graphs.Graph import Graph


def find(graph: Graph | None, node_name: str) -> Graph:
    """Busca un nodo no grafo polo seu nome e mostra a súa información por consola.

    Comportamento:
        - Localiza o nodo e imprime os seus detalles técnicos.
        - Non modifica o estado do grafo.

    Sintaxe no script:
        FIND ISS

    Args:
        graph (Graph | None): Grafo actual en memoria.
        node_name (str): Nome do nodo a buscar.

    Returns:
        Graph: O mesmo grafo recibido, sen modificacións.

    Raises:
        ValueError: Se o grafo é None.
    """
    # TODO: [Práctica Alumno]
    # 1. Validar que o grafo non sexa None (lanzar ValueError en caso contrario).
    # 2. Buscar o nodo polo seu nome mediante `graph.find_by_name(node_name)`.
    # 3. Imprimir os detalles do nodo se existe, ou a mensaxe correspondente se non se atopou.
    # 4. Devolver o grafo orixinal.
    ...