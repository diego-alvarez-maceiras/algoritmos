"""Comando do intérprete para establecer unha aresta/conexión entre dous nodos."""

from __future__ import annotations

import typing

from graphs import Graph


def connect(
    graph: Graph | None,
    origin_name: str,
    target_name: str,
    weight: str | None = None,
) -> Graph:
    """Establece unha conexión/aresta entre dous nodos do grafo identificados polo seu nome.

    Comportamento:
        - Busca os nodos orixe e destino no grafo polos seus nomes.
        - Se non se especifica `weight`, calcula a distancia euclidiana 3D entre ambos.
        - Establece a aresta no grafo co peso determinado.

    Sintaxe no script:
        CONNECT ISS SAT_1
        CONNECT ISS SAT_1 1500.50

    Args:
        graph (Graph | None): Grafo actual en memoria.
        origin_name (str): Nome do nodo orixe.
        target_name (str): Nome do nodo destino.
        weight (str | None): Peso explícito opcional para a aresta.

    Returns:
        Graph: O grafo actualizado coa nova conexión.

    Raises:
        ValueError: Se o grafo é None ou se algún dos nodos non existe na rede.
    """
    # TODO: [Práctica Alumno]
    # 1. Validar que o grafo non sexa None e que ambos nodos existan (usar `graph.find_by_name`).
    # 2. Determinar o peso da aresta: converter `weight` a float se se indicou, ou calcular a distancia 3D (`origin_node.distance(target_node)`).
    # 3. Crear a conexión mediante `graph.connect(origin_node, target_node, w)`.
    # 4. Imprimir a mensaxe de confirmación e devolver o grafo actualizado.
    ...